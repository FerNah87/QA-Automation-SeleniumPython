#Primera opcion para hacer informes pytest-htm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
t = 1
options = Options()

#options.add_argument("--headless")  # Opcional: ejecuta Chrome en modo headless (sin interfaz gráfica)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Conectar al contenedor de Selenium
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Realizar alguna acción en el navegador
#driver.get("https://www.google.com")
#print(driver.title)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
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

#hace captura de la pantalla para evidencia
#driver.save_screenshot("testDockerSele.jpeg")

# Cerrar el navegador
driver.quit()