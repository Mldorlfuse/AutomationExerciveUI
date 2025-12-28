from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

from components.locators import header_locators

class HeaderComponent(BasePage):
    def open_login_page(self):
        self.driver.find_element(*header_locators.login_and_signup_nav_button).click()

    def get_user_name(self):
        self.wait.until_not(EC.text_to_be_present_in_element_attribute(header_locators.user_name_locator, '', 'empty'))
        return self.driver.find_element(*header_locators.user_name_locator).get_attribute('innerText')
