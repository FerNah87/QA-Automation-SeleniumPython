#Automatizacion para navegar y volver a la pagina anterio

import time

from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=1

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.google.com/")
time.sleep(t)

driver.get("https://www.youtube.com/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
#driver.back()
time.sleep(t)

driver.execute_script("window.history.go(-1)")
#driver.back()
time.sleep(t)

driver.close()

print("Exito Navegar!!!")
#Se puede navegar por diferentes paginas