import os.path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import common_functions as cf

if __name__ == '__main__':
    TARGET_FOLDER = "~/Bolsa"
    # URL de la página oficial de la Bolsa de Madrid
    url = ('https://www.bolsasymercados.es/bme-exchange/es/Mercados-y-Cotizaciones/Acciones/Mercado-Continuo/Precios/'
           'ibex-35-ES0SI0000005')

    # Configurar el navegador
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Modo headless
    driver = webdriver.Chrome(options=options)

    # Cargar la página
    driver.get(url)

    # Esperar a que la página se cargue
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))

    # Encontrar la tabla con los datos financieros
    tabla = driver.find_elements(By.TAG_NAME, 'tbody')
    tabla = tabla[len(tabla) - 1]

    # Extraer los datos financieros de la tabla
    datos = []
    for fila in tabla.find_elements(By.TAG_NAME, 'tr')[1:]:
        cols = fila.find_elements(By.TAG_NAME, 'td')
        datos.append([col.text.strip() for col in cols])

    # Crear un DataFrame con los datos financieros
    columnas = ['Nombre', 'Último', '% Dif', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo (miles €)', 'Fecha', 'Hora']
    df = pd.DataFrame(datos, columns=columnas)

    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
    # Volcar los datos en un fichero CSV
    df.to_csv(f'{TARGET_FOLDER}/info_Ibex35_{cf.get_date()}.csv', index=False)

    # Cerrar el navegador
    driver.quit()
