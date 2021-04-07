from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime

DRIVER_PATH = r"C:\Program Files (x86)\chromedriver.exe"
SAVE_PATH = r""
URL = r"https://orteil.dashnet.org/cookieclicker/"

class CookieClickerBot:
    def __init__(self):
        # options = Options()
        # options.page_load_strategy = 'eager'
        # self.driver = Chrome(DRIVER_PATH, options=options)
        self.driver = Chrome(DRIVER_PATH)
        self.driver.get(URL)
        sleep(5)

        self.clickCookie = lambda times: [self.driver.find_element_by_id('bigCookie').click() for i in range(times)]

        input('Press enter to start ')
        self.main()

    def importSave(self):
        pass

    def exportSave(self):
        pass

    def clickUpgrades(self):
        try:
            self.driver.find_element_by_id('upgrade2').click()
            self.driver.find_element_by_id('upgrade1').click()
            self.driver.find_element_by_id('upgrade0').click()
        except:
            now = datetime.now()
            print('clickUpgrades exception - {}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second))

    def clickBuildings(self):
        try:
            buildings = self.driver.find_elements_by_css_selector('.product.unlocked.enabled')
            [[building.click() for i in range(10)] for building in buildings[::-1]]
        except:
            now = datetime.now()
            print('clickBuildings exception - {}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second))

    def main(self):
        while True:
            self.clickCookie(300)
            self.clickUpgrades()
            self.clickBuildings()


if __name__ == '__main__':
    bot = CookieClickerBot()
