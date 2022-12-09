from time import sleep
from datetime import datetime
from json import load as json_load

from selenium.webdriver import Chrome as ChromeDriver
from selenium.webdriver.common.by import By

from config import Config


class CookieClickerBot:

    def __init__(self):
        self.driver = ChromeDriver()
        self.driver.get(Config.GAME_URL)
        sleep(10)

        self.clickCookie = lambda times: [self.driver.find_element(By.ID, 'bigCookie').click() for _ in range(times)]
        self.importSave()
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
            with open(Config.SAVE_PATH) as f:
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
        save = self.driver.find_element(By.ID, 'textareaPrompt').get_attribute('value') # get save code
        self.driver.execute_script('Game.ClosePrompt();') # close export window

        if not save:
            CookieClickerBot.message('Save variable (exportSave) is empty')
        else:
            try:
                with open(Config.SAVE_PATH, 'w') as f:
                    f.write(save)
            except:
                CookieClickerBot.message("exportSave method raise an exception")
            else:
                CookieClickerBot.message('Save has been exported correctly!')


    def clickUpgrades(self):
        try:
            self.driver.find_element(By.ID, 'upgrade2').click()
            self.driver.find_element(By.ID, 'upgrade1').click()
            self.driver.find_element(By.ID, 'upgrade0').click()
        except:
            CookieClickerBot.message('clickUpgrades method raise an exception')


    def clickBuildings(self):
        try:
            buildings = self.driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
            [[building.click() for _ in range(10)] for building in buildings[::-1]]
        except:
            CookieClickerBot.message('clickBuildings method raise an exception')


    def main(self):
        CookieClickerBot.message('CookieClickerBot is starting!')
        while True:
            for _ in range(Config.SERIES_BEFORE_BUY):
                self.clickCookie(Config.CLICK_BEFORE_SAVE)
                self.exportSave()
            self.clickUpgrades()
            self.clickBuildings()



if __name__ == '__main__':
    CookieClickerBot()
