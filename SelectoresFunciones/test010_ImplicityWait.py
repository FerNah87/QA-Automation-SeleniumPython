#Implicity Wait: espera un tiempo determinado antes de lanzar una excepción si no puede encontrar un elemento
#espera hasta que el elemento este disponible en el DOM, si el elemento aparece el script continuará inmediatamente. Si no, lanzará una excepción NoSuchElementException
import time

from selenium import webdriver

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(t)

nombre = driver.find_element("xpath","//input[contains(@id,'userName')]")
nombre.send_keys("Fer")
time.sleep(t)

email=driver.find_element("xpath","//input[contains(@id,'userEmail')]")
email.send_keys("coso@coso.com")
time.sleep(t)

driver.find_element("xpath","//*[@id='currentAddress']").send_keys("Tres de Febrero")
time.sleep(t)
driver.find_element("xpath","//*[@id='permanentAddress']").send_keys("Martin Coronado")
time.sleep(t)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

driver.find_element("xpath","//*[@id='submit']").click()
time.sleep(t)

driver.close()

print("Exito Selector Xpath y Funcion Click")