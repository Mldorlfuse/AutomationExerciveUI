import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

from components.locators import dialog_locators

class DialogComponent(BasePage):
    def confirm_button_click(self):
        with allure.step("Нажать кнопку Соглашаюсь в модальном окне согласия с использованием данных"):
            self.driver.find_element(*dialog_locators.dialog_wrapper).find_element(*dialog_locators.confirm_button).click()