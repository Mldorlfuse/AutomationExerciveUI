from selenium.webdriver.common.by import By

signup_name = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
signup_email = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
signup_button = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
signup_form = (By.CSS_SELECTOR, '#form')

account_info_titles = [(By.CSS_SELECTOR, '[id="uniform-id_gender1"]'),(By.CSS_SELECTOR, '[id="uniform-id_gender2"]')]
account_info_password = (By.CSS_SELECTOR, '[data-qa="password"]')
account_info_day_of_birth = (By.CSS_SELECTOR, '[data-qa="days"]')
account_info_month_of_birth = (By.CSS_SELECTOR, '[data-qa="months"]')
account_info_year_of_birth = (By.CSS_SELECTOR, '[data-qa="years"]')
account_info_newsletter_checkbox = (By.NAME, 'newsletter')
account_info_special_offers_checkbox = (By.NAME, 'optin')
account_info_first_name = (By.CSS_SELECTOR, '[data-qa="first_name"]')
account_info_last_name = (By.CSS_SELECTOR, '[data-qa="last_name"]')
account_info_company = (By.CSS_SELECTOR, '[data-qa="company"]')
account_info_address = (By.CSS_SELECTOR, '[data-qa="address"]')
account_info_address2 = (By.CSS_SELECTOR, '[data-qa="address2"]')
account_info_country = (By.CSS_SELECTOR, '[data-qa="country"]')
account_info_state = (By.CSS_SELECTOR, '[data-qa="state"]')
account_info_city = (By.CSS_SELECTOR, '[data-qa="city"]')
account_info_zip = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
account_info_mobile_number = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')
account_info_create_account_btn = (By.CSS_SELECTOR, '[data-qa="create-account"]')

account_created_title = (By.CSS_SELECTOR, '[data-qa="account-created"]')
account_continue_btn = (By.CSS_SELECTOR, '[data-qa="continue-button"]')

login_email = (By.CSS_SELECTOR, '[data-qa="login-email"]')
login_password = (By.CSS_SELECTOR, '[data-qa="login-password"]')
login_btn = (By.CSS_SELECTOR, '[data-qa="login-button"]')
login_error_msg = (By.XPATH, '//form[@action="/login"]/p')

account_delete_title = (By.CSS_SELECTOR, '[data-qa="account-deleted"]')

email_already_exist_msg = (By.XPATH, '//form[@action="/signup"]/p')