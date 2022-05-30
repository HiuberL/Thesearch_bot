from tokenize import Number
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as econdi
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy
import os
import id

def comprobData_previos(Datanew,Dataprevious):
    if len(Dataprevious) != 0:
        for datos in Dataprevious:
            if Datanew[0] == datos[0]:
                return True
        return False
    else:
            return False

def scrappingdata(page,Country,Dataprevious):
    Data = []
    option = webdriver.ChromeOptions()
    option.add_argument('--start-maximized')
    option.add_argument('--disable-extensions')
    option.add_argument("--headless")
    option.add_argument("disable-gpu")
    option.add_argument("--log-level=3")
    option.add_argument("window-size=1500x50000")
    driver_path = os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
    driver = webdriver.Chrome(driver_path,chrome_options=option)
    
    if page == "CT":
        time.sleep(1)    
        driver.get('https://www.computrabajo.com.ec/empleos-en-'+Country+'?by=publicationtime')

        for n in range(1,11):
            try:
                time.sleep(1)
                WebDriverWait(driver,10)\
                    .until(econdi.element_to_be_clickable((By.XPATH,'/html/body/main/div[3]/div[2]/div[1]/div[2]/article['+ str(n) +']/div[1]/h1/a')))\
                    .click()
                time.sleep(1)
                try:
                    advertencia = driver.find_element(By.XPATH,'/html/body/main/div[3]/div[2]/h1')
                    advertencia = advertencia.text
                except:
                    advertencia = '0'
                if advertencia == "0" :
                    Title = driver.find_element(By.XPATH,'/html/body/main/div[1]/h1')
                    Title = Title.text
                    Description = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[2]/div[2]/p[1]')
                    Description = Description.text
                    Position = driver.find_element(By.XPATH,'/html/body/main/div[1]/p')
                    Position = Position.text
                    direccion = driver.current_url
                    c = comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:
                        Data.append([Title,Position,Description,direccion])                
                    WebDriverWait(driver,100)\
                        .until(econdi.element_to_be_clickable((By.XPATH,'//*[@id="back_to_list"]/a')))\
                        .click()
                else:
                    driver.get('https://www.computrabajo.com.ec/empleos-en-'+Country+'?by=publicationtime')
            except:
                pass

    if page == "UME":
        time.sleep(1)
        driver.get('https://www.unmejorempleo.com.ec/empleos?u='+Country+'&f=1')
        time.sleep(1)
        for n in range(1,21):
            try:    
                Title = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/h3')
                Title = Title.text
                direccion = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/h3/a')
                direccion = direccion.get_attribute('href')
                Position = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[1]')
                Position = Position.text
                Description = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[2]')
                Description = Description.text
                Date = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[3]')
                Date = Date.text
                Description = Description + "\n"+Date
                c = comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                if not c:
                    Data.append([Title,Position,Description,direccion])
            except:
                pass
            
    if page == "LIN":
        time.sleep(1)
        driver.get('https://www.linkedin.com/jobs/search/?keywords=&location=Ecuador&locationId=&geoId=106373116&f_TPR=r86400&position=1&pageNum=0')       
        time.sleep(5)
        for n in range(1,21):
            try:
                driver.find_element(By.XPATH,'/html/body/div[1]/div/main/section/ul/li['+str(n)+']').click()
                time.sleep(2)
                Title = driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/a/h2')
                Title = Title.text
                direccion = driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/a')
                direccion = direccion.get_attribute('href')
                Empresa = driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/h4/div[1]/span[1]')
                Empresa = Empresa.text
                Position = driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/h4/div[1]/span[2]')
                Position = Position.text
                Position = Position + " | " + Empresa
                Description = driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/section/div/div/section/div')
                Description = Description.text
                c = comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                if not c:
                    Data.append([Title,Position,Description,direccion])        
            except:
                pass
            
    if page == "EE":
        time.sleep(1)
        driver.get('https://encuentraempleo.trabajo.gob.ec/socioEmpleo-war/paginas/procesos/busquedaOferta.jsf')       
        time.sleep(2)
        for i in range(1,6):
            time.sleep(2)
            for n in range(1,6):
                try:
                    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/form/table/tbody/tr/td[2]/fieldset['+str(n)+']/div/a').click()
                    time.sleep(2)
                    Title = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]')
                    Title = Title.text
                    Position = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]')
                    Position = Position.text
                    Description = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]')
                    Description2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[4]')
                    Description3 = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]')
                    Description = Description.text + "\n" + Description2.text + '\n' + Description3.text
                    direccion = driver.current_url
                    c = comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:
                        Data.append([Title,Position,Description,direccion])        
                    driver.back()
                    time.sleep(1)
                except:
                    pass
            driver.find_element(By.CSS_SELECTOR,'#formBuscaOferta\:pagina > div.ui-selectonemenu-trigger.ui-state-default.ui-corner-right > span').click()
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR,'#formBuscaOferta\:pagina_'+str(i)+'').click()
            
    if page =="ET":
        time.sleep(1)
        driver.get('https://e-talent.jobs/bolsa-de-trabajo/#s=1')       
        time.sleep(2)
        for i in id.Datos.Diccionario_ext:
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,'#search_location').send_keys(i)
            driver.find_element(By.CSS_SELECTOR,'#search_location').send_keys(Keys.ENTER)
            time.sleep(2)
            for n in range(1,11):
                try:
                    driver.find_element(By.XPATH,'//*[@id="post-19"]/div/div/ul/li['+str(n)+']').click()
                    time.sleep(1)    
                    Title = driver.find_element(By.CSS_SELECTOR,'#job-details > div > div > ul > li:nth-child(4) > div > span')
                    Title = Title.text
                    Position = driver.find_element(By.CSS_SELECTOR,'#job-details > div > div > ul > li:nth-child(3) > div > span > a')
                    Position = Position.text
                    Empresa = driver.find_element(By.CSS_SELECTOR,'#wrapper > div.container.right-sidebar > div.eleven.columns > div > div.company-info.left-company-logo > div.content > h4 > a > strong')
                    Empresa = Empresa.text
                    Position = Empresa + ' | ' + Position
                    Description = driver.find_element(By.CSS_SELECTOR,'#wrapper > div.container.right-sidebar > div.eleven.columns > div > div.single_job_listing > div.job_description')
                    Description = Description.text
                    direccion = driver.current_url
                    c = comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:
                        Data.append([Title,Position,Description,direccion])        
                    driver.back()
                    time.sleep(1)
                except:
                    pass
            driver.get('https://e-talent.jobs/bolsa-de-trabajo/#s=1')
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,'#wrapper > div.container.wpjm-container.full-width > div > form > div.job_filters_links > a.reset').click()        
    driver.close()        
    return Data


