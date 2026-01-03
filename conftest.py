import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

from components.header_components import HeaderComponent
from pages.login_page import LoginPage
from pages.contact_us_page import ContactUsPage
from pages.products_page import ProductsPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def random_user_data():
    fake = Faker()

    return {
        'username': fake.user_name(),
        'email': f'{fake.date()}{fake.date()}{fake.email()}',
        'password': fake.password(),
        'type_of_gender': fake.random_int(0, 1),
        'day_of_birth': f'{fake.random_int(1, 31)}',
        'month_of_birth': f'{fake.random_int(1, 12)}',
        'year_of_birth': f'{fake.random_int(1900, 2021)}',
        'checkbox_newsletter': fake.boolean(),
        'checkbox_special_offers': fake.boolean(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'company': fake.company(),
        'address': fake.address(),
        'reserve_address': fake.address(),
        'country': fake.random_element(
            ['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']),
        'state': fake.state(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'phone_number': fake.phone_number(),
    }

@pytest.fixture()
def random_wrong_user_data():

    fake = Faker()

    return {
        'error_email': f'{fake.user_name()}{fake.date()}{fake.email()}',
        'error_password': fake.password(),
    }

@pytest.fixture()
def random_contact_us_data():

    fake = Faker()

    return {
        'name': fake.name(),
        'email': fake.email(),
        'subject': fake.sentence(nb_words=4),
        'message': fake.text(max_nb_chars=200)
    }

@pytest.fixture()
def header_component(driver):
    return HeaderComponent(driver)

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def contact_us_page(driver):
    return ContactUsPage(driver)

@pytest.fixture()
def products_page(driver):
    return ProductsPage(driver)