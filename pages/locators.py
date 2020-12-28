from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUSKET_LINK = (By.CSS_SELECTOR, "body > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    GOODS_LINK = (By.CSS_SELECTOR, "#basket_formset")
    TEXT_LINK = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.register_form")

    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():

    ADD_BUSKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button") 
    NAME_FACT_LINK = (By.CSS_SELECTOR, "div.alertinner > strong")

    NAME_LINK = (By.CSS_SELECTOR,"#content_inner > article > div:nth-child(1) > div.col-sm-6.product_main > h1")        
    
    PRICE_FACT_LINK = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    PRICE_LINK = (By.CSS_SELECTOR,"#content_inner > article > div:nth-child(1) > div.col-sm-6.product_main > p.price_color")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

    BUSKET_LINK = (By.CSS_SELECTOR, "body > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    GOODS_LINK = (By.CSS_SELECTOR, "#basket_formset")
    TEXT_LINK = (By.CSS_SELECTOR, "#content_inner > p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_LINK = (By.CSS_SELECTOR, "body > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    GOODS_LINK = (By.CSS_SELECTOR, "#basket_formset")
    TEXT_LINK = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


