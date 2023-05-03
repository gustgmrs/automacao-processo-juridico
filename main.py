from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from time import sleep

# Inicializando o serviço do Chrome
service = Service('/home/gustgmrs/Downloads/chromedriver')
driver = webdriver.Chrome(service=service)

# Abrindo o navegador
driver.get(
    'file:///home/gustgmrs/projetos/automacao-processo-juridico/files/index.html')

# Escolhendo o estado
dropdown = driver.find_element(By.XPATH, '/html/body/div/div')
item = driver.find_element(By.XPATH, '/html/body/div/div/div/a[2]')

# colocar o mouse em cima do dropdown
ActionChains(driver).move_to_element(dropdown).perform()

# clicar no item
item.click()
