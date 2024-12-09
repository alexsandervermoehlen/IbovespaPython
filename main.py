import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')
# time.sleep(3)

companys = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
values = list()
date_hour = list()

for company in companys:
    input_busca = driver.find_element(By.ID, 'filled-normal')
    input_busca.send_keys(company)
    time.sleep(2)
    input_busca.send_keys(Keys.ENTER)

    time.sleep(1)
    span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
    cotacao_valor = span_val.text

    values.append(cotacao_valor)
    date_hour.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    # print(f'Valor da cotação da {company}: {cotacao_valor}')

print(companys)
print(values)
print(date_hour)

input('')