import selenium
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utils.funces_globales import funciones
from utils.funciones_DD import data_Driven
from utils.casos_globales import casos

@pytest.fixture()
def navegador():
    navegador=webdriver.Chrome()
    navegador.get("https://formy-project.herokuapp.com/")
    navegador.maximize_window()
    yield navegador
    print("Cierre del navegador")
    navegador.quit()

def test1_caso (navegador):
    cas=casos(navegador)
    cas.carga_masivaDD()