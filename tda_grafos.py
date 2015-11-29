from collections import defaultdict


class Grafo_mapa(object):

    class _Ciudad(object):
        """Vertice del Grafo, modelado con los datos de una ciudad"""
        def __init__(self, id, nombre, longitud, latitud, provincia, habitantes):
            self.id = id
            self.nombre = nombre
            self.longitud = longitud
            self.latitud = latitud
            self.provincia = provincia
            self.habitantes = habitantes
        
        def obtener_id_ciudad(self):
            """Devuelve el id de la ciudad"""
            return self.id

        def obtener_nombre_ciudad(self):
            """Devuelve el nombre de la ciudad"""
            return self.nombre

        def obtener_coordenadas_ciudad(self):
            """Devuelve una tupla (longitud, latitud)"""
            return (self.longitud, self.latitud)

        def obtener_provincia_ciudad(self):
            """Devuelve el numero de provincia de la ciudad"""
            return self.provincia

        def obtener_habitantes_ciudad(self):
            """Devuelve la cantidad de habitantes de la ciudad"""
            return self.habitantes
    
    class _Ruta(object):
        """Arista del Grafo, modelada con los datos de una ruta"""
        def __init__(self, id, ciudad1, ciudad2, distancia, puntaje):
            self.id = id
            self.ciudad1 = ciudad1
            self.ciudad2 = ciudad2
            self.distancia = distancia
            self.puntaje = puntaje
        
        def obtener_id_ruta(self):
            """Devuelve el id de la ruta"""
            return self.id

        def obtener_ciudades_ruta(self):
            """Devuelve una tupla, con las ciudades que une (ciudad1, ciudad2)"""
            return (ciudad1, ciudad2)

        def obtener_distancia_ruta(self):
            """Devuelve la distancia abarcada por la ruta"""
            return self.distancia

        def obtener_puntaje_ruta(self):
            """Devuelve el puntaje de la ruta"""
            return self.puntaje
        
    def __init__(self, )
