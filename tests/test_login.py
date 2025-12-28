from time import sleep
import allure


@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Регистрация нового пользователя")
def test_create_new_account(header_component, login_page, random_user_data):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.signup_fill_form(random_user_data)
    login_page.enter_account_information(random_user_data)
    login_page.check_user_name(random_user_data['username'],header_component.get_user_name())
    sleep(1)
