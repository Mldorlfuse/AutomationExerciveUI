from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import random

from pages.locators import products_locators

class ProductsPage(BasePage):

    view_product_data = None

    def get_all_products(self):
        with allure.step('Получить список всех продуктов'):
            return self.driver.find_elements(*products_locators.list_products)

    def select_a_random_product_card(self):
        with allure.step('Выбрать случайную карточку продуктов'):
            self.random_element = random.choice(self.get_all_products())

    def go_to_product_card(self):
        with allure.step('Перейти в карточку продукта'):
            self.random_element.find_element(*products_locators.view_product_button).click()

    def wait_title(self):
        with allure.step('Дождаться появления надписи ALL PRODUCTS'):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    products_locators.title, 'ALL PRODUCTS'))

    def verif_product_data(self):
        elements = None
        random_element = None
        product_name = None
        product_price = None
        product_category = None

        self.wait_title()
        self.select_a_random_product_card()
        with allure.step('Получить имя продукта'):
            product_name = self.random_element.find_element(*products_locators.name_product).text
        with allure.step('Получить цену продукта'):
            product_price = self.random_element.find_element(*products_locators.price_product).text
        self.go_to_product_card()
        with allure.step(f'Имя карточки должно быть равно {product_name}'):
            assert self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_name).text == product_name
        with allure.step(f'Цена карточки должно быть равно {product_price}'):
            assert self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_price).text == product_price

    def checking_the_application_of_categories(self):
        categories = None
        random_category = None
        random_category_name = None
        subcategories = None
        random_subcategory = None
        random_subcategory_name = None

        self.wait_title()
        with allure.step('Выбрать случайную категорию'):
            categories = self.driver.find_elements(*products_locators.categories_wrapper)
            random_category = random.choice(categories)
            random_category_name = random_category.find_element(
                *products_locators.category).get_attribute("innerText")
            random_category.find_element(*products_locators.category).click()
        with allure.step('Выбрать случайную подкатегорию'):
            subcategories = random_category.find_elements(*products_locators.subcategories)
            random_subcategory = random.choice(subcategories)
            random_subcategory_name = random_subcategory.get_attribute("innerText")
            random_subcategory.click()
            self.select_a_random_product_card()
            self.go_to_product_card()
        with allure.step('Проверить соответствие категории в карточке продукта выбранным'):
            self.product_category = self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_category).text
            assert self.product_category == (f'Category: {random_category_name.capitalize()} '
                                             f'> {random_subcategory_name.capitalize()}')

    def search_product(self):
        key_word_search = ['men', 'women', 'blue', 'white', 'kid', ]
        key_word_searched = None

        self.wait_title()
        key_word_searched = random.choice(key_word_search)
        with allure.step('Ввести в поиск продукта случайное значение из спика'):
            self.driver.find_element(*products_locators.search).send_keys(key_word_searched)
        with allure.step('Нажать кнопку поиска'):
            self.driver.find_element(*products_locators.search_btn).click()
        with allure.step('Проверить соответствие каждого результата искомому'):
            for element in self.get_all_products():
                assert key_word_searched.casefold() in element.find_element(
                    *products_locators.name_product).text.casefold()

    def brands_check(self):
        brands = None
        random_brand = None
        random_brand_name = None
        random_brand_count = None

        self.wait_title()
        with allure.step('Выбрать случайный бранд из списка'):
            brands = self.driver.find_element(*products_locators.brands_wrapper
                                     ).find_elements(*products_locators.brands_elements)
            random_brand = random.choice(brands)
            random_brand_name = random_brand.find_element(*products_locators.brand_name).text
            random_brand_count = random_brand.find_element(*products_locators.brand_count).text
        with allure.step(f'Нажать на выбранный случайный бренд {random_brand_name}'):
            random_brand.click()
        with allure.step(
                f'Проверить равно ли количество найденных результатов указанному рядом с выбранным брендом - {random_brand_count.strip("()")}'):
            assert len(self.get_all_products()) == int(random_brand_count.strip("()"))
        self.select_a_random_product_card()
        self.go_to_product_card()
        with allure.step(
                f'Проверить соответствует ли выбранный бренд {random_brand_name} бренду в карточке продукта'):
            assert self.driver.find_element(*products_locators.view_product_brand
                                            ).text.casefold().strip('brand: ') in random_brand_name.casefold()

    def add_to_cart_from_product_view(self, count):
        self.wait_title()
        self.select_a_random_product_card()
        self.go_to_product_card()
        with allure.step(f'Ввести количество - {count} продуктов'):
            self.driver.find_element(*products_locators.view_product_quantity).clear()
            self.driver.find_element(*products_locators.view_product_quantity).send_keys(count)
        with allure.step('Получить данные из карточки продукта'):
            self.view_product_data = {
                'name': self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_name).text,
                'price': self.driver.find_element(*products_locators.view_product_wrapper).find_element(
                *products_locators.view_product_price).text
            }
        with allure.step('Нажать кнопку добавить в корзину'):
            self.driver.find_element(*products_locators.add_to_cart).click()

    def check_added_modal_info_and_confirm(self):
        with allure.step('Дождаться появления модального окна с заголовком "Added!"'):
            self.wait.until(
                lambda driver: "Added!" in driver.find_element(
                    *products_locators.cart_modal_wrapper
                ).find_element(
                    *products_locators.cart_modal_title
                ).text
            )
        with allure.step('Нажать кнопку continue'):
            self.driver.find_element(*products_locators.cart_modal_wrapper).find_element(
                *products_locators.cart_modal_continue_btn).click()