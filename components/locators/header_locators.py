from selenium.webdriver.common.by import By

login_and_signup_nav_button = (By.LINK_TEXT, 'Signup / Login')
user_name_locator = (By.XPATH, '//a[contains(text(),"Logged in as")]/b')
logout_nav_button = (By.XPATH, '//a[@href="/logout"]')
delete_account_nav_button = (By.XPATH, '//a[@href="/delete_account"]')
contact_us_nav_button = (By.XPATH, '//a[@href="/contact_us"]')
products_nav_button = (By.XPATH, '//a[@href="/products"]')
cart_nav_button = (By.XPATH, '//a[@href="/view_cart"]')