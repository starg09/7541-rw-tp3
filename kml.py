#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *

def exportar_ruta_a_kml(ciudades, id_ciudad1, id_ciudad2):

	f = open("ruta_" + id_ciudad1 + "_" + id_ciudad2 + ".kml", "w")

	f.write("<?xml version="1.0" encoding="UTF-8"?>\n")
	f.write("<kml xmlns="http://earth.google.com/kml/2.1">\n")
	f.write("<Document>\n")
	f.write("   <name>" + "Ruta desde" + ciudades[id_ciudad1].nombre + "hasta" + ciudades[id_ciudad2].nombre + ".kml" +"</name>\n")

	f.write("   <Placemark>\n")
    f.write("       <name>" + ciudades[id_ciudad1].nombre + "</name>\n")
    f.write("       <description>" + "Habitantes: " + ciudades[id_ciudad1].habitantes + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + ciudades[id_ciudad1].latitud + ", " + ciudades[id_ciudad1].longitud + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")

	f.write("   <Placemark>\n")
    f.write("       <name>" + ciudades[id_ciudad2].nombre + "</name>\n")
    f.write("       <description>" + "Habitantes: " + ciudades[id_ciudad2].habitantes + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + ciudades[id_ciudad2].latitud + ", " + ciudades[id_ciudad2].longitud + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")

	f.write("	<Placemark>\n")
    f.write("  		<LineString>\n")
    f.write("      		<coordinates>" + ciudades[id_ciudad1].latitud + ", " + ciudades[id_ciudad1].longitud + " " + ciudades[id_ciudad2].latitud + ", " + ciudades[id_ciudad2].longitud + "</coordinates>\n")
    f.write("       </LineString>\n")
    f.write("	</Placemark>\n")

	f.write("</Document>\n")
	f.write("</kml>\n")

	f.close()
