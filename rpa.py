import psycopg2
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.google.com/finance/quote/USD-BRL?sa=X&sqi=2&ved=2ahUKEwjHod2jweyEAxV4LrkGHTzSCNsQmY0JegQIDhAv")

time.sleep(5)

valor_element = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div")

valor_texto = valor_element.text.replace(',','.')

conexao_config = {
    'host': 'pg-90576f9-germinare-8711.e.aivencloud.com',
    'database': 'dbrpa',
    'user': 'avnadmin',
    'password': 'AVNS_5dJlXy00wwa8j288Qme',
    'port':'15864'
}

print(valor_texto)

conexao = psycopg2.connect(**conexao_config)

cursor = conexao.cursor()

consulta = f"CALL inserir_cotacao_dolar('{datetime.datetime.today().date()}', '{datetime.datetime.today().time()}', {float(valor_texto)})"

cursor.execute(consulta)

conexao.commit()

cursor.close()
conexao.close()

print(f"Inserido com sucesso\nData: {datetime.datetime.today().date()} - Hora:  {datetime.datetime.today().time()} - Valor {float(valor_texto)}")
