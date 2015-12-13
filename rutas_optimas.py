#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *
from heapq import *
from grafo import *
from collections import defaultdict


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def calcular_comodidad(inicio, fin, rutas, ciudades):
    """Devuelve el puntaje heuristico de las ciudad pasada por parametro"""
    try: 
        embotellamientos = (ciudades[inicio].habitantes + ciudades[fin].habitantes) / (rutas[min(inicio,fin)][max(inicio,fin)][0].distancia)
        felicidad = (0.0 + rutas[min(inicio,fin)][max(inicio,fin)][0].puntaje) / (ciudades[inicio].habitantes + ciudades[fin].habitantes)
        return (felicidad / embotellamientos)
    except:
        #print "ERROR"
        return 0

def ordenar_rutas_comodidad(rutas, ciudades):
	comodidad = []
	for ciudad1 in ciudades.keys():
		for ciudad2 in ciudades.keys():
			if (ciudad2 >= ciudad1):
				break
			if (len(rutas[ciudad2][ciudad1]) > 0):
				heappush(comodidad, (calcular_comodidad(ciudad1,ciudad2, rutas, ciudades), ciudad1, ciudad2))
	return comodidad


def obtener_rutas_optimas(rutas, ciudades):
	comodidad = ordenar_rutas_comodidad(rutas, ciudades) #Comodidad de la ruta directa
	
	rutas_optimas = defaultdict(lambda: defaultdict(list)) #Listas con rutas optimas, a ordenarse mediante heapq

	visitados = []
	ciudades_visitadas = 0
	rutas_por_ciudad = defaultdict(int)
	rutas_agregadas = 0
	rutas_totales = len(comodidad)
	ciudades_totales = len( ciudades.keys() )

	#print len(comodidad)

	grafo_opt = Grafo([])

	while ( ciudades_visitadas < ciudades_totales ) or (rutas_agregadas < (rutas_totales/8)):
		ruta_actual = heappop(comodidad)
		ciudad1 = min(ruta_actual[1], ruta_actual[2])
		ciudad2 = max(ruta_actual[1], ruta_actual[2])
		#print "Agregando", ciudad1, "y", ciudad2
		arbol_temp = set([ciudad1, ciudad2])
		arbol_total = set([ciudad1, ciudad2])
		visitados_temp = []
		for arbol in visitados:
			if (ciudad1 in arbol) or (ciudad2 in arbol):
				arbol_temp = arbol_temp.union(arbol)
			else:
				visitados_temp.append(arbol)
			arbol_total = arbol_total.union(arbol)
		visitados_temp.append(arbol_temp)
		ciudades_visitadas = len(arbol_total)
		visitados = visitados_temp

		#print len(arbol_total)
		#print len(rutas[ciudad1][ciudad2])
		if len(rutas[ciudad1][ciudad2]) == 0:
			continue
		grafo_opt.agregar_aristas([rutas[ciudad1][ciudad2][0].ciudades()])

		rutas_optimas[ciudad1][ciudad2] = rutas[ciudad1][ciudad2]
		rutas_agregadas += 1
		rutas_por_ciudad[ciudad1] += 1
		rutas_por_ciudad[ciudad2] += 1



	print "\t" + bcolors.OKGREEN + bcolors.BOLD, rutas_agregadas, "rutas seleccionadas de", rutas_totales, "totales." + bcolors.ENDC
	return rutas_optimas, grafo_opt



			








