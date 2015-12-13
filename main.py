#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from carga_archivos import *
from ruta_eficiente import *
from rutas_optimas import *
from tendido import *

def main():
	ciudades = cargar_ciudades("/home/starg09/Desktop/GitHub/7541-rw-tp3/Archivos/ciudades.csv")
	rutas, grafo = cargar_rutas("/home/starg09/Desktop/GitHub/7541-rw-tp3/Archivos/rutas.csv", ciudades)
	rutas_opt, grafo_opt = obtener_rutas_optimas(rutas, ciudades)
	

	s = ""
	while (s not in ["s", "S", "n", "N"]):
		s = raw_input("¿Calcular mejores rutas entre cada par de ciudades? (Todas las rutas vs rutas optimas)\n[sS/nN]\n")
	if s in ["s", "S"]:
		for id1 in ciudades.keys():
		 	for id2 in ciudades.keys():
		 		if (id1 != id2):
		 			print camino_minimo(id1, id2, rutas, ciudades, grafo), "vs", camino_minimo(id1, id2, rutas_opt, ciudades, grafo_opt)


	s = ""
	while (s not in ["s", "S", "n", "N"]):
		s = raw_input("¿Buscar mejor tendido para el cableado electrico?\n[sS/nN]\n")
	if s in ["s", "S"]:
		print "Mejor tendido encontrado:", calcular_tendido_minimo_electrico(rutas_opt, ciudades)


main()