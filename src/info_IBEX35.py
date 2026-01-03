import yfinance
import pandas

# Definir el rango de fechas
start_date = '2020-01-01'
end_date = '2022-02-26'

# Descargar los datos del IBEX 35
ibex = yfinance.download('IBEX.MC', start=start_date, end=end_date)

# Añadir una columna con la fecha de cada día
ibex['Fecha'] = ibex.index

# Volcar los datos en un fichero CSV
ibex.to_csv('tests/data/ibex35.csv', index=False)

# Obtener las empresas que componen el IBEX 35
empresas_ibex = [
    'BBVA.MC', 'BCO.MC', 'CASH.MC', 'DIA.MC', 'EDF.MC', 'ENGI.MC', 'FCC.MC', 'IAG.MC',
    'ICAG.MC', 'IBE.MC', 'INDITEX.MC', 'ITX.MC', 'MRO.MC', 'POWR.MC', 'REE.MC', 'SAB.MC',
    'SAN.MC', 'SANTANDER.MC', 'TEF.MC', 'VIS.MC'
]

# Crear un DataFrame vacío para almacenar los datos
df_empresas = pandas.DataFrame(columns=['Empresa', 'Valor', 'Fecha'])

# Iterar sobre las empresas y descargar los datos
for empresa in empresas_ibex:
    datos_empresa = yfinance.download(empresa, start=start_date, end=end_date)['Close']
    for elemento in datos_empresa:
        df_empresa = pandas.DataFrame({'Fecha': elemento.index, 'empresa': empresa, 'Valor': elemento.values})
        df_empresas = pandas.concat([df_empresas, df_empresa])

# Volcar los datos en un fichero CSV
df_empresas.to_csv('tests/data/empresas_ibex35.csv', index=False)

print(df_empresas)
