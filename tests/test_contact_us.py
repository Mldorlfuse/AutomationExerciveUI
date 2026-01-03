import allure

@allure.epic("UI")
@allure.feature("Форма обратной связи")
@allure.story("Отправка формы обратной связи")
def test_contact_us_form_send(open_contact_page, contact_us_page, random_contact_us_data):
    contact_us_page.fill_contact_us_form(random_contact_us_data)