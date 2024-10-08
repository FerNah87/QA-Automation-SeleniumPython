import unittest

from selenium import webdriver
from FuncionesLog import Page_Loguin
import HtmlTestRunner

class loguin_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    
    def test_1(self):
        driver = self.driver
        f=Page_Loguin(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath("//input[contains(@id,'user-name')]", "standard_user", 2)
        f.Texto_Xpath("//input[contains(@id,'password')]", "secret_sauce", 2)
        f.Click_Xpath("//input[contains(@id,'login-button')]", 2)
        print("Los datos son correctos")
        print("Prueba Login Ok")
    
    def test_2(self):
        driver = self.driver
        f=Page_Loguin(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath("//input[contains(@id,'user-name')]", "standard_usser", 2)
        f.Texto_Xpath("//input[contains(@id,'password')]", "secret_sauce", 2)
        f.Click_Xpath("//input[contains(@id,'login-button')]", 2)
        print("El usuario es incorrecto")
        print("Prueba error Login Ok")
    
    def test_3(self):
        driver = self.driver
        f=Page_Loguin(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath("//input[contains(@id,'user-name')]", "standard_user", 2)
        f.Texto_Xpath("//input[contains(@id,'password')]", "secrett_ssauce", 2)
        f.Click_Xpath("//input[contains(@id,'login-button')]", 2)
        print("La contraseña es incorrecta")
        print("Prueba error Login Ok")
    
    def test_4(self):
        driver = self.driver
        f=Page_Loguin(driver)
        f.Navegar("https://www.saucedemo.com/", 2)
        f.Texto_Xpath("//input[contains(@id,'user-name')]", "standard_user", 2)
        f.Texto_Xpath("//input[contains(@id,'password')]", "secret_sauce", 2)
        f.Click_Xpath("//input[contains(@id,'login-button')]", 2)
        f.Click_Xpath("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]", 2)
        f.Click_Xpath("//a[@class='shopping_cart_link'][contains(.,'1')]", 2)
        f.Click_Xpath("//button[contains(@id,'continue-shopping')]", 2)
        print("Agrega productos al carrito")
        print("Prueba Carrito Ok")
    
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='TestSaucedo\Reportes',  # Carpeta de salida
        report_name='Prueba generar informes Unittest',
        report_title='Pruebas Auto en https://www.saucedemo.com/',
        descriptions="Este es un reporte generado automáticamente.",
        add_timestamp=True,  # Para agregar la hora y fecha al reporte
    ))
    