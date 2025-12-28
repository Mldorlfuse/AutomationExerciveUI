from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = 'https://automationexercise.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_url}')