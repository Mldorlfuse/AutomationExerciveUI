from xml.etree.ElementTree import tostring

from faker import Faker

fake = Faker()

def get_random_login():
    return fake.user_name()

def get_random_email():
    return f'{fake.date()}{fake.date()}{fake.email()}'

def get_random_password():
    return fake.password()

def get_random_gender():
    return fake.random_int(0,1)

def get_random_day_of_birth():
    return f'{fake.random_int(1, 31)}'

def get_random_month_of_birth():
    return f'{fake.random_int(1,12)}'

def get_random_year_of_birth():
    return f'{fake.random_int(1900,2021)}'

def get_random_fill_checkbox_newsletter():
    return fake.boolean()

def get_random_fill_checkbox_special_offers():
    return fake.boolean()

def get_random_first_name():
    return fake.first_name()

def get_random_last_name():
    return fake.last_name()

def get_random_company_name():
    return fake.company()

def get_random_address():
    return fake.address()

def get_random_address2():
    return fake.address()

def get_random_country_select():
    return fake.random_element(['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore'])

def get_random_state():
    return fake.state()

def get_random_city():
    return fake.city()

def get_random_zipcode():
    return fake.zipcode()

def get_random_mobile_number():
    return fake.phone_number()