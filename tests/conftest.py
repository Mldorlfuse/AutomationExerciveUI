import pytest

@pytest.fixture
def open_login_page(login_page, header_component):
    login_page.open_home_page()
    header_component.open_login_page()

@pytest.fixture
def open_contact_page(contact_us_page, header_component):
    contact_us_page.open_home_page()
    header_component.open_contact_us_page()

@pytest.fixture
def open_products_page(products_page, header_component):
    products_page.open_home_page()
    header_component.open_products_page()