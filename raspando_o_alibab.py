from bs4 import BeautifulSoup
import requests
import email.message
import smtplib
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import pyautogui
import pandas as pd 
from matplotlib import pyplot as plt
import tabula



URLDOLARGOOGLE = 'https://www.google.com/search?q=d%C3%B3lar&rlz=1C1SQJL_pt-BRBR811BR811&oq=D%C3%93LAR&aqs=chrome.0.69i59j35i39j0i433i512l6j0i131i433i512j0i512.2545j0j7&sourceid=chrome&ie=UTF-8'

cabeçalho = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

site = requests.get(URLDOLARGOOGLE, headers=cabeçalho)

soup = BeautifulSoup(site.content, 'html.parser')

dolar = float(soup.find('span', class_= "DFlfde SwHCTb").get_text().strip().replace(',',''))/100

dolarwhats = str(f'Cotação em Reais atual do dólar: {dolar}')

print(f'Dólar hoje: {dolar}')

#print(soup.prettify())

URLALIBABA = 'https://www.alibaba.com/product-detail/Wholesale-Solar-Power-Bank-80000mah-10000mah_1600140783650.html?spm=a2700.12243863.0.0.2ce82568m4BbmH'

CABEÇALHO = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

SITE = requests.get(URLALIBABA, headers=CABEÇALHO)

SOUP = BeautifulSoup(SITE.content, 'html.parser')

FORNECEDOR = float(str(SOUP.find('div', class_='sku-price__sku-price-item').get_text().strip().replace(',','')[1:5]))

print(f'Preço do Enguia: {FORNECEDOR}')

fornecedorwhats = str(f'Preço do Enguia em dólares: {FORNECEDOR}')

frete_china = 29.70
icms_social = 1
icms = 118/100
entrega = 0.51
lucro = 150/100
preço_de_conversão = dolar * FORNECEDOR
enguiareais = str(f'O preço do Enguia em Reais és: {preço_de_conversão:.2f}')


  
preço_com_imp = ((preço_de_conversão * icms) + entrega + icms_social + frete_china)
imposto = f'O preço de custo do produto (já incluindo o ICMS, a correção monetária, entrega internacional, frete e apenas faltando o custo aduaneiro) és de {preço_com_imp:,.2f} Reais'
preço_de_venda = float(preço_com_imp * lucro)
sale = f'O preço de venda do produto és de {(preço_com_imp * lucro):,.2f} Reais'
luc = f'{preço_de_venda - preço_com_imp:.2f} Reais de lucro por produto'
frete_inter = f'Frete internacional incidente por produto: {frete_china} Reais'


navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements_by_id('side')) < 1:
  time.sleep(1)

numw =  [5511988016162, 5511994083095]

for enviar in numw:
  texto = urllib.parse.quote(dolarwhats)
  texto1 = urllib.parse.quote(fornecedorwhats)
  texto2 = urllib.parse.quote(enguiareais)  
  texto3 = urllib.parse.quote(imposto)
  texto4 = urllib.parse.quote(sale)
  texto5 = urllib.parse.quote(luc)
  texto6 = urllib.parse.quote(frete_inter)


  link = f'https://web.whatsapp.com/send?phone={enviar}&text={texto, texto1, texto2, texto3, texto4, texto6, texto5}'
  navegador.get(link)

  while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)
  time.sleep(10)
  
  pyautogui.moveTo(1015, 669)
  pyautogui.click()
  time.sleep(10)
  #navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_Keys(Keys.ENTER)
  




