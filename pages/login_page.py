from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


from pages.locators import login_locators
from utils import random_account_generation
from components.header_components import HeaderComponent


class LoginPage(BasePage):
    name = random_account_generation.get_random_login()
    email = random_account_generation.get_random_email()
    password = random_account_generation.get_random_password()

    def signup_fill_form(self):
        self.driver.find_element(*login_locators.signup_name).send_keys(self.name)
        self.driver.find_element(*login_locators.signup_email).send_keys(self.email)
        self.driver.find_element(*login_locators.signup_button).click()

    def enter_account_information(self):
        (self.driver.find_element(*login_locators.account_info_titles[random_account_generation.get_random_gender()])
         .click())
        self.driver.find_element(*login_locators.account_info_password).send_keys(self.password)
        (Select(self.driver.find_element(*login_locators.account_info_day_of_birth))
         .select_by_value(random_account_generation.get_random_day_of_birth()))
        (Select(self.driver.find_element(*login_locators.account_info_month_of_birth))
         .select_by_value(random_account_generation.get_random_month_of_birth()))
        (Select(self.driver.find_element(*login_locators.account_info_year_of_birth))
         .select_by_value(random_account_generation.get_random_year_of_birth()))
        if random_account_generation.get_random_fill_checkbox_newsletter():
            (self.driver.find_element(*login_locators.account_info_newsletter_checkbox).click())
        if random_account_generation.get_random_fill_checkbox_special_offers():
            (self.driver.find_element(*login_locators.account_info_special_offers_checkbox).click())
        (self.driver.find_element(*login_locators.account_info_first_name)
         .send_keys(random_account_generation.get_random_first_name()))
        (self.driver.find_element(*login_locators.account_info_last_name)
         .send_keys(random_account_generation.get_random_last_name()))
        (self.driver.find_element(*login_locators.account_info_company)
         .send_keys(random_account_generation.get_random_company_name()))
        (self.driver.find_element(*login_locators.account_info_address)
         .send_keys(random_account_generation.get_random_address()))
        (self.driver.find_element(*login_locators.account_info_address2)
         .send_keys(random_account_generation.get_random_address2()))
        (self.driver.find_element(*login_locators.account_info_country)
         .send_keys(random_account_generation.get_random_country_select()))
        (self.driver.find_element(*login_locators.account_info_state).
         send_keys(random_account_generation.get_random_state()))
        (self.driver.find_element(*login_locators.account_info_city)
         .send_keys(random_account_generation.get_random_city()))
        (self.driver.find_element(*login_locators.account_info_zip)
         .send_keys(random_account_generation.get_random_zipcode()))
        (self.driver.find_element(*login_locators.account_info_mobile_number)
         .send_keys(random_account_generation.get_random_mobile_number()))
        self.driver.find_element(*login_locators.account_info_create_account_btn).click()
        self.wait.until(EC.text_to_be_present_in_element(login_locators.account_created_title, 'ACCOUNT CREATED!'))
        assert self.driver.find_element(*login_locators.account_created_title).text == 'ACCOUNT CREATED!'
        self.driver.find_element(*login_locators.account_created_continue_btn).click()

    def check_user_name(self, user_name_in_header):
        assert self.name == user_name_in_header
