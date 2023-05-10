from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep

import pandas as pd

# Inicializando o serviço do Chrome
service = Service('/home/gustgmrs/Downloads/chromedriver')
driver = webdriver.Chrome(service=service)

# Criando o DataFrame
df_processos = pd.read_excel('./files/processos.xlsx')

# Para cada linha do DataFrame, faça:
for i, linha in enumerate(df_processos.index):

    # Abrindo o navegador
    driver.get(
        'file:///home/gustgmrs/projetos/automacao-processo-juridico/files/index.html')

    # colocar o mouse em cima do dropdown
    dropdown = driver.find_element(By.XPATH, '/html/body/div/div')
    ActionChains(driver).move_to_element(dropdown).perform()

    # Escolhendo o estado
    cidade = df_processos.loc[linha, 'Cidade']
    driver.find_element(By.PARTIAL_LINK_TEXT, cidade).click()

    # mudar para a aba nova
    aba_principal = driver.window_handles[0]  # pega a aba principal
    indice = 1 + linha  # pega o índice da aba secundária
    nova_aba = driver.window_handles[indice]  # pega a aba secundária
    driver.switch_to.window(nova_aba)  # muda para a aba secundária

    # preencher formulário
    # Enviando nome do cliente
    nome = driver.find_element(By.ID, 'nome')
    nome.send_keys(df_processos.loc[linha, 'Nome'])

    # Enviando nome do advogado
    advogado = driver.find_element(By.ID, 'advogado')
    advogado.send_keys(df_processos.loc[linha, 'Advogado'])

    # Enviando número do processo
    processo = driver.find_element(By.ID, 'numero')
    processo.send_keys(df_processos.loc[linha, 'Processo'])

    # Clicando no botão de pesquisar
    pesquisar = driver.find_element(By.CLASS_NAME, 'registerbtn')
    pesquisar.click()
    sleep(2)

    # Aceitando o alert
    alerta = driver.switch_to.alert
    alerta.accept()

    # esperar o resultado da pesquisa e agir de acordo com o resultado
    while True:
        try:
            alerta = driver.switch_to.alert
            break
        except:
            sleep(1)

    sleep(2)
    texto_alerta = alerta.text

    if 'Processo encontrado com sucesso' in texto_alerta:
        alerta.accept()
        df_processos.loc[linha, 'Status'] = 'Encontrado'
    else:
        df_processos.loc[linha, 'Status'] = 'Não encontrado'
        alerta.accept()

driver.quit()
print(df_processos)
