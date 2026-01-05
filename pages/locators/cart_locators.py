from selenium.webdriver.common.by import By

cart_check_info = (By.XPATH, '//li[@class="active"]')

cart_wrapper = (By.CSS_SELECTOR, '#cart_info_table')
item_name = (By.XPATH, '//td[@class="cart_description"]/h4')
item_count = (By.XPATH, '//td[@class="cart_quantity"]')
item_price = (By.XPATH, '//td[@class="cart_price"]/p')

check_out_btn = (By.CSS_SELECTOR, '.check_out')

place_order_btn = (By.CSS_SELECTOR, '.check_out')

name_of_card = (By.CSS_SELECTOR, '[data-qa="name-on-card"]')
card_number = (By.CSS_SELECTOR, '[data-qa="card-number"]')
cvc_code = (By.CSS_SELECTOR, '[data-qa="cvc"]')
expiration_month = (By.CSS_SELECTOR, '[data-qa="expiry-month"]')
expiration_year = (By.CSS_SELECTOR, '[data-qa="expiry-year"]')

submit_btn = (By.CSS_SELECTOR, '[data-qa="pay-button"]')

title = (By.CSS_SELECTOR, '[data-qa="order-placed"]')
continue_btn = (By.CSS_SELECTOR, '[data-qa="continue-button"]')