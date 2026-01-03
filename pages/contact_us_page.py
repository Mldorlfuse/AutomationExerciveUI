from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import allure
import os

from pages.locators import contact_us_locators

class ContactUsPage(BasePage):

    file_name = 'cat.jpeg'

    base_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(base_dir)
    img_dir = os.path.join(project_dir, 'src/image/', file_name)

    def fill_contact_us_form(self, random_data):
        with allure.step('Заполнить форму обратной связи'):
            with allure.step('Дождаться появления надписи CONTACT US'):
                self.wait.until(
                    EC.text_to_be_present_in_element(
                        contact_us_locators.title, 'CONTACT US'))
            with allure.step(f'Заполнить поле name значением {random_data["name"]}'):
                self.driver.find_element(*contact_us_locators.name_field).send_keys(random_data['name'])
            with allure.step(f'Заполнить поле email значением {random_data["email"]}'):
                self.driver.find_element(*contact_us_locators.email_field).send_keys(random_data['email'])
            with allure.step(f'Заполнить поле subject значением {random_data["subject"]}'):
                self.driver.find_element(*contact_us_locators.subject_field).send_keys(random_data['subject'])
            with allure.step(f'Заполнить поле message значением {random_data["message"]}'):
                self.driver.find_element(*contact_us_locators.message_field).send_keys(random_data['message'])
            with allure.step(f'Загрузить файл {self.file_name} в поле загрузки файла'):
                self.driver.find_element(*contact_us_locators.upload_file).send_keys(self.img_dir)
            with allure.step('Нажать кнопку Submit'):
                self.driver.find_element(*contact_us_locators.submit_btn).click()
            with allure.step('Нажать кнопку ok в появившемся окне'):
                alert = Alert(self.driver)
                alert.accept()
            with allure.step('Дождаться появления подтверждающего сообщения об успешной отправке формы обратной связи'):
                self.wait.until(
                    EC.text_to_be_present_in_element(contact_us_locators.success_msg, 'Success! Your details have been submitted successfully.'))
            with allure.step('Текст подтверждающей надписи должен быть "Success! Your details have been submitted successfully."'):
                assert self.driver.find_element(*contact_us_locators.success_msg).text == 'Success! Your details have been submitted successfully.'