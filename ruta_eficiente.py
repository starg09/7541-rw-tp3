#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def puntaje_heuristico(inicio, fin, rutas, ciudades):
    """Devuelve el puntaje heuristico de las ciudad pasada por parametro"""
    
def reconstruir_camino(predecesores, actual):
    camino_final = [actual]
    while actual in predecesores:
        actual = predecesores[actual]
        camino_final.append(actual)
    return camino_final
    
def camino_minimo(inicio, fin, rutas, ciudades):
    """Devuelve una lista con el camino mas corto y de menor coste entre inicio y fin (ambas ciudades de nuestro grafo)
    Pre: inicio, fin son las IDs de las ciudades; rutas es un diccionario con objetos Ruta (rutas[id_ciudad1][id_ciudad2]), y ciudades es un diccionario con objetos Ciudad (ciudades[id_ciudad])
    Post: se devolvio una lista con los id_ciudad de las ciudades que conforman el camino minimo en orden (inicio -> .... -> fin)
    """

    visitados = set()  #Conjunto de ciudades visitadas (sus IDs)  
    por_visitar = []   #Min-heap con tuplas (puntaje_f, id_ciudad) donde la prioridad estara dada por puntaje_f
    predecesores = {}  #Diccionario con formato {"id_ciudad" : "id_predecesor"}
    puntaje_g = {}     #Diccioneario donde se guardaran los puntajes g
    puntaje_f = {}     #Diccioneario donde se guardaran los puntajes f

    for id_ciudad, ciudad in ciudades:
        puntaje_g[id_ciudad] = -1  #En vez de infinito ponemos -1
        puntaje_f[id_ciudad] = -1  #En vez de infinito ponemos -1   
    puntaje_g[inicio] = 0
    puntaje_f[inicio] = puntaje_heuristico(inicio, fin, rutas, ciudades)
    heappush(por_visitar, (puntaje_f[inicio], inicio))
    while (len(por_visitar) != 0):
        actual := heappop(por_visitar)
        if actual[1] = fin
            return reconstruir_camino(predecesores, fin) 
        visitados.union(set(actual)) 
        for id_vecino, ruta in rutas[actual]: 
            if id_vecino in visitados	
                continue
            puntaje_g_parcial = puntaje_g[actual] + rutas[actual][id_vecino].distancia
            else if puntaje_g_parcial >= puntaje_g[id_vecino] 
                continue
            predecesores[id_vecino] = actual
            puntaje_g[id_vecino] = puntaje_g_parcial
            puntaje_f[id_vecino] = puntaje_g[id_vecino] + puntaje_heuristico(id_vecino, fin, rutas, ciudades)
            heappush(por_visitar, (puntaje_f[id_vecino], id_vecino))

    return None