from selenium.webdriver.common.by import By

title = (By.XPATH, '//h2')
name_field = (By.CSS_SELECTOR, '[data-qa="name"]')
email_field = (By.CSS_SELECTOR, '[data-qa="email"]')
subject_field = (By.CSS_SELECTOR, '[data-qa="subject"]')
message_field = (By.CSS_SELECTOR, '[data-qa="message"]')
upload_file = (By.NAME, 'upload_file')
submit_btn = (By.CSS_SELECTOR, '[data-qa="submit-button"]')

success_msg = (By.CSS_SELECTOR, '.alert-success')
