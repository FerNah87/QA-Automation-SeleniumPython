import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

t = 1

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(t)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

btnCheckMale = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='male']")))
btnCheckMale.click()

btnCheckFemale = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='female']")))
btnCheckFemale.click()

btnCheckSunday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'sunday')]")))
btnCheckSunday.click()

btnCheckMonday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'monday')]")))
btnCheckMonday.click()

btnCheckTuesday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'tuesday')]")))
btnCheckTuesday.click()

btnCheckWednesday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'wednesday')]")))
btnCheckWednesday.click()

btnCheckThursday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'thursday')]")))
btnCheckThursday.click()

btnCheckFriday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'friday')]")))
btnCheckFriday.click()

btnCheckSaturday = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'saturday')]")))
btnCheckSaturday.click()

btnColorsRed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='red'][contains(.,'Red')]")))
btnColorsRed.click()

btnColorsYellow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='yellow'][contains(.,'Yellow')]")))
btnColorsYellow.click()

btnColorsBlue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='blue'][contains(.,'Blue')]")))
btnColorsBlue.click()

btnColorsGreen = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='green'][contains(.,'Green')]")))
btnColorsGreen.click()


time.sleep(t)
driver.close()

print("La pagina de Checkbox es https://testautomationpractice.blogspot.com/")