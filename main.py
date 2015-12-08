from carga_archivos import *
from ruta_eficiente import *

def main():
	ciudades = cargar_ciudades("/home/starg09/Desktop/GitHub/7541-rw-tp3/Archivos/ciudades.csv")
	rutas, grafo = cargar_rutas("/home/starg09/Desktop/GitHub/7541-rw-tp3/Archivos/rutas.csv", ciudades)
	print camino_minimo(13, 28, rutas, ciudades)

main()