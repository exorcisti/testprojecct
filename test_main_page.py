from .pages.main_page import MainPage
from .pages.login_page import LoginPage

import pytest


'''
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    
    #Главнаая страница
    page = MainPage(browser, link, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # кликаем на кнопку — переходим на страницу логина

    #Страница авторизации
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
 ''' 

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"   
    page = MainPage(browser, link, timeout=10)
    page.open()
    page.go_to_busket_page()
    page.no_product_in_basket()
    page.is_text_about_basket_empty()

