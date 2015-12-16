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
	
	# Modulo de mejores rutas
	char = si_o_no(bcolors.WARNING + bcolors.BOLD + "\n\n¿Calcular mejor ruta entre un par de ciudades?\n" + bcolors.ENDC + "\t(Todas las rutas vs rutas optimas)\n" + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
	while not(char in ["n", "N"]):
		if char in ["s", "S"]:
			ciudades_validas = False
			while not(ciudades_validas):
				try:
					id1 = int(raw_input("\nIngrese ID de Ciudad nro. 1: "))
					id2 = int(raw_input("\nIngrese ID de Ciudad nro. 2: "))
					ciudades_validas = True
				except:
					char = si_o_no(bcolors.FAIL + bcolors.BOLD + "\n\nERROR: ID no válido. ¿Desea intentar nuevamente?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
					if (char in ["n", "N"]):
						ciudades_validas = True #No son validas, pero así cierra el while, y lo siguiente no se cumple por el char.
		if char in ["s", "S"]:
			#print "\n\n\n", camino_minimo(id1, id2, rutas, ciudades, grafo), "vs", camino_minimo(id1, id2, rutas_opt, ciudades, grafo_opt), "\n"
			cam_min = camino_minimo(id1, id2, rutas_opt, ciudades, grafo_opt)
			print bcolors.OKGREEN + bcolors.BOLD + "\n\n\nMejor Ruta Encontrada entre ciudades", str(id1), "y", str(id2) + ": " + bcolors.ENDC + str(cam_min), "\n"
			char = si_o_no(bcolors.BOLD + "\n\n¿Desea guardar un archivo KML con la ruta?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
			if char in ["s", "S"]:
				exportar_ruta_a_kml(ciudades, rutas_opt, grafo_opt, id1, id2)

			char = si_o_no(bcolors.BOLD + "\n\n¿Desea buscar otra ruta diferente?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)



	char = si_o_no(bcolors.WARNING + bcolors.BOLD + "\n\n¿Buscar mejor tendido para el cableado electrico?\n" + bcolors.ENDC + bcolors.HEADER + "\t[sS/nN]\n\t" + bcolors.ENDC)
	if char in ["s", "S"]:
		mejor_tendido = calcular_tendido_minimo_electrico(rutas_opt, ciudades)
		print bcolors.OKGREEN + bcolors.BOLD + "\n\nMejor tendido encontrado:", bcolors.ENDC + str(mejor_tendido), "\n\n\n"
		exportar_tendido_a_kml(ciudades, rutas_opt, grafo_opt, mejor_tendido)


main()