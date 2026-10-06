import random
import string


def generate_unique_email():
    """Генерирует уникальный email в формате имя_фамилия_когорта_цифры@домен."""
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    surname = ''.join(random.choices(string.ascii_lowercase, k=7))
    cohort = random.randint(1000, 9999)
    digits = random.randint(100, 999)
    domain = random.choice(['yandex.ru', 'mail.ru', 'gmail.com'])
    return f"{name}_{surname}_{cohort}_{digits}@{domain}"


def generate_password(length=8):
    """Генерирует пароль заданной длины (по умолчанию 8 символов)."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def generate_name():
    """Генерирует случайное имя."""
    return ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()