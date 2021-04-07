from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime

DRIVER_PATH = r"C:\Program Files (x86)\chromedriver.exe"
SAVE_PATH = r"save.txt"
URL = r"https://orteil.dashnet.org/cookieclicker/"


class CookieClickerBot:
    def __init__(self):
        self.driver = Chrome(DRIVER_PATH)
        self.driver.get(URL)
        sleep(5)

        self.clickCookie = lambda times: [self.driver.find_element_by_id('bigCookie').click() for i in range(times)]
        self.importSave()

        CookieClickerBot.message('CookieClickerBot is starting!')
        self.main()


    @staticmethod
    def getTime():
        now = datetime.now()
        return '{}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second)


    @staticmethod
    def message(content):
        print(CookieClickerBot.getTime() + ' - ' + content)


    def importSave(self):
        try:
            with open(SAVE_PATH) as f:
                save = f.read()
        except FileNotFoundError:
            CookieClickerBot.message("Incorrect save file path or file doesn't exist")
        else:
            if not save:
                CookieClickerBot.message('Save file (importSave) is empty')
            else:
                self.driver.execute_script('Game.ImportSaveCode("{}");'.format(save))
                CookieClickerBot.message('Save has been imported correctly!')


    def exportSave(self):
        self.driver.execute_script('Game.ExportSave();') # open export window
        save = self.driver.find_element_by_id('textareaPrompt').get_attribute('value') # get save code
        self.driver.execute_script('Game.ClosePrompt();') # close export window

        if not save:
            CookieClickerBot.message('Save variable (exportSave) is empty')
        else:
            try:
                with open(SAVE_PATH, 'w') as f:
                    f.write(save)
            except:
                CookieClickerBot.message("exportSave method raise an exception")
            else:
                CookieClickerBot.message('Save has been exported correctly!')
                

    def clickUpgrades(self):
        try:
            self.driver.find_element_by_id('upgrade2').click()
            self.driver.find_element_by_id('upgrade1').click()
            self.driver.find_element_by_id('upgrade0').click()
        except:
            CookieClickerBot.message('clickUpgrades method raise an exception')


    def clickBuildings(self):
        try:
            buildings = self.driver.find_elements_by_css_selector('.product.unlocked.enabled')
            [[building.click() for i in range(10)] for building in buildings[::-1]]
        except:
            CookieClickerBot.message('clickBuildings method raise an exception')


    def main(self):
        while True:
            for _ in range(3):
                self.clickCookie(300)
                self.clickUpgrades()
                self.clickBuildings()
            self.exportSave()



if __name__ == '__main__':
    bot = CookieClickerBot()
