from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import allure

from pages.locators import cart_locators

class CartPage(BasePage):
    def wait_check_cart(self):
        with allure.step('Дождаться открытия страницы корзины'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    cart_locators.cart_check_info, 'Shopping Cart'))

    def wait_check_checkout(self):
        with allure.step('Дождаться открытия страницы кассы'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    cart_locators.cart_check_info, 'Checkout'))

    def wait_order_title(self):
        with allure.step('Дождаться появления информации об успешном оформлении заказа'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    cart_locators.title, 'ORDER PLACED!'))

    def placing_an_order(self, data, count, card_data):
        self.wait_check_cart()
        with (allure.step('Проверить соответствия имени продукта и цены')):
            assert data['name'] == self.driver.find_element(*cart_locators.cart_wrapper
                                                            ).find_element(*cart_locators.item_name).text
            assert data['price'] == self.driver.find_element(*cart_locators.cart_wrapper
                                                             ).find_element(*cart_locators.item_price).text
            assert int(count) == int(self.driver.find_element(*cart_locators.cart_wrapper
                                                              ).find_element(*cart_locators.item_count).text)
        with allure.step('Нажать кнопку checkout'):
            self.driver.find_element(*cart_locators.check_out_btn).click()
        self.wait_check_checkout()
        with allure.step('Нажать кнопку Place Order'):
            self.driver.find_element(*cart_locators.place_order_btn).click()
        with allure.step(f'Заполнить имя держателя карты значением {card_data["holder"]}'):
            self.driver.find_element(*cart_locators.name_of_card).send_keys(card_data['holder'])
        with allure.step(f'Заполнить номер карты значением {card_data["number"]}'):
            self.driver.find_element(*cart_locators.card_number).send_keys(card_data['number'])
        with allure.step(f'Заполнить cvc карты значением {card_data["cvv"]}'):
            self.driver.find_element(*cart_locators.cvc_code).send_keys(card_data['cvv'])
        with allure.step(f'Заполнить месяц окончания карты значением {card_data["expiry_month"]}'):
            self.driver.find_element(*cart_locators.expiration_month).send_keys(card_data['expiry_month'])
        with allure.step(f'Заполнить год окончания карты значением {card_data["expiry_year"]}'):
            self.driver.find_element(*cart_locators.expiration_year).send_keys(card_data['expiry_year'])
        with allure.step('Нажать кнопку pay and confirm'):
            self.driver.find_element(*cart_locators.submit_btn).click()
        self.wait_order_title()
        with allure.step('Нажать кнопку continue'):
            self.driver.find_element(*cart_locators.continue_btn).click()