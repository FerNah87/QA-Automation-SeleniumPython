import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class Funciones_Globales():
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
#-------- Texto XPATH secc 20.77--------
    def Texto_Xpath(self, xpath, texto, tiempo, boton_Login=None):
        valor=self.driver.find_element(By.XPATH, xpath)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(tiempo)
        return tiempo
#-------- Click XPATH--------    
    def Click_Xpath(self, xpath, tiempo):
        boton=self.driver.find_element(By.XPATH, xpath)
        boton.click()
        t = time.sleep(tiempo)
#-------- Texto ID secc 20.78--------
    def Texto_ID(self, ID, texto, tiempo, boton_Login=None):
        valor=self.driver.find_element(By.ID, ID)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(tiempo)
        return tiempo
 #-------- Click ID--------      
    def Click_ID(self, ID, tiempo):
        boton=self.driver.find_element(By.ID, ID)
        boton.click()
        t = time.sleep(tiempo)
#-------- Texto XPATH Mejorado secc 20.79-------se agrega el tiempo de espera antes del error-------
    def Texto_Xpath_Mejorado(self, xpath, texto, tiempo, boton_Login=None):
        try:
            valor=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor.clear()
            valor.send_keys(texto)
            t = time.sleep(tiempo)
            return tiempo
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)
#-------- Texto XPATH Mejorado secc 20.80-------hace scroll al elemento-------
    def Texto_Xpath_Mejorado_2(self, xpath, texto, tiempo, boton_Login=None):
        try:
            valor=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView()", valor)
            valor.clear()
            valor.send_keys(texto)
            t = time.sleep(tiempo)
            return tiempo
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)
