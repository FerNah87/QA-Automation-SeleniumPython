#Explicity Wait: 
#espera hasta que el elemento este disponible en el DOM, si el elemento aparece el script continuará inmediatamente. Si no, lanzará una excepción NoSuchElementException

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(t)

#Las 2 formas
#driver.find_element_by_xpath("//input[contains(@id,'user-message')]").send_keys("Coso de Bienvenido")
#time.sleep(t)
#driver.find_element_by_xpath("//button[contains(.,'Show Message')]").click()
#time.sleep(t)

#Es para el MODAL que actualmente no aparece
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='at-cv-lightbox-button-holder']/a[2]")))
# element.click()

#driver.find_element_by_xpath("//*[@id='at-cv-lightbox-button-holder']/a[2]").click()

driver.find_element_by_xpath("//input[contains(@id,'user-message')]").send_keys("Coso de Bienvenido" + Keys.TAB + Keys.ENTER )
time.sleep(t)


driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

#Las 2 formas
#driver.find_element_by_xpath("//input[contains(@id,'sum1')]").send_keys("5")
#time.sleep(t)
#driver.find_element_by_xpath("//input[contains(@id,'sum2')]").send_keys("6")
#time.sleep(t)
#driver.find_element_by_xpath("//button[contains(.,'Get Total')]").click()
#time.sleep(t)
driver.find_element_by_xpath("//input[contains(@id,'sum1')]").send_keys("5" + Keys.TAB + "6" + Keys.TAB + Keys.ENTER)

time.sleep(t)
driver.close()

print("La pagina de EJEMPLO es https://demoqa.com/text-box")