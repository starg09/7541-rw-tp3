#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *
from ruta_eficiente import *
import os

def exportar_ruta_a_kml(ciudades, rutas, grafo, id_ciudad1, id_ciudad2):

	if (None in [ciudades, rutas, grafo]):
		return None

	if not os.path.exists("./Archivos_KML/"):
		os.makedirs("./Archivos_KML/")

	ruta_ideal = camino_minimo(id_ciudad1, id_ciudad2, rutas, ciudades, grafo)

	f = open("./Archivos_KML/ruta_" + str(id_ciudad1) + "_" + str(id_ciudad2) + ".kml", "w")

	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	f.write("<kml xmlns=\"http://earth.google.com/kml/2.1\">\n")
	f.write("<Document>\n")
	f.write("\t<name>" + "Ruta desde" + ciudades[id_ciudad1].nombre + "hasta" + ciudades[id_ciudad2].nombre + ".kml" +"</name>\n")

	for idc in range(0, len(ruta_ideal)):
		f.write("\t<Placemark>\n")
		f.write("\t\t<name>" + ciudades[ruta_ideal[idc]].nombre + "</name>\n")
		f.write("\t\t<description>" + "Habitantes: " + str(ciudades[ruta_ideal[idc]].habitantes) + "</description>\n")
		f.write("\t\t<Point>\n")
		f.write("\t\t\t<coordinates>" + str(ciudades[ruta_ideal[idc]].longitud) + ", " + str(ciudades[ruta_ideal[idc]].latitud) + "</coordinates>\n")
		f.write("\t\t</Point>\n")
		f.write("\t</Placemark>\n")

	for idc in range(0, len(ruta_ideal)-1):
		f.write("\t<Placemark>\n")
		f.write("\t\t<LineString>\n")
		f.write("\t\t\t<coordinates>" + str(ciudades[ruta_ideal[idc]].longitud) + ", " + str(ciudades[ruta_ideal[idc]].latitud) + " " + str(ciudades[ruta_ideal[idc + 1]].longitud) + ", " + str(ciudades[ruta_ideal[idc + 1]].latitud) + "</coordinates>\n")
		f.write("\t\t</LineString>\n")
		f.write("\t</Placemark>\n")

	f.write("</Document>\n")
	f.write("</kml>\n")

	f.close()

	print "\n\n\tArchivo creado en \"./Archivos_KML/ruta_" + str(id_ciudad1) + "_" + str(id_ciudad2) + ".kml\"\n"


def exportar_conexiones_a_kml(ruta, ciudades, conexiones):

	if (None in [ruta, ciudades, conexiones]):
		return None

	if not os.path.exists("./Archivos_KML/"):
		os.makedirs("./Archivos_KML/")

	f = open("./Archivos_KML/" + ruta, "w")

	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	f.write("<kml xmlns=\"http://earth.google.com/kml/2.1\">\n")
	f.write("<Document>\n")
	f.write("\t<name>" + "Cableado Eléctrico de Tendido Mínimo.kml" +"</name>\n")

	for id_ciudad in ciudades.keys():
		f.write("\t<Placemark>\n")
		f.write("\t\t<name>" + ciudades[id_ciudad].nombre + "</name>\n")
		f.write("\t\t<description>" + "Habitantes: " + str(ciudades[id_ciudad].habitantes) + "</description>\n")
		f.write("\t\t<Point>\n")
		f.write("\t\t\t<coordinates>" + str(ciudades[id_ciudad].longitud) + ", " + str(ciudades[id_ciudad].latitud) + "</coordinates>\n")
		f.write("\t\t</Point>\n")
		f.write("\t</Placemark>\n")

	for par in conexiones:
		f.write("\t<Placemark>\n")
		f.write("\t\t<LineString>\n")
		f.write("\t\t\t<coordinates>" + str(ciudades[par[0]].longitud) + ", " + str(ciudades[par[0]].latitud) + " " + str(ciudades[par[1]].longitud) + ", " + str(ciudades[par[1]].latitud) + "</coordinates>\n")
		f.write("\t\t</LineString>\n")
		f.write("\t</Placemark>\n")

	f.write("</Document>\n")
	f.write("</kml>\n")

	f.close()

	print "\tArchivo creado en \"" + ruta + "\""