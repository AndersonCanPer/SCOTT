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
from utils.funces_globales import funciones
from utils.funciones_DD import data_Driven

class casos ():
    
    def __init__(self,driver):
        self.driver=driver
    
    def carga_masivaDD(self):
        driver=self.driver
        driver.implicitly_wait(10)
        fces=funciones(driver)
        dd=data_Driven()
        #Click en el linktest para abrir el formulario
        fces.click_linktext("Form")
        #Ingreso de data con las funciones de data driven
        path=r'C:/Users/Dell/Desktop/PCAS/probando.xlsx'
        sheetname='Hoja1'
        fila=dd.contar_Filas(path,sheetname)
        for f in range (2,fila+1):
            estado_datos=dd.leer_Datos(path,sheetname,f,5)
            if estado_datos=='No Insertado' or estado_datos==None:
                
                name=dd.leer_Datos(path,sheetname,f,1)
                name2=dd.leer_Datos(path,sheetname,f,2)
                apellido=dd.leer_Datos(path,sheetname,f,3)
                job_tilte=dd.leer_Datos(path,sheetname,f,4)
                
                fces.diligenciar_campo("css","input#first-name",name)
                fces.diligenciar_campo("css","input#first-name",name2)
                fces.diligenciar_campo("css","input#last-name",apellido)
                fces.diligenciar_campo("css","input#job-title",job_tilte)
                
                fces.clic_botton("css","a[role=button]")
                elemento=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-success']")))
                if elemento:
                    print(f"Se visualiza la alerta: {elemento.text}")
                    dd.insertar_Datos(path,sheetname,f,5,"Insertado")
                    driver.back()
                else:
                    print("No se visualizo la alerta")
                    dd.insertar_Datos(path,sheetname,f,5,"No Insertado")
                    driver.back()
            elif estado_datos=="Insertado":
                print(f"""Los datos de la fila: {f} ya fueron insertados: 
                     Name: {dd.leer_Datos(path,sheetname,f,1)} 
                     Name2: {dd.leer_Datos(path,sheetname,f,2)}
                     Apellido: {dd.leer_Datos(path,sheetname,f,3)}
                     Job_tiltle: {dd.leer_Datos(path,sheetname,f,4)}
                     Estado: {dd.leer_Datos(path,sheetname,f,5)}
                      """)
            else:
                driver.quit()
        