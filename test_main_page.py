from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_form()


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    register_form = LoginPage(browser, link)
    register_form.open()
    register_form.should_be_register_form()


def test_should_be_ckeck_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page_link = LoginPage(browser, link)
    page_link.open()
    page_link.should_be_login_url()
