from selenium.webdriver.common.by import By

# === ГЛАВНАЯ СТРАНИЦА ===
MAIN_PAGE_URL = "https://stellarburgers.education-services.ru"  # Основной URL приложения
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PROFILE_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader') and text()='Личный кабинет']")  # Кнопка «Личный кабинет» в шапке
LOGO = (By.XPATH, "//div[contains(@class, 'Logo')]")  # Логотип Stellar Burgers (клик ведёт в конструктор)
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор» в шапке

# === ФОРМА ВХОДА ===
EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода email
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Забыли пароль?']")  # Ссылка «Забыли пароль?»
REGISTER_LINK_FROM_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться» в форме входа

# === ФОРМА РЕГИСТРАЦИИ ===
REGISTER_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")  # Поле ввода имени
REGISTER_EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Email')]")  # Поле ввода email в регистрации
REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Пароль')]")  # Поле ввода пароля в регистрации
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке пароля (меньше 6 символов)

# === ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ===
FORGOT_PASSWORD_SUBMIT = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка отправки формы восстановления
LOGIN_LINK_FROM_RECOVERY = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме восстановления

# === ЛИЧНЫЙ КАБИНЕТ ===
PERSONAL_CABINET_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader') and text()='Личный кабинет']")  # Ссылка «Личный кабинет»
PROFILE_EDIT_LINK = (By.XPATH, "//button[text()='Редактировать профиль']")  # Кнопка редактирования профиля
EXIT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка выхода из аккаунта

# === КОНСТРУКТОР БУРГЕРОВ ===
BUN_TAB = (By.XPATH, "//div[text()='Булки']")  # Вкладка «Булки»
SAUCE_TAB = (By.XPATH, "//div[text()='Соусы']")  # Вкладка «Соусы»
FILLING_TAB = (By.XPATH, "//div[text()='Начинки']")  # Вкладка «Начинки»
BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела «Булки» (видимость = раздел активен)
SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела «Соусы»
INGREDIENTS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела «Начинки»
INGREDIENT_CARD = (By.XPATH, "//ul[@class='Ingredients']//li")  # Карточка ингредиента (для проверки загрузки списка)

# === ОБЩИЕ ЭЛЕМЕНТЫ ===
MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_overlay')]")  # Фоновый слой модального окна (клик закрывает окно)
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")  # Кнопка закрытия модального окна
ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Общее сообщение об ошибке ввода
SUCCESS_REGISTRATION = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход» после успешной регистрации (переход к форме входа)

# === URL СТРАНИЦ (для проверок навигации) ===
LOGIN_PAGE_URL = MAIN_PAGE_URL + "/login"  # Страница входа
REGISTER_PAGE_URL = MAIN_PAGE_URL + "/register"  # Страница регистрации
RECOVERY_PAGE_URL = MAIN_PAGE_URL + "/forgot-password"  # Страница восстановления пароля
PROFILE_PAGE_URL = MAIN_PAGE_URL + "/account/profile"  # Личный кабинет
