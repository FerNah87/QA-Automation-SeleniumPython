#Utiliza la condicion que exite el logo/titulo
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=2

driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

titulo=driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())

btn1=driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(t)
else:
    print("No existe dicha imagen")

driver.close()

print("El Ejemplo de Alert es https://demoqa.com/ todo OK!!!")