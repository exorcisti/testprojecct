import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert len(button.text) > 0
    time.sleep(30)

