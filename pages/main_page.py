
#Главная страница
from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_busket_page(self): #добавлеяем товар в корзину
        busket_link = self.browser.find_element(*MainPageLocators.BUSKET_LINK)
        busket_link.click()

    def no_product_in_basket(self):         
        assert self.is_not_element_present(*MainPageLocators.GOODS_LINK)

    def is_text_about_basket_empty(self):         
        empty_busket = self.browser.find_element(*MainPageLocators.TEXT_LINK)
        assert "is empty" in empty_busket.text


