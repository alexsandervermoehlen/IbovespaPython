import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import pandas as pd
import openpyxl

def get_dados():
    # as duas linhas a baico instanciam para executar apenas o codigo por baixo dos panios não exibem a poarte grafica
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        # linha a baixo não exibe o processo de abrir o navegador executa somente por baixo dos panos
        options=options
    )

    driver.get('https://economia.uol.com.br/cotacoes/bolsas/')
    # time.sleep(3)

    companys = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
    values = list()
    date_hour = list()

    for company in companys:
        input_busca = driver.find_element(By.ID, 'filled-normal')
        input_busca.send_keys(company)
        time.sleep(1)
        input_busca.send_keys(Keys.ENTER)

        time.sleep(1)
        span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
        cotacao_valor = span_val.text

        values.append(cotacao_valor)
        date_hour.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

        # print(f'Valor da cotação da {company}: {cotacao_valor}')

    # print(companys)
    # print(values)
    # print(date_hour)

    dados = {
        'empresa': companys,
        'valor': values,
        'data_hora': date_hour
    }

    return dados

def create_csv(dados, file_namw):

    # df significa dataframe
    df_empresas = pd.DataFrame(dados)
    df_empresas.to_csv(file_namw, index=False)

dados = get_dados()
create_csv(dados, 'empresas_ações.csv')

# input('')