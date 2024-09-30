import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Page_Loguin():
    def __init__(self, driver):
        self.driver = driver
    
    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t
    
    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def Texto_Xpath(self, xpath, texto, tiempo, boton_Login=None):
        valor=self.driver.find_element(By.XPATH, xpath)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(tiempo)
        return tiempo
  
    def Click_Xpath(self, xpath, tiempo):
        boton=self.driver.find_element(By.XPATH, xpath)
        boton.click()
        t = time.sleep(tiempo)