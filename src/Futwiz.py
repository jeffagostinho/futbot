import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.repository.PlayerRepository import PlayerRepository
from time import sleep

class Futwiz:
    URL = 'https://www.futwiz.com'

    def __init__(self, driver):
        self.driver = driver

    def extract(self):
        driver = self.driver

        driver.get(self.URL + '/en/fc24/players?page=0&minprice=18000&maxprice=100000&sort[]=bin-high')

        table = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'player-search-results')))
        links = table.find_elements(By.TAG_NAME, 'a')
        
        for link in links:
        
            sleep(1)

            name = link.find_element(By.CLASS_NAME, 'card-24-pack-name')
            rating = link.find_element(By.CLASS_NAME, 'card-24-pack-rating')
            position = link.find_element(By.CLASS_NAME, 'card-24-pack-position')

            player = {
                "source": 'futwiz',
                "name": name.text,
                "rating": rating.text,
                "position": position.text,
            }

            link.click()

            sleep(1)

            playerGuide = driver.window_handles[-1]
            driver.switch_to.window(playerGuide)

            sleep(1)
            
            playerPrice = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='player-prices']/div[1]")))
            
            currentPrice = playerPrice.find_element(By.CLASS_NAME, 'price-num')
            minPrice = playerPrice.find_element(By.XPATH, "//div[@class='extra-prices']/div[1]")
            averagePrice = playerPrice.find_element(By.XPATH, "//div[@class='extra-prices']/div[2]")
            maxPrice = playerPrice.find_element(By.XPATH, "//div[@class='extra-prices']/div[3]")
            latestPriceUpdate = playerPrice.find_element(By.CLASS_NAME, 'price-updated')

            prices = {
                'current_price': currentPrice.text,
                'min_price': minPrice.text,
                'average_price': averagePrice.text,
                'max_price': maxPrice.text,
                'latest_price_update': latestPriceUpdate.text,
            }

            player.update(prices)

            print(player)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            sleep(1)
        
        driver.quit()

