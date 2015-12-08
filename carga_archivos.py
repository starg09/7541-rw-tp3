#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *
from parseo_csv import *
from grafo import *
from heapq import heappush
from collections import defaultdict

def cargar_ciudades(ruta_archivo):
	"""
	Carga todas las ciudades en el csv dado, y devuelve un diccionario con los objetos Ciudad creados apropiadamente
	Si alguna ciudad carga erroneamente, devuelve None.
	"""
	archivo = open(ruta_archivo, "r")

	#Pasar la primer linea
	archivo.readline()
	linea = archivo.readline()
	
	ciudades = defaultdict(Ciudad)
	while not (linea == ""):
		nueva_ciudad = parsear_ciudad(linea)
		if (nueva_ciudad == None):
			del ciudades
			return None
		ciudades[nueva_ciudad.id] = nueva_ciudad
		linea = archivo.readline()
	archivo.close()

	return ciudades



def cargar_rutas(ruta_archivo, ciudades):
	"""
	Carga todas las rutas en el csv dado, y devuelve dos elementos: un diccionario con los objetos
	Ruta creados apropiadamente, y un grafo con todas las conexiones entre las ciudades. 

	Para acceder a un elemento de este diccionario, se debe buscar en la forma
	"rutas[ciudad_A][ciudad_B]", siendo ciudad_A la ciudad de menor ID.

	Si alguna ciudad carga erroneamente, la función devuelve None. También si una ruta tiene
	misma ciudad de llegada que de salida, o si la ciudad no se encuentra en la lista (creada
	previo a correr esta función)

	Pre: Ciudades se generó mediante cargar_ciudades, y es una lista valida.
	     ruta_archivo es una ruta valida.
	"""
	archivo = open(ruta_archivo, "r")

	#Pasar la primer linea
	archivo.readline()
	linea = archivo.readline()
	
	rutas = defaultdict(lambda: defaultdict(list))
	grafo = Grafo([])

	while not (linea == ""):
		nueva_ruta = parsear_ruta(linea)
		if (nueva_ruta is None) or (not(nueva_ruta.id_ciudad1 in ciudades)) or (not(nueva_ruta.id_ciudad2 in ciudades)):
			del rutas
			del grafo
			return None, None
		if (nueva_ruta.id_ciudad1 < nueva_ruta.id_ciudad2):
			heappush(rutas[nueva_ruta.id_ciudad1][nueva_ruta.id_ciudad2], nueva_ruta)
		else:
			heappush(rutas[nueva_ruta.id_ciudad2][nueva_ruta.id_ciudad1], nueva_ruta)

		grafo.agregar_aristas([nueva_ruta.ciudades()])

		linea = archivo.readline()
	archivo.close()
	
	# for ciudad1 in rutas:
	# 	for ciudad2, lista in rutas[ciudad1].iteritems():
	# 		print ciudad1, " - ", ciudad2, ": ", len(rutas[ciudad1][ciudad2])

	return rutas, grafo


