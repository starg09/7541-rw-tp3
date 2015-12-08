#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Ciudad(object):
    """Vertice del Grafo, modelado con los datos de una ciudad"""
    def __init__(self, nro_id, nombre, longitud, latitud, provincia, habitantes):
        self.id = nro_id                # Un integer
        self.nombre = nombre            # Un string
        self.longitud = longitud        # Un float
        self.latitud = latitud          # Un float
        self.provincia = provincia      # Un integer
        self.habitantes = habitantes    # Un integer    
    
    def coordenadas(self):
        """Devuelve una tupla (longitud, latitud)"""
        return (self.longitud, self.latitud)


class Ruta(object):
    """Almacena el puntaje y distancia de una ruta entre dos ciudades."""
    def __init__(self, nro_id, id_ciudad1, id_ciudad2, puntaje, distancia):
        self.id = nro_id                # Un integer
        self.id_ciudad1 = id_ciudad1    # Un integer
        self.id_ciudad2 = id_ciudad2    # Un integer
        self.puntaje = puntaje          # Un integer
        self.distancia = distancia      # Un float

    def ciudades(self):
        """Devuelve una tupla, con las ciudades que une (ciudad1, ciudad2)"""
        return (self.id_ciudad1, self.id_ciudad2)

    def __cmp__(self,otro):
        """Funcion de comparacion entre rutas"""
        if self.distancia < otro.distancia:
            return -1
        if self.distancia > otro.distancia:
            return 1
        return 0