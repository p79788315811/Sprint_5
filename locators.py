from selenium.webdriver.common.by import By

# === ГЛАВНАЯ СТРАНИЦА ===
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")  # Ссылка «Личный Кабинет» в шапке (ведёт в аккаунт/вход)
LOGO = (By.CSS_SELECTOR, "svg[viewBox*='290']")  # Логотип Stellar Burgers (клик ведёт в конструктор)
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/..")  # Кнопка «Конструктор» в шапке
CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок рабочей области конструктора

# === ФОРМА ВХОДА ===
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # Поле ввода email
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»
REGISTER_LINK_FROM_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться» в форме входа

# === ФОРМА РЕГИСТРАЦИИ ===
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")  # Поле ввода имени
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # Поле ввода email в регистрации
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # Поле ввода пароля в регистрации
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке пароля (меньше 6 символов)
LOGIN_LINK_FROM_REGISTER = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме регистрации

# === ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ===
FORGOT_PASSWORD_SUBMIT = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка отправки формы восстановления
LOGIN_LINK_FROM_RECOVERY = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме восстановления

# === ЛИЧНЫЙ КАБИНЕТ ===
PERSONAL_CABINET_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # Ссылка «Личный Кабинет» в шапке
PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка «Профиль» в личном кабинете (маркер: мы в кабинете)
EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта

# === КОНСТРУКТОР БУРГЕРОВ ===
BUN_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка «Булки»
SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка «Соусы»
FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка «Начинки»
ACTIVE_BUN_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")  # Активная вкладка «Булки»
ACTIVE_SAUCE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")  # Активная вкладка «Соусы»
ACTIVE_FILLING_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")  # Активная вкладка «Начинки»
BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела «Булки» (видимость = раздел активен)
SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела «Соусы»
INGREDIENTS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела «Начинки»

# === ОБЩИЕ ЭЛЕМЕНТЫ ===
MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")  # Оверлей модального окна (на главной появляется при загрузке и перехватывает клики)
ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Общее сообщение об ошибке ввода
SUCCESS_REGISTRATION = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход» после успешной регистрации (переход к форме входа)