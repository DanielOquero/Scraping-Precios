"""
Script que obtiene los precios sugeridos de la Cámara Argentina de Refrigeración

"""
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

# Obtener la página web

website = "https://www.camaraargentinaderefrigeracion.com/precios-sugeridos-2019-2020"
pagina = requests.get(website)                      # Hacer una solicitud GET a la página web
soup = BeautifulSoup(pagina.content, 'html.parser') # Crear un objeto BeautifulSoup
datos = soup.find_all("div", class_="ZTH0AF")       # Encontrar los datos en la página web

items = list()                                      # Crear una lista vacía para almacenar los datos

for i in datos:                                     
    items.append(i.get_text())                  # Agregar los datos a la lista filtrando solo texto

pares = {}                                      # Crear un diccionario vacío para almacenar los pares clave-valor      

for i in range(0, len(items), 2):               # Iterar sobre los elementos de la lista
    clave = items[i]                            # Obtener la clave
    valor = items[i + 1]                        # Obtener el valor
    pares [clave] = valor                       # Agregar el par clave-valor al diccionario

# Convertir el diccionario a una lista de listas
tabla = [[clave, valor] for clave, valor in pares.items()]

# Especificar los encabezados
encabezados = ["TRABAJO", "COSTO"]

# Imprimir la tabla
print(tabulate(tabla, headers=encabezados, tablefmt="pretty"))




