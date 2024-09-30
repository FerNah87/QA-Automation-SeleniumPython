#Automatizacion completando un formulario. se utiliza el elemento By.Id y Click
#Importar el By
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nombre = driver.find_element(By.ID,"userName")
nombre.send_keys("Fer")
time.sleep(t)

email=driver.find_element(By.ID,"userEmail")
email.send_keys("coso@coso.com")
time.sleep(t)

driver.find_element(By.ID,"currentAddress").send_keys("Tres de Febrero")
time.sleep(t)
driver.find_element(By.ID,"permanentAddress").send_keys("Martin Coronado")
time.sleep(t)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

driver.find_element(By.ID,"submit").click()
time.sleep(t)

driver.close()

print("Exito Selector By.Id y Funcion Click")