import allure

@allure.epic("UI")
@allure.feature("Продукты и корзина")
@allure.story("Проверка соответствия полей продукта в списке продуктов и карточке продукта")
def test_verif_product_data(open_products_page, products_page):
    products_page.verif_product_data()

@allure.epic("UI")
@allure.feature("Продукты и корзина")
@allure.story("Проверка соответствия категории в карточке продукта после фильтрования продуктов по этой категории")
def test_applications_of_categories(open_products_page, products_page):
    products_page.checking_the_application_of_categories()

@allure.epic("UI")
@allure.feature("Продукты и корзина")
@allure.story("Поиск продукта по ключевому слову и проверка соответсия результата")
def test_search_products(open_products_page, products_page):
    products_page.search_product()

@allure.epic("UI")
@allure.feature("Продукты и корзина")
@allure.story("Проверка соответствия бренда в карточке продукта после фильтрования продуктов по этому бренду")
def test_applications_of_brands(open_products_page, products_page):
    products_page.brands_check()

@allure.epic("UI")
@allure.feature("Продукты и корзина")
@allure.story("Добавить случайное количество продукта, проверить отображаемое количество в корзине и оформить заказ")
def test_add_products_to_cart(
        login_and_open_products_page,
        products_page,
        random_count_for_view,
        header_component,
        cart_page,
        random_card_data):
    products_page.add_to_cart_from_product_view(random_count_for_view)
    products_page.check_added_modal_info_and_confirm()
    header_component.open_card_page()
    cart_page.placing_an_order(products_page.view_product_data, random_count_for_view, random_card_data)