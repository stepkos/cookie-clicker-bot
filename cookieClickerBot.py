from selenium import webdriver
from settings import Settings
import time

class CookieClickerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(Settings.PATH)
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.driver.implicitly_wait(5)

        self.cookie = self.driver.find_element_by_id('bigCookie')
        self.cookie_counter = self.driver.find_element_by_id('cookies')
        self.buildings = [self.driver.find_elements_by_id('productPrice' + str(i))[0] for i in range(17, -1, -1)]


        time.sleep(20)

        [print(i.text) for i in self.buildings]




if __name__ == '__main__':
    bot = CookieClickerBot()
