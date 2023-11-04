import selenium
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
from utils.funciones_DD import data_Driven


class funciones ():
    
    def __init__(self,driver):
        self.driver=driver
    
    def clic_botton(self,tipo_selector,selector):
        driver=self.driver
        if tipo_selector=="css":
            try:
                elemento=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",elemento)
                print(f"Se da clic en el boton {elemento.text}")
                elemento.click()
            except TimeoutException as e:
                print(e, f"No se halla elemento: {selector}")
        elif tipo_selector=="xpath":
            try:
                elemento=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",elemento)
                print(f"Se da clic en el boton: {elemento.text}")
                elemento.click()
            except TimeoutException as e:
                print(e,f"No se halla el elemento: {selector}")
        else:
            print(f"El tipo de selector ingresdo no es valido, debe ser 'css' o 'xpath', utd ingreso: {tipo_selector}")
            
    def click_linktext (self,texto):
        driver=self.driver
        driver.implicitly_wait(10)
        try:
            linktext=driver.find_element(By.LINK_TEXT,texto)
            driver.execute_script("arguments[0].scrollIntoView();",linktext)
            linktext.click()
        except NoSuchElementException as e:
            print(e,f"No se halla el el elemento: {texto}")
    
    def diligenciar_campo(self, tipo_Selectoor, selector,valores):
        driver=self.driver
        if tipo_Selectoor == 'css':
            try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",campo)
                campo.send_keys(valores)
                print(f"Se diligencia el campo: {selector} con los valores: {valores}")
            except TimeoutException as e:
                print(f"No se halla el elemento: {selector}") 
        elif tipo_Selectoor == 'xpath':
            try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",campo)
                campo.send_keys(valores)
                print(f"Se diligencia el campo: {selector} con los valores: {valores}")
            except TimeoutException as e:
                print(f"No se halla el elemento: {selector}") 
        else:
            print(f"El tipo de selector ingresado no es valido deberia ser 'css' o 'xpath' utd ingreso: {tipo_Selectoor}")
        
    def DataDriven_Datoespecifico (self, tipo_selector,selector,path,sheetname,num_fila,num_columna):
        driver=self.driver
        fdd=data_Driven()
        dato_ingresar=fdd.leer_Datos(path,sheetname,num_fila,num_columna)
        if tipo_selector=='css':
            try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector)))
                driver.excute_script("arguments[0].scrollIntoView();",campo)
                campo.send_keys(dato_ingresar)
            except TimeoutException as e:
                print(e, f"No se haya el elemento {selector}")
        elif tipo_selector=='xpath':
            try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,selector)))
                driver.excute_script("arguments[0].scrollIntoView();",campo)
                campo.send_keys(dato_ingresar)
            except TimeoutException as e:
                print(e, f"No se haya el elemento {selector}")
        else:
            print(f"El tipo de selector ingresado no es valido, debe ingrear 'css' o 'xpath' utd ingreso: {tipo_selector}")
            
    def validar_elemento(self,tipo_selector,selector):
        driver=self.driver
        if tipo_selector=='css':
            try:
                elemento=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",elemento)
                print(f"El elemento {selector} está visible")
            except TimeoutException as e:
                print(e,f"No se halla el elemeno {selector}")
        elif tipo_selector=='xpath':
            try:
                elemento=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",elemento)
                print(f"El elemento {selector} está visible")
            except TimeoutException as e:
                print(e,f"No se halla el elemeno {selector}")
        else:
            print(f"El tipo de selector ingresado no es valido, debe ingrear 'css' o 'xpath' utd ingreso: {tipo_selector}")
            
    def diligenciar_combobox(self,tipo_selector,selector,seleccionar_por,opcion):
        driver=self.driver
        if tipo_selector=='css':
            try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",campo)
                seleccion=Select(campo)
                opciones=seleccion.options
                print(f"El campo {selector} tiene las opciones: ")
                for p in opciones:
                    print(p.text)
                if seleccionar_por=='index':
                    seleccion.select_by_index(opcion)
                elif seleccionar_por=='value':
                    seleccion.select_by_value(opcion)
                elif seleccion=='visible_text':
                    seleccion.select_by_visible_text(opcion)
                else:
                    print(f"""La opcion para seleccionar que ingresaste: '{seleccionar_por}' 
                          no es valida debe ser por 'index', 'value, o 'visible_text'' """)            
            except TimeoutException as e:
                print(e,f"No se halla el elemnto {selector}")
        elif tipo_selector=='xpath':
             try:
                campo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,selector)))
                driver.execute_script("arguments[0].scrollIntoView();",campo)
                seleccion=Select(campo)
                opciones=seleccion.options
                print(f"El campo {selector} tiene las opciones: ")
                for p in opciones:
                    print(p.text)
                if seleccionar_por=='index':
                    seleccion.select_by_index(opcion)
                elif seleccionar_por=='value':
                    seleccion.select_by_value(opcion)
                elif seleccion=='visible_text':
                    seleccion.select_by_visible_text(opcion)
                else:
                    print(f"""La opcion para seleccionar que ingresaste: '{seleccionar_por}' 
                          no es valida debe ser por 'index', 'value, o 'visible_text'' """)            
             except TimeoutException as e:
                print(e,f"No se halla el elemnto {selector}")
        else:
            print(f"El tipo de selector ingresado es erroneo: {tipo_selector}, debe ser 'css' o 'xpath'") 