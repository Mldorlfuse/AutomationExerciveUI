import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

from components.locators import header_locators

class HeaderComponent(BasePage):
    def open_login_page(self):
        with allure.step("Открыть страницу регистрации/авторизации используя навигационное меню в header"):
            self.driver.find_element(*header_locators.login_and_signup_nav_button).click()

    def get_user_name(self):
        with allure.step("Получить имя пользователя из навигационного меню в header"):
            self.wait.until_not(
                EC.text_to_be_present_in_element_attribute(
                    header_locators.user_name_locator,
                    '',
                    'empty')
            )
            return self.driver.find_element(*header_locators.user_name_locator).get_attribute('innerText')

    def logout_button_click(self):
        with allure.step('Нажать кнопку Logout'):
            self.driver.find_element(*header_locators.logout_nav_button).click()

    def check_unauthorized(self):
        with allure.step('Проверить отсутствие авторизации'):
            assert self.driver.find_element(*header_locators.login_and_signup_nav_button).is_enabled()

    def delete_button_click(self):
        with allure.step('Нажать кнопку Delete'):
            self.driver.find_element(*header_locators.delete_account_nav_button).click()

    def open_contact_us_page(self):
        with allure.step('Открыть страницу формы обратной связи используя навигационное меню в header'):
            self.driver.find_element(*header_locators.contact_us_nav_button).click()

    def open_products_page(self):
        with allure.step('Открыть страницу продуктов используя навигационное меню в header'):
            self.driver.find_element(*header_locators.products_nav_button).click()

    def open_card_page(self):
        with allure.step('Открыть страницу корзины используя навигационное меню в header'):
            self.driver.find_element(*header_locators.cart_nav_button).click()