import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=1

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)

#Nueva forma de SCROLL sin saber el tiempo (eliminar windows.scrollTo)
try:
    Buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Descubre más')]")))
    Buscar=driver.find_element(By.XPATH, "//span[contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no estaaaaa")


time.sleep(t)
driver.close()

print("La pagina de EJEMPLO Scroll es https://pixabay.com/es/ y todo OK!!!")