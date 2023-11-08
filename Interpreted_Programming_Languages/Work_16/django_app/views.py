
import re
from django.shortcuts import render
from django.http import HttpResponse


def sign_up(request):
    return render(request, "sign_up.html")


def sign_up_sending(request):
    surname = request.POST.get("surname", "-undefined-")
    name = request.POST.get("name", "-undefined-")
    patronymic = request.POST.get("patronymic", "-undefined-")
    email = request.POST.get("email", "-undefined-")
    password = request.POST.get("password", "-undefined-")

    name_regex = r"^([А-ЯЁ][а-яё]+)$"
    email_regex = r"^[^@]+@[^@]+\.[a-zA-Z]{2,5}$"
    password_regex = r"^(?=.*[A-Za-z])(?=.*\d)[a-za-z\d@#$%*+?^_.-]{8,}$"

    error_surname, error_name, error_patronymic, error_email, error_password = '', '', '', '', ''

    if not re.match(name_regex, surname):
        error_surname = f'''
                <input name="surname" type="text" style="border: 3px solid red;" value="{surname}">
                <p style="font-size: 9px;">Фамилия должна начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
    else:
        error_surname = f'<input name="surname" type="text" value="{surname}">'
    if not re.match(name_regex, name):
        error_name = f'''
                <input name="name" type="text" style="border: 3px solid red;" value="{name}">
                <p style="font-size: 9px;">Имя должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
    else:
        error_name = f'<input name="name" type="text" value="{name}">'
    if not re.match(name_regex, patronymic):
        error_patronymic = f'''
                <input name="patronymic" type="text" style="border: 3px solid red;" value="{patronymic}">
                <p style="font-size: 9px;">Отчество должно начинаться с заглавной буквы, после которой идут прописные (Кириллица)</p>'''
    else:
        error_patronymic = f'<input name="patronymic" type="text" value="{patronymic}">'
    if not re.match(email_regex, email):
        error_email = f'''
                <input name="email" type="email" style="border: 3px solid red;" value="{email}">
                <p style="font-size: 9px;">Почта должна быть в виде login@email.domain</p>'''
    else:
        error_email = f'<input name="email" type="email" value="{email}">'
    if not re.match(password_regex, password):
        error_password = f'''
                <input name="password" type="password" style="border: 3px solid red;" value="{password}">
                <p style="font-size: 9px;">Пароль должен содержать заглавные и строчные латинские буквы, специальные символы и быть не менее 8 символов </p>'''
    else:
        error_password = f'<input name="password" type="password" value="{password}">'

    data = {"error_surname": error_surname, "error_name": error_name,
            "error_patronymic": error_patronymic, "error_email": error_email,
            "error_password": error_password}
    return render(request, "sign_up_sending.html", context=data)


def log_in(request):
    return render(request, "log_in.html")
