#Cтраница
from .base_page import BasePage
from .locators import ProductPageLocators #достать из локатаора ссылки


class ProductPage(BasePage): #наследник класса BasePage
   
   def should_be_login_url(self):
      assert "?promo=newYear" in self.browser.current_url, "login is absent in current url"   

   def add_to_busket_page(self): #добавлеяем товар в корзину
      busk_link = self.browser.find_element(*ProductPageLocators.ADD_BUSKET_LINK)
      busk_link.click()

#Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.   
   def should_be_same_name(self):        
      #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "absent login form"
      name1= self.browser.find_element(*ProductPageLocators.NAME_LINK)
      name2 = self.browser.find_element(*ProductPageLocators.NAME_FACT_LINK)
      assert name1.text == name2.text


#Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.   
   def should_be_same_price(self):         
      price_booked = self.browser.find_element(*ProductPageLocators.PRICE_LINK)
      price_fact = self.browser.find_element(*ProductPageLocators.PRICE_FACT_LINK)
      assert price_booked.text == price_fact.text


   def should_not_be_success_message(self):
      assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

   def disappeared_after_adding_product_to_basket(self):
      assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

   def go_to_busket_page(self): 
      busket_link = self.browser.find_element(*ProductPageLocators.BUSKET_LINK)
      busket_link.click()

   def no_product_in_basket(self):         
      assert self.is_not_element_present(*ProductPageLocators.GOODS_LINK)

   def is_text_about_basket_empty(self):         
      empty_busket = self.browser.find_element(*ProductPageLocators.TEXT_LINK)
      assert "is empty" in empty_busket.text
