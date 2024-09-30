#Automatizacion completando un formulario. se utiliza el elemento By.Xpath - salto de linea TAB y Click
#Importar el By
#Importar el Keys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nombre = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")
nombre.send_keys("Fer")
nombre.send_keys(Keys.TAB + "cualquiera@cualquiera.com" + Keys.TAB + "Tres de Febrero" + Keys.TAB + "Martin Coronado" + Keys.TAB + Keys.ENTER)
time.sleep(t)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

driver.find_element(By.CSS_SELECTOR,"#submit").click()
time.sleep(t)

driver.close()

print("Exito Selector By Xpath - salto de linea TAB y Funcion Click")