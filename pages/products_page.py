from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import random

from pages.locators import products_locators

class ProductsPage(BasePage):

    elements = None
    random_element = None
    product_name = None
    product_price = None
    product_category = None

    categories = None
    random_category = None
    random_category_name = None
    subcategories = None
    random_subcategory = None
    random_subcategory_name = None

    def select_a_random_product_card(self):
        with allure.step('Выбрать случайную карточку продуктов'):
            self.elements = self.driver.find_elements(*products_locators.list_products)
            self.random_element = random.choice(self.elements)

    def go_to_product_card(self):
        with allure.step('Перейти в карточку продукта'):
            self.random_element.find_element(*products_locators.view_product_button).click()

    def verif_product_data(self):
        with allure.step('Дождаться появления надписи ALL PRODUCTS'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    products_locators.title, 'ALL PRODUCTS'))
        self.select_a_random_product_card()
        with allure.step('Получить имя продукта'):
            self.product_name = self.random_element.find_element(*products_locators.name_product).text
        with allure.step('Получить цену продукта'):
            self.product_price = self.random_element.find_element(*products_locators.price_product).text
        self.go_to_product_card()
        with allure.step(f'Имя карточки должно быть равно {self.product_name}'):
            assert self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_name).text == self.product_name
        with allure.step(f'Цена карточки должно быть равно {self.product_price}'):
            assert self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_price).text == self.product_price

    def checking_the_application_of_categories(self):
        with allure.step('Дождаться появления надписи ALL PRODUCTS'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    products_locators.title, 'ALL PRODUCTS'))
        with allure.step('Выбрать случайную категорию'):
            self.categories = self.driver.find_elements(*products_locators.categories_wrapper)
            self.random_category = random.choice(self.categories)
            self.random_category_name = self.random_category.find_element(
                *products_locators.category).get_attribute("innerText")
            self.random_category.find_element(*products_locators.category).click()
        with allure.step('Выбрать случайную подкатегорию'):
            self.subcategories = self.random_category.find_elements(*products_locators.subcategories)
            self.random_subcategory = random.choice(self.subcategories)
            self.random_subcategory_name = self.random_subcategory.get_attribute("innerText")
            self.random_subcategory.click()
            self.select_a_random_product_card()
            self.go_to_product_card()
        with allure.step('Проверить соответствие категории в карточке продукта'):
            self.product_category = self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_category).text
            assert self.product_category == (f'Category: {self.random_category_name.capitalize()} '
                                             f'> {self.random_subcategory_name.capitalize()}')
