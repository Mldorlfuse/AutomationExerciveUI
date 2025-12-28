from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import allure

from pages.locators import login_locators

class LoginPage(BasePage):

    correct_user_data = {
        'correct_email': '2019-10-071978-02-17ericafranklin@example.net',
        'correct_password': '!746(7Nozr',
        'correct_username': 'casey12'
    }

    def signup_fill_form(self, user_data=None):
        with allure.step('Заполнить формы регистрации'):
            if user_data is None:
                user_data = {
                    'username': self.correct_user_data['correct_username'],
                    'email': self.correct_user_data['correct_email']
                }

            with allure.step(f'Заполнить поле name значением {user_data["username"]}'):
                self.driver.find_element(*login_locators.signup_name).send_keys(user_data["username"])
            with allure.step(f'Заполнить поле email значением {user_data["email"]}'):
                self.driver.find_element(*login_locators.signup_email).send_keys(user_data["email"])
            with allure.step('Нажать кнопку Signup'):
                self.driver.find_element(*login_locators.signup_button).click()

    def enter_account_information(self, user_data):
        with allure.step('Заполнить формы информации об аккаунте'):
            with allure.step('Заполнить поле гендер выбрав случайный вариант'):
                (self.driver.find_element(*login_locators.account_info_titles[user_data["type_of_gender"]])
                 .click())
            with allure.step(f'Заполнить поле пароль значением {user_data["password"]}'):
                self.driver.find_element(*login_locators.account_info_password).send_keys(user_data["password"])
            with allure.step(f'Заполнить поле день рождения значением {user_data["day_of_birth"]}'):
                (Select(self.driver.find_element(*login_locators.account_info_day_of_birth))
                 .select_by_value(user_data["day_of_birth"]))
            with allure.step(f'Заполнить поле месяц рождения значением {user_data["month_of_birth"]}'):
                (Select(self.driver.find_element(*login_locators.account_info_month_of_birth))
                 .select_by_value(user_data["month_of_birth"]))
            with allure.step(f'Заполнить поле год рождения значением {user_data["year_of_birth"]}'):
                (Select(self.driver.find_element(*login_locators.account_info_year_of_birth))
                 .select_by_value(user_data["year_of_birth"]))
            with allure.step('Поставить или нет чекбокс получения рассылки'):
                if user_data["checkbox_newsletter"]:
                    (self.driver.find_element(*login_locators.account_info_newsletter_checkbox).click())
            with allure.step('Поставить или нет чекбокс получения специальных предложений от партнеров'):
                if user_data["checkbox_special_offers"]:
                    (self.driver.find_element(*login_locators.account_info_special_offers_checkbox).click())
            with allure.step(f'Заполнить поле имя значением {user_data["first_name"]}'):
                (self.driver.find_element(*login_locators.account_info_first_name)
                 .send_keys(user_data["first_name"]))
            with allure.step(f'Заполнить поле фамилия значением {user_data["last_name"]}'):
                (self.driver.find_element(*login_locators.account_info_last_name)
                 .send_keys(user_data["last_name"]))
            with allure.step(f'Заполнить поле компания значением {user_data["company"]}'):
                (self.driver.find_element(*login_locators.account_info_company)
                 .send_keys(user_data["company"]))
            with allure.step(f'Заполнить поле адрес значением {user_data["address"]}'):
                (self.driver.find_element(*login_locators.account_info_address)
                 .send_keys(user_data["address"]))
            with allure.step(f'Заполнить поле дополнительный адрес значением {user_data["reserve_address"]}'):
                (self.driver.find_element(*login_locators.account_info_address2)
                 .send_keys(user_data["reserve_address"]))
            with allure.step(f'Выбрать значение {user_data["country"]} в списке стран'):
                (self.driver.find_element(*login_locators.account_info_country)
                 .send_keys(user_data["country"]))
            with allure.step(f'Заполнить поле штат значением {user_data["state"]}'):
                (self.driver.find_element(*login_locators.account_info_state).
                 send_keys(user_data["state"]))
            with allure.step(f'Заполнить поле город значением {user_data["city"]}'):
                (self.driver.find_element(*login_locators.account_info_city)
                 .send_keys(user_data["city"]))
            with allure.step(f'Заполнить поле зипкод значением {user_data["zipcode"]}'):
                (self.driver.find_element(*login_locators.account_info_zip)
                 .send_keys(user_data["zipcode"]))
            with allure.step(f'Заполнить поле номер телефона значением {user_data["phone_number"]}'):
                (self.driver.find_element(*login_locators.account_info_mobile_number)
                 .send_keys(user_data["phone_number"]))
            with allure.step('Нажать кнопку Create Account'):
                self.driver.find_element(*login_locators.account_info_create_account_btn).click()
            with allure.step('Дождаться появления подтверждающего сообщения об успешной регистрации'):
                self.wait.until(EC.text_to_be_present_in_element(login_locators.account_created_title, 'ACCOUNT CREATED!'))
            with allure.step('Текст подтверждающей надписи должен быть "ACCOUNT CREATED!"'):
                assert self.driver.find_element(*login_locators.account_created_title).text == 'ACCOUNT CREATED!'
            with allure.step('Нажать кнопку Continue'):
                self.driver.find_element(*login_locators.account_continue_btn).click()

    @staticmethod
    def check_user_name(user_name, user_name_in_header):
        with allure.step(f'Имя пользователя в навигационном меню header равен {user_name}'):
            assert user_name == user_name_in_header

    def fill_login_email(self, email):
        with (allure.step(f'Заполнить поле email значением {email}')):
            self.driver.find_element(*login_locators.login_email).send_keys(email)

    def fill_login_password(self, password):
        with (allure.step(f'Заполнить поле password значением {password}')):
            self.driver.find_element(*login_locators.login_password).send_keys(password)

    def click_login_btn(self):
        with allure.step('Нажать кнопку Login'):
            self.driver.find_element(*login_locators.login_btn).click()

    def check_error_msg(self):
        with allure.step('Появился текст ошибки "Your email or password is incorrect!"'):
            assert self.driver.find_element(*login_locators.login_error_msg
                                            ).text == 'Your email or password is incorrect!'

    def login_with_incorrect_data(self, incorrect_email, incorrect_password):
        with allure.step('Авторизация с несуществующими данными'):
            self.fill_login_email(incorrect_email)
            self.fill_login_password(incorrect_password)
            self.click_login_btn()
            self.check_error_msg()

    def login_with_correct_data(self, user_data=None):
        with allure.step('Авторизация с существующими данными'):
            if user_data is None:
                user_data = self.correct_user_data
            self.fill_login_email(user_data['correct_email'])
            self.fill_login_password(user_data['correct_password'])
            self.click_login_btn()

    def delete_account(self):
        with allure.step('Дождаться появления подтверждающего сообщения об успешном удалении аккаунта'):
            self.wait.until(EC.text_to_be_present_in_element(login_locators.account_delete_title, 'ACCOUNT DELETED!'))
        with allure.step('Текст подтверждающей надписи должен быть "ACCOUNT DELETED!"'):
            assert self.driver.find_element(*login_locators.account_delete_title).text == 'ACCOUNT DELETED!'
        with allure.step('Нажать кнопку Continue'):
            self.driver.find_element(*login_locators.account_continue_btn).click()

    def check_email_already_exist_message(self):
        with allure.step('Появился текст ошибки "Email Address already exist!"'):
            assert self.driver.find_element(*login_locators.email_already_exist_msg
                                            ).text == 'Email Address already exist!'