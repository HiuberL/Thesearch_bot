from errno import ECANCELED
from tokenize import Number
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as econdi
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy
import os

def comprobData_previos(Datanew,Dataprevious):
    if len(Dataprevious) != 0:
        existe = Dataprevious.__contains__(Datanew)
        if not existe:
            return False
        else:
            return True
    else:
            return False

def scrappingComputrabajo(Country,Dataprevious):
    Data = []
    option = webdriver.ChromeOptions()
    option.add_argument('--start-maximized')
    option.add_argument('--disable-extensions')
    option.add_argument("--headless")
    option.add_argument("disable-gpu")
    option.add_argument("--log-level=3")
    driver_path = os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
    driver = webdriver.Chrome(driver_path,chrome_options=option)
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
    driver.close()        
    return Data

def scrappingUnmejorempleo(Country,Dataprevious):
    Data = []
    option = webdriver.ChromeOptions()
    option.add_argument('--start-maximized')
    option.add_argument('--disable-extensions')
    option.add_argument("--headless")
    option.add_argument("disable-gpu")
    option.add_argument("--log-level=3")
    driver_path = os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
    driver = webdriver.Chrome(driver_path,chrome_options=option)
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
    driver.close()        
    return Data

def scrappinglinkedin(Dataprevious):
    Data = []
    option = webdriver.ChromeOptions()
    option.add_argument('--start-maximized')
    option.add_argument('--disable-extensions')    
    option.add_argument("--headless")
    option.add_argument("disable-gpu")
    option.add_argument("--window-size=1500x10000");
    option.add_argument("--log-level=3")
    driver_path = os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
    driver = webdriver.Chrome(driver_path,chrome_options=option)
    time.sleep(1)
    driver.get('https://www.linkedin.com/jobs/search/?geoId=106373116&location=Ecuador&position=1&pageNum=0')       
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
    driver.close()        
    return Data
