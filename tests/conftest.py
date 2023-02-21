import pytest
import requests
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.base_session import BaseSession

from config import settings


@pytest.fixture(scope='session')
def demoshop():
    demoshop_session = BaseSession(settings.demo_web_shop_base_url)
    return demoshop_session


@pytest.fixture
def browser_login(demoshop):
    browser.config.timeout = 5.0
    browser.config.base_url = settings.demo_web_shop_base_url
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.driver.maximize_window()

    payload = {
        'Email': settings.email,
        'Password': settings.password
    }

    auth_response = demoshop.post('/login', data=payload, allow_redirects=False)
    auth_cookies = auth_response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open('/Themes/DefaultClean/Content/images/logo.png')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_cookies})

    yield

    browser.quit()
