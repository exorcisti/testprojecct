from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('num', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    
    page = ProductPage(browser, link, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    #page.should_be_login_url()
    page.add_to_busket_page() #Добавляем товар в корзину
    page.solve_quiz_and_get_code()
    page.should_be_same_name()
    page.should_be_same_price() 


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=10)
    page.open() #Открываем страницу товара 
    page.go_to_busket_page() 
    page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_guest_cant_see_success_message(browser): 
    link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=10)
    page.open() #Открываем страницу товара 
    page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.go_to_busket_page()
    page.disappeared_after_adding_product_to_basket() #Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"   
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.go_to_busket_page()
    page.no_product_in_basket()
    page.is_text_about_basket_empty()
    

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):

        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "stepik12345"
        page.register_new_user(email, password) #зарегистрировать нового пользователя
        page.should_be_authorized_user() #проверить, что пользователь залогинен.
        time.sleep(2)

    
    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open() #Открываем страницу товара 
        page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present 

    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"       
        
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        time.sleep(2)
        #page.should_be_login_url()
        page.add_to_busket_page() #Добавляем товар в корзину
        page.solve_quiz_and_get_code()
        page.should_be_same_name() 
        page.should_be_same_price()


