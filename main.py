from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


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
sleep(2)

aba_principal = driver.window_handles[0]  # pega a aba principal
aba_secundaria = driver.window_handles[1]  # pega a aba secundária

# mudar para a aba secundária
driver.switch_to.window(aba_secundaria)
sleep(2)

# Enviando nome do cliente
nome = driver.find_element(By.ID, 'nome')
nome.send_keys('Gustavo')

# Enviando nome do advogado
advogado = driver.find_element(By.ID, 'advogado')
advogado.send_keys('Victória')

# Enviando número do processo
processo = driver.find_element(By.ID, 'numero')
processo.send_keys('123456789')

# Clicando no botão de pesquisar
pesquisar = driver.find_element(By.CLASS_NAME, 'registerbtn')
pesquisar.click()
sleep(2)

# Aceitando o alert
alerta = Alert(driver)
alerta.accept()
sleep(10)
