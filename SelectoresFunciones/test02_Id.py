#Automatizacion completando un formulario. se utiliza el elemento Id y Click
import time

from selenium import webdriver

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nombre = driver.find_element("id","userName")
nombre.send_keys("Fer")
time.sleep(t)

email=driver.find_element("id","userEmail")
email.send_keys("coso@coso.com")
time.sleep(t)

driver.find_element("id","currentAddress").send_keys("Tres de Febrero")
time.sleep(t)
driver.find_element("id","permanentAddress").send_keys("Martin Coronado")
time.sleep(t)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

driver.find_element("id","submit").click()
time.sleep(t)

driver.close()

print("Exito Selector Id y Funcion Click")