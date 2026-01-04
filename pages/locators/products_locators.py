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
cart_modal_wrapper = (By.CSS_SELECTOR, '#cartModal')
cart_modal_title = (By.TAG_NAME, 'h4')
cart_modal_continue_btn = (By.TAG_NAME, 'button')

categories_wrapper = (By.CSS_SELECTOR, '.panel.panel-default')
category = (By.XPATH, './/h4[@class="panel-title"]/a')
subcategories = (By.XPATH, './/div[@class="panel-body"]/ul/li/a')

search = (By.CSS_SELECTOR, '#search_product')
search_btn = (By.CSS_SELECTOR, '#submit_search')

brands_wrapper = (By.CSS_SELECTOR, '.nav.nav-pills.nav-stacked')
brands_elements = (By.XPATH, './/li')
brand_name = (By.TAG_NAME, 'a')
brand_count = (By.TAG_NAME, 'span')