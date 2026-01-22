import pytest

@pytest.fixture
def open_login_page(login_page, dialog_component, header_component):
    login_page.open_home_page()
    dialog_component.confirm_button_click()
    header_component.open_login_page()

@pytest.fixture
def open_contact_page(contact_us_page, dialog_component, header_component):
    contact_us_page.open_home_page()
    dialog_component.confirm_button_click()
    header_component.open_contact_us_page()

@pytest.fixture
def open_products_page(products_page, dialog_component, header_component):
    products_page.open_home_page()
    dialog_component.confirm_button_click()
    header_component.open_products_page()

@pytest.fixture()
def login(login_page, dialog_component, header_component):
    login_page.login_with_correct_data()
    dialog_component.confirm_button_click()
    login_page.check_user_name(login_page.correct_user_data['correct_username'], header_component.get_user_name())