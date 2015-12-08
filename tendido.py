#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *

def prim(inicio, rutas, ciudades):
    mst = set()
    por_visitar = []
    visitados = set(inicio)
    heappush(por_visitar, (0,inicio))
    while (len(por_visitar) != 0):
        actual = heappop(por_visitar)
        if (actual[1] not in visitados):
            union(visitados,set(actual[1]))
            union(mst, set(actual))
            for id_vecino, rutas in rutas[actual[1]]:
                if (id_vecino not in visitados):
                    heappush(por_visitar, (rutas.distancia, id_vecino))
                
    return mst


