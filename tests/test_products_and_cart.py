import allure

@allure.epic("UI")
@allure.feature("Продукты")
@allure.story("Проверка соответствия полей продукта в списке продуктов и карточке продукта")
def test_verif_product_data(open_products_page, products_page):
    products_page.verif_product_data()

@allure.epic("UI")
@allure.feature("Продукты")
@allure.story("Проверка соответствия категории в карточке продукта после фильтрования продуктов по этой категории")
def test_applications_of_categories(open_products_page, products_page):
    products_page.checking_the_application_of_categories()

@allure.epic("UI")
@allure.feature("Продукты")
@allure.story("Поиск продукта по ключевому слову и проверка соответсия результата")
def test_search_products(open_products_page, products_page):
    products_page.search_product()

@allure.epic("UI")
@allure.feature("Продукты")
@allure.story("Проверка соответствия бренда в карточке продукта после фильтрования продуктов по этому бренду")
def test_applications_of_brands(open_products_page, products_page):
    products_page.brands_check()