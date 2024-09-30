#Ejemplo de uso de las funciones creadas (Funciones.py) de la Seccion 20: Page Object Models
import unittest

from selenium import webdriver
from Funciones import Funciones_Globales

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_Xpath(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath("//input[@id='user-name']", "Ferchu_Xpath", 2)
        f.Texto_Xpath("//input[@id='password']", "123456", 2)
        f.Click_Xpath("//input[@id='login-button']", 2)
    
    def test_ID(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_ID("user-name", "Ferchu_ID", 2)
        f.Texto_ID("password", "123456", 2)
        f.Click_ID("login-button", 2)
    
    def test_Xpath_Mejorado(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath_Mejorado("//input[@id='user-name']", "Ferchu_Xpath_Mejorado", 2)
        f.Texto_Xpath_Mejorado("//input[@id='password']", "123456", 2)
        f.Click_Xpath("//input[@id='login-button']", 2)
    
    def test_Xpath_Mejorado_2(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath_Mejorado("//input[@id='user-name']", "Ferchu_Xpath_Mejorado_2", 2)
        f.Texto_Xpath_Mejorado("//input[@id='password']", "123456", 2)
        f.Click_Xpath("//input[@id='login-button']", 2)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()