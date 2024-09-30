#Utiliza la condicion que exite el logo/titulo y la funcion de un boton al darle click
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=2

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

#validar el boton
btn_submit=driver.find_element("xpath", "//button[@type='button'][contains(.,'Submit')]")
print(btn_submit.is_enabled())

if(btn_submit.is_enabled()==True):
    print("Puede dar click")
else:
    print("No esta activo")

driver.close()

print("Validar el Boton https://demoqa.com/text-box todo OK!!!")