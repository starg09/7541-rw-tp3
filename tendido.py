#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *

def prim(inicio, rutas, ciudades):

    mst = set() # Conjunto de truplas con ciudades, su distancia minima, y la ruta mas corta con su padre.
    por_visitar = [] # Conjunto de truplas a visitar, de mismo formato a las de mst.
    visitados = set() # Set con ciudades ya visitadas. (Solo el id)
    heappush(por_visitar, (0,inicio, NULL))
    while (len(por_visitar) != 0) and (len(mst) < len(ciudades.keys())):
        actual = heappop(por_visitar)
        if (actual[1] not in visitados):
            union(visitados,set(actual[1]))
            union(mst, set(actual))
            for id_vecino, ruta in rutas[actual[1]]:
                if (id_vecino not in visitados):
                    heappush(por_visitar, (ruta.distancia, id_vecino, ruta))
                
    return mst


