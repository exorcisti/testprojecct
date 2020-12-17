
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        #Метод get() возвращает значение по указанному ключу/ browser.get(url)
        self.browser.get(self.url)
