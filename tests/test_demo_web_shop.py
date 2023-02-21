import allure
from selene import have, be
from selene.support.shared import browser
from config import settings


def test_login_with_api(browser_login):
    browser.open('/')

    with allure.step('Verify successful login'):
        browser.element('a.account').should(have.text(settings.email))


def test_successful_search(browser_login):
    browser.open('/')

    with allure.step('Successful search'):
        browser.element('input.search-box-text').type('$25 Virtual Gift Card')
        browser.element('h2.product-title > a').should(have.text('$25 Virtual Gift Card'))


def test_add_product_to_shopping_cart(browser_login):
    browser.open('/')

    with allure.step('Add product to the shopping cart'):
        browser.element('input.product-box-add-to-cart-button').click()

        browser.element('input.recipient-name').type('Maks')
        browser.element('input.recipient-email').type(settings.email)
        browser.element('input#add-to-cart-button-2').click()

        browser.element('li#topcartlink > a').click()
        browser.driver.refresh()

        browser.element('a.product-name').should(be.visible)


def test_open_account(browser_login):
    browser.open('/')

    with allure.step('Open account page'):
        browser.element('a.account').click()
        browser.element('div.page-title > h1').should(have.text('My account - Customer info'))


def test_open_product_details(browser_login):
    browser.open('/')

    with allure.step('Open product details'):
        browser.element('input.product-box-add-to-cart-button').click()
        browser.element('div.product-name').should(be.visible)
