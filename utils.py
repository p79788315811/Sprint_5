import random
import string

def generate_unique_email(prefix="test", cohort=1999):
    """Генерирует уникальный email по шаблону: имя_фамилия_номер_когорты_3_цифры@yandex.ru"""
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}_{cohort}_{digits}@yandex.ru"

def generate_password(length=8):
    """Генерирует случайный пароль заданной длины"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
def generate_name():
    """Генерирует случайное имя"""
    names = ["Иван", "Мария", "Алексей", "Ольга", "Дмитрий"]
    return random.choice(names)
