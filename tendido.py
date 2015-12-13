#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from estructuras import *
from heapq import *

def prim(inicio, rutas, ciudades):

    mst = set() # Conjunto de truplas con ciudades, su distancia minima, y la ruta mas corta con su padre.
    dist_total = 0
    por_visitar = [] # Conjunto de truplas a visitar, de mismo formato a las de mst.
    visitados = set() # Set con ciudades ya visitadas. (Solo el id)
    heappush(por_visitar, (0,inicio, None))
    while (len(por_visitar) != 0) and (len(mst) < len(ciudades.keys())):
        actual = heappop(por_visitar)
        if (actual[1] not in visitados):
            visitados = visitados.union(visitados,set([actual[1]]))
            mst = mst.union(mst, set(actual))
            for id_vecino in rutas[actual[1]]:
                if (id_vecino not in visitados):
                    ruta = rutas[actual[1]][id_vecino][0]
                    heappush(por_visitar, (ruta.distancia, id_vecino, ruta))
                    dist_total += ruta.distancia

    #print visitados
    #print mst
    return mst, dist_total

def buscar_padre(ciudad, padre):
    if padre[ciudad] != ciudad:
        return buscar_padre(padre[ciudad], padre)
    return ciudad

def unir_ramas(ciudad1, ciudad2, padre, nivel):
    padre1 = buscar_padre(ciudad1, padre)
    padre2 = buscar_padre(ciudad2, padre)
    if padre1 != padre2:
        if nivel[padre1] > nivel[padre2]:
            padre[padre2] = padre1
        else:
            padre[padre1] = padre2
            if nivel[padre1] == nivel[padre2]:
                nivel[padre2] += 1

def kruskal(rutas, ciudades):
    padre = {}
    nivel = {}
    for ciudad in ciudades.keys():
        padre[ciudad] = ciudad
        nivel[ciudad] = 0
    arbol = set()

    lista_rutas = []
    for ciudad1 in rutas:
        for ciudad2 in rutas[ciudad1]:
            if (ciudad1 !=ciudad2) and (len(rutas[min(ciudad1, ciudad2)][max(ciudad1, ciudad2)]) > 0):
                heappush(lista_rutas, (rutas[min(ciudad1, ciudad2)][max(ciudad1, ciudad2)][0].distancia, min(ciudad1, ciudad2), max(ciudad1, ciudad2)))

    for elemento in lista_rutas:
        dist, ciudad1, ciudad2 = elemento
        if buscar_padre(ciudad1, padre) != buscar_padre(ciudad2, padre):
            unir_ramas(ciudad1, ciudad2, padre, nivel)
            arbol.add((ciudad1, ciudad2))
    return list(arbol)





def calcular_tendido_minimo_electrico(rutas, ciudades):
    return kruskal(rutas, ciudades)
