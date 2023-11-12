
import re
from django.shortcuts import render
from django.contrib import messages
from .models import *
import hashlib


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

    email_regex = r"^[^@]+@[^@]+\.[a-zA-Z]{2,5}$"
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{8,}$"

    error_email, error_password = '', ''
    kol = 0

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
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        if checking_for_availability(email, md5.hexdigest()):
            messages.success(request, "Вы успешно авторизовались!")
            data = {"error_email": error_email, "error_password": error_password}
            return render(request, "log_in/redirect_l.html", context=data)
        else:
            messages.error(request, "Вы ввели неверную почту/пароль!")
            data = {"error_email": error_email, "error_password": error_password}
            return render(request, "log_in/log_in_sending.html", context=data)

    data = {"error_email": error_email, "error_password": error_password}
    return render(request, "log_in/log_in_sending.html", context=data)


def main(request):
    return render(request, "main.html")

