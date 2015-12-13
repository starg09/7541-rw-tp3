#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from estructuras import *
from heapq import *


def puntaje_heuristico(inicio, fin, rutas, ciudades):
    """Devuelve el puntaje heuristico de las ciudad pasada por parametro"""
    return 0
    
def reconstruir_camino(predecesores, actual):
    camino_final = [actual]
    while actual in predecesores.keys():
        actual = predecesores[actual]
        camino_final.insert(0, actual)
    return camino_final
    
def camino_minimo(inicio, fin, rutas, ciudades, grafo):
    """Devuelve una lista con el camino mas corto y de menor coste entre inicio y fin (ambas ciudades de nuestro grafo)
    Pre: inicio, fin son las IDs de las ciudades; rutas es un diccionario con objetos Ruta (rutas[id_ciudad1][id_ciudad2]), y ciudades es un diccionario con objetos Ciudad (ciudades[id_ciudad])
    Post: se devolvio una lista con los id_ciudad de las ciudades que conforman el camino minimo en orden (inicio -> .... -> fin) o None si no hay ciudades
    """

    visitados = set()  #Conjunto de ciudades visitadas (sus IDs)  
    por_visitar = []   #Min-heap con tuplas (puntaje_f, id_ciudad) donde la prioridad estara dada por puntaje_f
    predecesores = {}  #Diccionario con formato {"id_ciudad" : "id_predecesor"}
    puntaje_g = {}     #Diccioneario donde se guardaran los puntajes g
    puntaje_f = {}     #Diccioneario donde se guardaran los puntajes f

    for id_ciudad, ciudad in ciudades.iteritems():
        puntaje_g[id_ciudad] = float("inf")
        puntaje_f[id_ciudad] = float("inf")   
    puntaje_g[inicio] = 0.0
    puntaje_f[inicio] = puntaje_heuristico(inicio, fin, rutas, ciudades)
    heappush(por_visitar, (puntaje_f[inicio], inicio))
    while (len(por_visitar) != 0):
        actual = heappop(por_visitar)
        if actual[1] == fin:
            return reconstruir_camino(predecesores, fin) 
        visitados = visitados.union([actual[1]])
        #print grafo._grafo[actual[1]]
        for id_vecino in grafo._grafo[actual[1]]:
            if id_vecino in visitados:
                #print "SALTEO 1 (Ciudad ya visitada, evitando ciclo)"
                continue
            try:
                puntaje_g_parcial = puntaje_g[actual[1]] + rutas[min(actual[1], id_vecino)][max(actual[1], id_vecino)][0].distancia
            except:
                #print "SALTEO 2 (Ruta Inexistente)"
                continue
            
            #print puntaje_g_parcial, " vs ", puntaje_g[id_vecino]

            if puntaje_g_parcial >= puntaje_g[id_vecino]:
                #print "SALTEO 3"
                continue
            predecesores[id_vecino] = actual[1]
            puntaje_g[id_vecino] = puntaje_g_parcial
            puntaje_f[id_vecino] = puntaje_g[id_vecino] + puntaje_heuristico(id_vecino, fin, rutas, ciudades)
            #print actual[1], ": ", puntaje_f[id_vecino], " vs ", puntaje_g[id_vecino], " (", puntaje_heuristico(id_vecino, fin, rutas, ciudades), ")"
            heappush(por_visitar, (puntaje_f[id_vecino], id_vecino))

    print "ERROR: Ruta no encontrada ( Dist.:", puntaje_g[actual[1]], ")"
    return None