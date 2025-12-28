from time import sleep

def test_create_new_account(header_component, login_page):
    login_page.open_home_page()
    header_component.open_login_page()
    login_page.signup_fill_form()
    login_page.enter_account_information()
    login_page.check_user_name(header_component.get_user_name())
    sleep(3)
