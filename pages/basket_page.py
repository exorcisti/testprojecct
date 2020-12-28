
from .locators import BasePageLocators
from .base_page import BasePage
import pytest


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def go_to_busket_page(self): #добавлеяем товар в корзину
        busket_link = self.browser.find_element(*BasePageLocators.BUSKET_LINK)
        busket_link.click()

    def no_product_in_basket(self):         
        assert self.is_not_element_present(*BasePageLocators.GOODS_LINK)

    def is_text_about_basket_empty(self):         
        empty_busket = self.browser.find_element(*BasePageLocators.TEXT_LINK)
        assert "is empty" in empty_busket.text


def test_guest_cant_see_product_in_basket_opened_from_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"   
    page = BasketPage(browser, link, timeout=10)
    page.open()
    page.go_to_busket_page()
    page.no_product_in_basket()
    page.is_text_about_basket_empty()