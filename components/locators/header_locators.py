from selenium.webdriver.common.by import By

login_and_signup_nav_button = (By.LINK_TEXT, 'Signup / Login')
user_name_locator = (By.XPATH, '//a[contains(text(),"Logged in as")]/b')
logout_nav_button = (By.XPATH, '//a[@href="/logout"]')
delete_account_nav_button = (By.XPATH, '//a[@href="/delete_account"]')