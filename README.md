# Stellar Burgers - 5 спринт автоматизированного тестирования на Python

## Тесты

### `test_user_registration.py`

- **test_successful_registration**: Проверяет успешную регистрацию пользователя с корректным именем, email и паролем.
- **test_registration_with_invalid_password**: Проверяет отображение ошибки при попытке регистрации с некорректным паролем.

### `test_user_login.py`

- **test_login_via_login_button**: Проверяет вход по кнопке "Войти в аккаунт" на главной странице.
- **test_login_via_account_button_in_header**: Проверяет вход через кнопку "Личный кабинет".
- **test_login_via_registration_form**: Проверяет вход через кнопку в форме регистрации.
- **test_login_via_forgot_password_form**: Проверяет вход через кнопку в форме восстановления пароля.

### `test_user_logout.py`

- **test_logout_from_account**: Проверяет функциональность выхода из личного кабинета.

### `test_navigation_to_account.py`

- **test_navigate_to_account_page**: Проверяет переход в личный кабинет по клику на кнопку "Личный кабинет" после входа в систему.

### `test_navigation_to_constructor.py`

- **test_navigation_from_account_to_constructor_via_constructor_button**: Проверяет переход в конструктор по кнопке "Конструктор".
- **test_navigation_from_account_to_constructor_via_logo**: Проверяет переход в конструктор по клику на логотип Stellar Burgers.

### `test_navigation_in_constructor_sections.py`

- **test_navigation_to_sections**: Проверяет переходы между разделами "Булки", "Соусы", "Начинки" в конструкторе.
