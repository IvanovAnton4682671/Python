
import re
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
import hashlib
import random


def search_email(input_email):
    users = Users.objects.filter(email=input_email)
    if not users:
        return True
    else:
        return False


def checking_for_availability(input_email, input_password):
    user = Users.objects.filter(email=input_email, password=input_password)
    if not user:
        return False
    else:
        return True


def get_user(input_email):
    user = Users.objects.get(email=input_email)
    return user


def sign_up(request):
    return render(request, "sign_up/sign_up.html")


def sign_up_sending(request):
    surname = request.POST.get("surname", "-undefined-")
    name = request.POST.get("name", "-undefined-")
    patronymic = request.POST.get("patronymic", "-undefined-")
    email = request.POST.get("email", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    name_regex = r"^([А-ЯЁ][а-яё]+)$"
    email_regex = r"^[^@]+@[^@]+\.[a-zA-Z]{2,5}$"
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{8,}$"

    error_surname, error_name, error_patronymic, error_email, error_password = '', '', '', '', ''
    kol = 0

    if not re.match(name_regex, surname):
        error_surname = f'''
                <input name="surname" type="text" style="border: 3px solid red;" value="{surname}">
                <p style="font-size: 9px;">Фамилия должна начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
        kol += 1
    else:
        error_surname = f'<input name="surname" type="text" value="{surname}">'
    if not re.match(name_regex, name):
        error_name = f'''
                <input name="name" type="text" style="border: 3px solid red;" value="{name}">
                <p style="font-size: 9px;">Имя должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
        kol += 1
    else:
        error_name = f'<input name="name" type="text" value="{name}">'
    if not re.match(name_regex, patronymic):
        error_patronymic = f'''
                <input name="patronymic" type="text" style="border: 3px solid red;" value="{patronymic}">
                <p style="font-size: 9px;">Отчество должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
        kol += 1
    else:
        error_patronymic = f'<input name="patronymic" type="text" value="{patronymic}">'
    if not re.match(email_regex, email):
        error_email = f'''
                <input name="email" type="email" style="border: 3px solid red;" value="{email}">
                <p style="font-size: 9px;">Почта должна быть в виде login@email.domain</p>'''
        kol += 1
    else:
        error_email = f'<input name="email" type="email" value="{email}">'
    if not re.match(password_regex, password):
        error_password = f'''
                <input id="passwordInput" name="password" type="password" style="border: 3px solid red;" value="{password}">
                <p style="font-size: 9px;">Пароль должен содержать заглавные и строчные латинские буквы, специальные символы и быть не менее 8 символов </p>'''
        kol += 1
    else:
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'

    if kol == 0:
        if search_email(email):
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            user = Users(
                type="Default_User",
                surname=surname,
                name=name,
                patronymic=patronymic,
                email=email,
                password=md5.hexdigest()
            )
            user.save()
            request.session["user_email"] = email
            messages.success(request, "Вы успешно зарегистрировались!")
            data = {"error_surname": error_surname, "error_name": error_name,
                    "error_patronymic": error_patronymic, "error_email": error_email,
                    "error_password": error_password}
            return render(request, "sign_up/redirect_s.html", context=data)
        else:
            messages.error(request, "Пользователь с такой почтой уже существует!")
            data = {"error_surname": error_surname, "error_name": error_name,
                    "error_patronymic": error_patronymic, "error_email": error_email,
                    "error_password": error_password}
            return render(request, "sign_up/sign_up_sending.html", context=data)

    data = {"error_surname": error_surname, "error_name": error_name,
            "error_patronymic": error_patronymic, "error_email": error_email,
            "error_password": error_password}
    return render(request, "sign_up/sign_up_sending.html", context=data)


def log_in(request):
    return render(request, "log_in/log_in.html")


def log_in_sending(request):
    email = request.POST.get("email", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    error_email, error_password = '', ''

    error_email = f'<input name="email" type="email" value="{email}">'
    error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if checking_for_availability(email, md5.hexdigest()):
        request.session["user_email"] = email
        messages.success(request, "Вы успешно авторизовались!")
        data = {"error_email": error_email, "error_password": error_password}
        return render(request, "log_in/redirect_l.html", context=data)
    else:
        messages.error(request, "Вы ввели неверную почту/пароль!")
        data = {"error_email": error_email, "error_password": error_password}
        return render(request, "log_in/log_in_sending.html", context=data)


def password_recovery(request):
    return render(request, "password_recovery/password_recovery.html")


def password_recovery_sending(request):
    email = request.POST.get("email", "-undefined-")
    error_email = f'<input name="email" type="email" value="{email}">'
    input_code = request.POST.get("code", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    code = request.session.get('code', ''.join(random.choices("0123456789", k=7)))

    if search_email(email) and input_code == "" and password == "":
        error_code = f'<input name="code" type="text" value="{input_code}">'
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        messages.error(request, "Вы ввели неверную почту!")
        button_code = f'<button type="submit">Отправить код</button>'
        button_submit = f'<button type="button">Поменять пароль</button>'
        data = {"error_email": error_email, "button_code": button_code, "error_code": error_code,
                "error_password": error_password, "button_submit": button_submit}
        return render(request, "password_recovery/password_recovery_sending.html", context=data)
    else:
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{8,}$"
        error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        button_code = f'<button type="button">Отправить код</button>'
        button_submit = f'<button type="submit">Поменять пароль</button>'
        error_code = f'<input name="code" type="text" value="{input_code}">'

        if not search_email(email) and input_code == "" and password == "":
            subject = "Восстановление пароля"
            output_message = f"Ваш код для восстановления пароля: {code}"
            from_email = "anton-ivanov-080203@mail.ru"
            send_mail(subject, output_message, from_email, [email])
            messages.success(request, "Код отправлен на вашу почту!")
            request.session['code'] = code
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "error_password": error_password, "button_submit": button_submit}
            return render(request, "password_recovery/password_recovery_sending.html", context=data)

        kol = 0
        if not re.match(password_regex, password):
            error_password = f'''
                    <input id="passwordInput" name="password" type="password" style="border: 3px solid red;" value="{password}">
                    <p style="font-size: 9px;">Пароль должен содержать заглавные и строчные латинские буквы, специальные символы и быть не менее 8 символов </p>'''
            kol += 1
        else:
            error_password = f'<input id="passwordInput" name="password" type="password" value="{password}">'
        if str(input_code) != str(code):
            error_code = f'<input name="code" type="text" value="{input_code}" style="border: 3px solid red;">'
            kol += 1
        else:
            error_code = f'<input name="code" type="text" value="{input_code}">'

        if kol == 0:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            user = get_user(email)
            user.password = md5.hexdigest()
            user.save()
            request.session["user_email"] = email
            messages.success(request, "Вы успешно сменили пароль!")
            del request.session['code']
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "button_submit": button_submit, "error_password": error_password}
            return render(request, "password_recovery/redirect_p.html", context=data)

        else:
            messages.error(request, "Вы ввели неверный код/пароль!")
            data = {"error_email": error_email, "error_code": error_code, "button_code": button_code,
                    "button_submit": button_submit, "error_password": error_password}
            return render(request, "password_recovery/password_recovery_sending.html", context=data)


def main(request):
    return render(request, "main.html")

