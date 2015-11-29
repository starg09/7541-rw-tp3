from estructuras import *

def parsear_ciudad(linea):
	"""
	Lee una linea del archivo de ciudades, separa los campos, y devuelve un objeto armado.
	"""
	campos = linea.split("	")
	nueva_ciudad = new Ciudad(campos[0], campos[1], campos[2], campos[3], campos[4], campos[5])
	return nueva_ciudad


def parsear_ruta(linea):
	"""
	Lee una linea del archivo de rutas, separa los campos, y devuelve un objeto armado.
	"""
	campos = linea.split("	")
	nueva_ruta = new Ruta(campos[0], campos[1], campos[2], campos[3], campos[4])
	return nueva_ruta