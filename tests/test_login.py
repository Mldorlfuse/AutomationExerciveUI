from time import sleep
import allure

@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Регистрация нового пользователя и выход из аккаунта")
def test_full_registration_path(header_component, login_page, random_user_data):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.signup_fill_form(random_user_data)
    login_page.enter_account_information(random_user_data)
    login_page.check_user_name(random_user_data['username'],header_component.get_user_name())
    header_component.logout_button_click()
    header_component.check_unauthorized()


@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Авторизация с несуществующими данными")
def test_authorization_using_non_existent_data(header_component, login_page, random_user_data):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.login_with_incorrect_data(random_user_data['error_email'], random_user_data['error_password'])

@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Авторизация с существующими данными из списка тестовых пользователей")
def test_authorization_test_data_and_logout(header_component, login_page):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.login_with_correct_data()
    login_page.check_user_name(login_page.correct_user_data['correct_username'], header_component.get_user_name())

@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Регистрация нового пользователя и удаление аккаунта")
def test_full_registration_path_with_delete(header_component, login_page, random_user_data):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.signup_fill_form(random_user_data)
    login_page.enter_account_information(random_user_data)
    login_page.check_user_name(random_user_data['username'],header_component.get_user_name())
    header_component.delete_button_click()
    login_page.delete_account()
    header_component.open_login_page()
    login_page.login_with_incorrect_data(random_user_data['email'], random_user_data['password'])

@allure.epic("UI")
@allure.feature("Авторизация/регистрация")
@allure.story("Регистрация с существующими данными пользователя")
def test_authorization_with_already_exist_email(header_component, login_page):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.signup_fill_form()
    login_page.check_email_already_exist_message()



