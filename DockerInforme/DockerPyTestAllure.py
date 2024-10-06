import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

t = 1

@pytest.fixture(scope="function")
def driver():
    options = Options()
    #options.add_argument("--headless")  # Opcional: ejecuta Chrome en modo headless (sin interfaz gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Conectar al contenedor de Selenium
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()

@allure.feature("DemoQA Form Test")
@allure.story("Fill and submit text box form")
def test_demoqa_form(driver):
    with allure.step("Abrir DemoQA página"):
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
        time.sleep(t)

    with allure.step("Completar el formulario"):
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
    
    with allure.step("Hacer scroll y enviar el formulario"):
    #para bajar la ventana y que se vea el boton y no de error
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(t)

    driver.find_element("xpath","//*[@id='submit']").click()
    time.sleep(t)

    # Cerrar el navegador
    driver.quit()