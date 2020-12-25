from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    
    #Главнаая страница
    page = MainPage(browser, link, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # кликаем на кнопку — переходим на страницу логина

    #Страница авторизации
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
  




    
