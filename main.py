#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from carga_archivos import *
from ruta_eficiente import *
from rutas_optimas import *
from tendido import *
from kml import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def si_o_no(mensaje):
	char = ""
	while (char not in ["s", "S", "n", "N"]):
		char = raw_input(mensaje)
	return char

def main():
	ciudades = cargar_ciudades("./Archivos/ciudades.csv")
	rutas, grafo = cargar_rutas("./Archivos/rutas.csv", ciudades)
	print "\n"
	rutas_opt, grafo_opt = obtener_rutas_optimas(rutas, ciudades)
	
	print bcolors.OKGREEN + bcolors.BOLD + "\n\nRed Optimizada creada.\n\n" + bcolors.ENDC

	conexiones_red_opt = []
	for ciudad_1 in grafo_opt._grafo.keys():
		for ciudad_2 in grafo_opt._grafo[ciudad_1]:
			if (ciudad_1 < ciudad_2):
				break
			conexiones_red_opt.append((ciudad_2, ciudad_1))

	exportar_conexiones_a_kml("red.kml", ciudades, conexiones_red_opt)


	mejor_tendido = calcular_tendido_minimo_electrico(rutas_opt, ciudades)
	print bcolors.OKGREEN + bcolors.BOLD + "\n\nRéd electrica de tendido minimo encontrada.\n\n" + bcolors.ENDC
	exportar_conexiones_a_kml("tendido.kml", ciudades, mejor_tendido)
	print ""

	cam_min = None
	while (cam_min == None):
		ciudades_validas = False
		id1 = -1
		id2 = -1
		while (not(ciudades_validas)):
			try:
				id1 = int(raw_input("\nIngrese ID de Ciudad nro. 1: "))
				if not(1 <= id1 <= len(ciudades.keys())):
					raise ValueError
				id2 = int(raw_input("\nIngrese ID de Ciudad nro. 2: "))
				if not(1 <= id2 <= len(ciudades.keys())):
					raise ValueError
				ciudades_validas = True
			except:
				char = si_o_no(bcolors.FAIL + bcolors.BOLD + "\n\nERROR: ID no válido. ¿Desea intentar nuevamente?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
				if (char in ["n", "N"]):
					ciudades_validas = True #No son validas, pero así cierra el while, y lo siguiente no se cumple por el char.

		if not( (id1 < 0) or (id2 < 0) ):
			cam_min = camino_minimo(id1, id2, rutas_opt, ciudades, grafo_opt)
			if (cam_min != None):
				print bcolors.OKGREEN + bcolors.BOLD + "\n\nMejor Ruta Encontrada entre ciudades", str(id1), "y", str(id2) + ": " + bcolors.ENDC + str(cam_min), ""
				exportar_ruta_a_kml(ciudades, rutas_opt, grafo_opt, id1, id2)
				print ""
			else:
				char = si_o_no(bcolors.FAIL + bcolors.BOLD + "\n\nERROR: No se encontró ninguna ruta válida entre esas ciudades. (Esto no debería suceder)\n\t¿Desea intentar nuevamente?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
				if (char in ["n", "N"]):
					cam_min = True #No son validas, pero así cierra el while, y lo siguiente no se cumple por el char.
		else:
			cam_min = True
	




main()