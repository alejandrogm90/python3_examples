#!/usr/bin/env python3
#
#
#       Copyright 2026 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
