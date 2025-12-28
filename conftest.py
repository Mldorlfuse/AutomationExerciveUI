import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from components.header_components import HeaderComponent
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    return chrome_driver

@pytest.fixture()
def header_component(driver):
    return HeaderComponent(driver)

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
