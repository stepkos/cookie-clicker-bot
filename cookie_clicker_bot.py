from time import sleep

from selenium.webdriver import Chrome as ChromeDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from config import Config
from logger import Logger


class CookieClickerBot:

    def __init__(self):
        self.driver = ChromeDriver()
        self.driver.get(Config.GAME_URL)
        self.wait = lambda time: sleep(time)
        self.wait(4)
        self.chose_language()
        self.wait(4)
        self.import_save()
        self.main()


    def main(self):
        self.big_cookie = self.driver.find_element(By.ID, 'bigCookie')
        Logger.success('CookieClickerBot is starting!')
        while True:
            for _ in range(Config.CLICKS_BEFORE_PURCHASE // Config.CLICKS_BEFORE_SAVING):
                self.click_cookie(Config.CLICKS_BEFORE_SAVING)
                self.export_save()
            self.click_upgrades()
            self.click_buildings()
    

    def click_cookie(self, times):
        for _ in range(times):
            self.big_cookie.click()
            self.wait(1/60)


    def import_save(self):
        try:
            with open(Config.SAVE_PATH) as file:
                save = file.read()
        except FileNotFoundError:
            Logger.warning("Incorrect save file path or file doesn't exist")
        else:
            if not save:
                Logger.warning('Save file is empty')
            else:
                self.driver.execute_script('Game.ImportSaveCode("{}");'.format(save))
                Logger.success('Save has been imported correctly!')


    def export_save(self):
        self.driver.execute_script('Game.ExportSave();') # open export window
        save = self.driver.find_element(By.ID, 'textareaPrompt').get_attribute('value') # get save code
        self.driver.execute_script('Game.ClosePrompt();') # close export window

        if not save:
            Logger.error('Save variable in game is empty')
        else:
            try:
                with open(Config.SAVE_PATH, 'w') as file:
                    file.write(save)
            except:
                Logger.error("Save to file error")
            else:
                Logger.success('Save has been exported correctly!')


    def click_upgrades(self):
        try:
            self.driver.find_element(By.ID, 'upgrade2').click()
            self.driver.find_element(By.ID, 'upgrade1').click()
            self.driver.find_element(By.ID, 'upgrade0').click()
        except:
            Logger.info('click_upgrades method raise an exception')


    def click_buildings(self):
        try:
            buildings = self.driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
            [[building.click() for _ in range(10)] for building in buildings[::-1]]
        except:
            Logger.info('click_buildings method raise an exception')

    
    def chose_language(self):
        try:
            self.driver.find_element(By.ID, 'langSelect-EN').click()
        except TimeoutError:
            Logger.info('Is no language to chose')



if __name__ == '__main__':
    CookieClickerBot()
