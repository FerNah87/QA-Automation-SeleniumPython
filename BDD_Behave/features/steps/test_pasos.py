from behave import *

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from steps.FuncionesBDD import Funciones_Globales

@given(u'Abriendo el Navegador')
def step_impl(context):
    global driver, f
    context.driver = webdriver.Chrome() 
    f=Funciones_Globales(context.driver)
    f.Navegar("https://demoqa.com/text-box", 2)

@when(u'Cargando el Nombre de Usuario')
def step_impl(context):
    f.Texto_Xpath("//input[@type='text']", "Test Nombre Usuario", 2)

@then(u'Cargando el Email')
def step_impl(context):
    f.Texto_Xpath("//input[@type='email']", "Test Email", 2)

@then(u'Cargando su direccion')
def step_impl(context):
    f.Texto_Xpath("//textarea[@placeholder='Current Address']", "Coso Domicilio 123", 2)
