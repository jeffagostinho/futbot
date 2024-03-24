from src.Driver import Driver
from src.Futwiz import Futwiz

driver = Driver().get()

source = Futwiz(driver)
source.extract()