
#Страница аутентификации и регистрации
from .base_page import BasePage #Где исскать page
from .locators import LoginPageLocators #Где искать локатор
import time

class LoginPage(BasePage):


    def should_be_login_page(self):
        self.should_be_login_url()
        #self.should_be_login_form()
        #self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес (строка ввода браузера)
        assert "/login" in self.browser.current_url, "login is absent in current url"
        #assert "/login" in self.open(), "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина (столбец аутентификации)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "absent login form"
        
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице (столбец регистрации)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "absent registration form"

    def register_new_user(self, email, password):
        #принимает две строки и регистрирует пользователя. 
        #Реализуйте его, описав соответствующие элементы страницы.
        bemail = self.browser.find_element(*LoginPageLocators.EMAIL)
        bemail.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        password2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

