"""
teste_automatizado_com_selenium.py

Este script utiliza Selenium para automatizar:
- Abertura do Google
- Aceitação de cookies
- Busca de um termo
- Verificação se resultados foram encontrados
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Configuração inicial
driver = webdriver.Chrome()

def selecionar_clickar_escrever(elemento_id, texto):
    """
    Clica e escreve em um campo identificado por ID.

    Parâmetros:
    elemento_id (str): ID do elemento a ser localizado.
    texto (str): Texto a ser inserido no campo.
    """
    text = driver.find_element(By.ID, elemento_id)
    text.send_keys(texto)

driver.get("https://www.google.com")

# Aceitar cookies(se aparecer)
try:
    aceitar = driver.find_elements(By.XPATH, '//button[text()="Aceitar tudo"]')
    # aceitar.click()
# Ignora se o botão não existir
except NoSuchElementException:
    print("Botão de cookies não encontrado. Continuando...")

# Campo de pesquisa
campo_busca = driver.find_element(By.NAME, "q")
campo_busca.send_keys("Teste Automatizado com Selenium")
campo_busca.send_keys(Keys.RETURN)

# Manter o navegador aberto para inspeção
input("Pressione Enter para fechar o navegador...")


# Verificar se há resultados
resultados = driver.find_elements(By.CSS_SELECTOR, "div.g")

if resultados:
    print(f"Teste passou!{len(resultados)} resultados encontrados.")
else:
    print("Teste falou! Nenhum resultado encontrado foi encontrado.")

# Fechar o navegador
driver.quit()
