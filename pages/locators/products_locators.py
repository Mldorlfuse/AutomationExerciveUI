from selenium.webdriver.common.by import By

title = (By.XPATH, '//div[@class="features_items"]/h2')

list_products = (By.CSS_SELECTOR, '.product-image-wrapper')
product_info_wrapper = (By.CSS_SELECTOR, '.productinfo')
price_product = (By.TAG_NAME, 'h2')
name_product = (By.TAG_NAME, 'p')
view_product_button = (By.LINK_TEXT, 'View Product')

view_product_wrapper = (By.CSS_SELECTOR, '.product-information')
view_product_name = (By.TAG_NAME, 'h2')
view_product_price = (By.XPATH,'//div[@class="product-information"]/span/span')
view_product_category = (By.TAG_NAME, 'p')
view_product_quantity = (By.CSS_SELECTOR, '#quantity')
view_product_brand = (By.XPATH, '//div[@class="product-information"]/p[4]')

add_to_cart = (By.CSS_SELECTOR, '.btn-default')

categories_wrapper = (By.CSS_SELECTOR, '.panel.panel-default')
category = (By.XPATH, './/h4[@class="panel-title"]/a')
subcategories = (By.XPATH, './/div[@class="panel-body"]/ul/li/a')