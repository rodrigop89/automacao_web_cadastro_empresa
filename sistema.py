# Funções que o programa executa

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from dados import email, senha, url
from identificadores_pagina import (area_atuacao, botao_cadastrar,
                                    botao_entrar, campo_email, campo_senha,
                                    cnpj_empresa, data_fundacao, email_empresa,
                                    endereco_empresa, nome_empresa,
                                    numero_funcionarios, telefone_empresa)
from planilha import tabela

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(12)


def abre_navegador():
    driver.get(url)
    time.sleep(3)


def login():
    driver.find_element(By.XPATH, campo_email).send_keys(email)
    time.sleep(2)
    driver.find_element(By.XPATH, campo_senha).send_keys(senha)
    time.sleep(2)
    driver.find_element(By.XPATH, botao_entrar).click()


def preencher_planilha():
    for indice, linha in tabela.iterrows():
        driver.find_element(By.ID, nome_empresa).send_keys(
            linha['Nome da Empresa'])
        time.sleep(1)
        driver.find_element(By.ID, email_empresa).send_keys(linha['Email'])
        time.sleep(1)
        driver.find_element(By.ID, telefone_empresa).send_keys(
            linha['Telefone'])
        time.sleep(1)
        driver.find_element(By.ID, endereco_empresa).send_keys(
            linha['Endereço'])
        time.sleep(1)
        driver.find_element(By.ID, cnpj_empresa).send_keys(linha['CNPJ'])
        time.sleep(1)
        driver.find_element(By.ID, area_atuacao).send_keys(
            linha['Área de Atuação'])
        time.sleep(1)
        driver.find_element(By.ID, numero_funcionarios).send_keys(
            linha['Quantidade de Funcionários'])
        time.sleep(1)
        driver.find_element(By.ID, data_fundacao).send_keys(
            linha['Data de Fundação'])
        time.sleep(1)
        driver.find_element(By.XPATH, botao_cadastrar).click()
        time.sleep(3)
