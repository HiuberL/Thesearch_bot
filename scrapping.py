from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as econdi
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy
import os
import id

class connect(object):
    def __init__(self) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        option.add_argument("--headless")
        option.add_argument("disable-gpu")
        option.add_argument("--log-level=3")
        option.add_argument("window-size=1500x50000")
        driver_path = os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path,chrome_options=option)

    @staticmethod
    def comprobData_previos(Datanew,Dataprevious):
        if len(Dataprevious) != 0:
            for datos in Dataprevious:
                if Datanew[0] == datos[0]:
                    return True
            return False
        else:
                return False

    def scrappingdata(self,page,Country,Dataprevious):
        Data = []
        if page == "CT":
            time.sleep(1)    
            self.driver.get('https://www.computrabajo.com.ec/empleos-en-'+Country+'?by=publicationtime')

            for n in range(1,11):
                try:
                    time.sleep(1)
                    WebDriverWait(self.driver,10)\
                        .until(econdi.element_to_be_clickable((By.XPATH,'/html/body/main/div[3]/div[2]/div[1]/div[2]/article['+ str(n) +']/div[1]/h1/a')))\
                        .click()
                    time.sleep(1)
                    try:
                        advertencia = self.driver.find_element(By.XPATH,'/html/body/main/div[3]/div[2]/h1')
                        advertencia = advertencia.text
                    except:
                        advertencia = '0'
                    if advertencia == "0" :
                        Title = self.driver.find_element(By.XPATH,'/html/body/main/div[1]/h1')
                        Title = Title.text
                        Description = self.driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[2]/div[2]/p[1]')
                        Description = Description.text
                        Position = self.driver.find_element(By.XPATH,'/html/body/main/div[1]/p')
                        Position = Position.text
                        direccion = self.driver.current_url
                        c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                        if not c:
                            Data.append([Title,Position,Description,direccion])                
                        WebDriverWait(self.driver,100)\
                            .until(econdi.element_to_be_clickable((By.XPATH,'//*[@id="back_to_list"]/a')))\
                            .click()
                    else:
                        self.driver.get('https://www.computrabajo.com.ec/empleos-en-'+Country+'?by=publicationtime')
                except:
                    pass

        if page == "UME":
            time.sleep(1)
            self.driver.get('https://www.unmejorempleo.com.ec/empleos?u='+Country+'&f=1')
            time.sleep(1)
            for n in range(1,21):
                try:    
                    Title = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/h3')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/h3/a')
                    direccion = direccion.get_attribute('href')
                    Position = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[1]')
                    Position = Position.text
                    Description = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[2]')
                    Description = Description.text
                    Date = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/article/div['+str(n)+']/ul/li[3]')
                    Date = Date.text
                    Description = Description + "\n"+Date
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:
                        Data.append([Title,Position,Description,direccion])
                except:
                    pass
                
        if page == "LIN":
            time.sleep(1)
            self.driver.get('https://www.linkedin.com/jobs/search/?keywords=&location=Ecuador&locationId=&geoId=106373116&f_TPR=r86400&position=1&pageNum=0')       
            time.sleep(5)
            for n in range(1,21):
                try:
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div/main/section/ul/li['+str(n)+']').click()
                    time.sleep(2)
                    Title = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/a/h2')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/a')
                    direccion = direccion.get_attribute('href')
                    Empresa = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/h4/div[1]/span[1]')
                    Empresa = Empresa.text
                    Position = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[2]/div/h4/div[1]/span[2]')
                    Position = Position.text
                    Position = Position + " | " + Empresa
                    Description = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/section/div/div/section/div')
                    Description = Description.text
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:
                        Data.append([Title,Position,Description,direccion])        
                except:
                    pass
                
        if page == "EE":
            time.sleep(1)
            self.driver.get('https://encuentraempleo.trabajo.gob.ec/socioEmpleo-war/paginas/procesos/busquedaOferta.jsf')       
            time.sleep(2)
            for i in range(1,6):
                time.sleep(2)
                for n in range(1,6):
                    try:
                        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/form/table/tbody/tr/td[2]/fieldset['+str(n)+']/div/a').click()
                        time.sleep(2)
                        Title = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]')
                        Title = Title.text
                        Position = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]')
                        Position = Position.text
                        Description = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]')
                        Description2 = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[4]')
                        Description3 = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]')
                        Description = Description.text + "\n" + Description2.text + '\n' + Description3.text
                        direccion = self.driver.current_url
                        c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                        if not c:
                            Data.append([Title,Position,Description,direccion])        
                        self.driver.back()
                        time.sleep(1)
                    except:
                        pass
                self.driver.find_element(By.CSS_SELECTOR,'#formBuscaOferta\:pagina > div.ui-selectonemenu-trigger.ui-state-default.ui-corner-right > span').click()
                time.sleep(0.5)
                self.driver.find_element(By.CSS_SELECTOR,'#formBuscaOferta\:pagina_'+str(i)+'').click()
                
        if page =="ET":
            time.sleep(1)
            self.driver.get('https://e-talent.jobs/bolsa-de-trabajo/#s=1')       
            time.sleep(2)
            for i in id.Datos.Diccionario_ext:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR,'#search_location').send_keys(i)
                self.driver.find_element(By.CSS_SELECTOR,'#search_location').send_keys(Keys.ENTER)
                time.sleep(2)
                for n in range(1,11):
                    try:
                        self.driver.find_element(By.XPATH,'//*[@id="post-19"]/div/div/ul/li['+str(n)+']').click()
                        time.sleep(1)    
                        Title = self.driver.find_element(By.CSS_SELECTOR,'#job-details > div > div > ul > li:nth-child(4) > div > span')
                        Title = Title.text
                        Position = self.driver.find_element(By.CSS_SELECTOR,'#job-details > div > div > ul > li:nth-child(3) > div > span > a')
                        Position = Position.text
                        Empresa = self.driver.find_element(By.CSS_SELECTOR,'#wrapper > div.container.right-sidebar > div.eleven.columns > div > div.company-info.left-company-logo > div.content > h4 > a > strong')
                        Empresa = Empresa.text
                        Position = Empresa + ' | ' + Position
                        Description = self.driver.find_element(By.CSS_SELECTOR,'#wrapper > div.container.right-sidebar > div.eleven.columns > div > div.single_job_listing > div.job_description')
                        Description = Description.text
                        direccion = self.driver.current_url
                        c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                        if not c:
                            Data.append([Title,Position,Description,direccion])        
                        self.driver.back()
                        time.sleep(1)
                    except:
                        pass
                self.driver.get('https://e-talent.jobs/bolsa-de-trabajo/#s=1')
                time.sleep(2)
                WebDriverWait(self.driver,10)\
                    .until(econdi.element_to_be_clickable((By.CSS_SELECTOR,'#wrapper > div.container.wpjm-container.full-width > div > form > div.job_filters_links > a.reset')))\
                    .click()
                    
        if page =="TD":
            time.sleep(1)
            self.driver.get('https://ec.trabajosdiarios.com/ofertas-trabajo')       
            time.sleep(2)
            s = 4
            for n in range(1,13):
                if n%2==0:
                    s = 5
                else:
                    s = 4
                try:
                    Title = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div['+str(n)+']/div/a/div[1]/div[1]')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div['+str(n)+']/div/a')
                    direccion = direccion.get_attribute('href')
                    Empresa = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div['+str(n)+']/div/a/div[3]')
                    Empresa = Empresa.text
                    Position = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div['+str(n)+']/div/a/div[2]')
                    Position = Position.text
                    Position = Position + " | " + Empresa
                    Description = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div['+str(n)+']/div/a/div['+str(s)+']')
                    Description = Description.text
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:                    
                        Data.append([Title,Position,Description,direccion])
                except:
                    pass       
        if page =='OE':
            time.sleep(1)
            self.driver.get('https://www.opcionempleo.ec/ofertas-empleo-ecuador-114371.html?radius=15&nw=1')       
            time.sleep(2)
            for n in range(1,21):
                try:
                    Title = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/ul[2]/li['+str(n)+']/article/header/h2/a')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/ul[2]/li['+str(n)+']/article/header/h2/a')
                    direccion = direccion.get_attribute('href')
                    Empresa = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/ul[2]/li['+str(n)+']/article/p')
                    Empresa = Empresa.text
                    Position = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/ul[2]/li['+str(n)+']/article/ul[2]/li')
                    Position = Position.text
                    Position = Position + " | " + Empresa
                    Description = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/ul[2]/li['+str(n)+']/article/div')
                    Description = Description.text
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:                            
                        Data.append([Title,Position,Description,direccion])        
                except:
                    pass
        if page == 'AT':
            time.sleep(1)
            self.driver.get('https://acciontrabajo.ec/buscar-empleos?o=d')       
            time.sleep(2)
            for n in range(1,21):
                try: 
                    Title = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/article/section['+str(n)+']/div/a/h2')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/article/section['+str(n)+']/div/a')
                    direccion = direccion.get_attribute('href')
                    Empresa = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/article/section['+str(n)+']/div/a/b')
                    Empresa = Empresa.text
                    Position = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/article/section['+str(n)+']/div/div/div/div[2]/span')
                    Position = Position.text
                    Position = Position + " | " + Empresa
                    Description = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/article/section['+str(n)+']/div/a/span')
                    Description = Description.text
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:                        
                        Data.append([Title,Position,Description,direccion])        
                except:
                    pass            
        if page == 'PE':
            time.sleep(1)
            self.driver.get('https://www.porfinempleo.com')       
            time.sleep(2)
            for n in range(1,21):
                try: 
                    Title = self.driver.find_element(By.XPATH,'/html/body/div/div[4]/section[2]/div/div/div/div[2]/div['+str(n)+']/div[2]/div/a[1]/div')
                    Title = Title.text
                    direccion = self.driver.find_element(By.XPATH,'/html/body/div/div[4]/section[2]/div/div/div/div[2]/div['+str(n)+']/div[2]/div/a[1]')
                    direccion = direccion.get_attribute('href')
                    Position = self.driver.find_element(By.XPATH,'/html/body/div/div[4]/section[2]/div/div/div/div[2]/div['+str(n)+']/div[2]/div/a[2]/span')
                    Position = Position.text
                    Position = Position
                    Description = self.driver.find_element(By.XPATH,'/html/body/div/div[4]/section[2]/div/div/div/div[2]/div['+str(n)+']/div[2]/p')
                    Description = Description.text
                    c = self.comprobData_previos([Title,Position,Description,direccion],Dataprevious)
                    if not c:                     
                        Data.append([Title,Position,Description,direccion])        
                except:
                    pass            
        return Data

    def close(self):
        self.driver.close()
