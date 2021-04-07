from selenium.webdriver import Chrome
from time import sleep
from datetime import datetime
from json import load as json_load


class CookieClickerBot:
    def __init__(self):
        self.loadConfig()
        self.driver = Chrome(self.config['DRIVER_PATH'])
        self.driver.get(self.config['URL'])
        sleep(5)

        self.clickCookie = lambda times: [self.driver.find_element_by_id('bigCookie').click() for _ in range(times)]
        self.importSave()
        self.main()


    def loadConfig(self):
        try:
            with open('config.json') as f:
                self.config = json_load(f)
        except FileNotFoundError:
            self.message("FATAL ERROR! - config.json not found")
            raise FileNotFoundError


    @staticmethod
    def getTime():
        now = datetime.now()
        return '{}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second)


    @staticmethod
    def message(content):
        print(CookieClickerBot.getTime() + ' - ' + content)


    def importSave(self):
        try:
            with open(self.config['SAVE_PATH']) as f:
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
                with open(self.config['SAVE_PATH'], 'w') as f:
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
            [[building.click() for _ in range(10)] for building in buildings[::-1]]
        except:
            CookieClickerBot.message('clickBuildings method raise an exception')


    def main(self):
        CookieClickerBot.message('CookieClickerBot is starting!')
        while True:
            self.clickCookie(self.config['clickBeforeBuy'])
            self.clickUpgrades()
            self.clickBuildings()
            self.exportSave()



if __name__ == '__main__':
    CookieClickerBot()
