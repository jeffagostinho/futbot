from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:

    def get(self):
        options = Options()
        options.add_argument('--start-maximized')

        driver = webdriver.Chrome(options=options)

        return driver

