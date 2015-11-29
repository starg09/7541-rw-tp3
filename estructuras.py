from collections import defaultdict

class Ciudad(object):
    """Vertice del Grafo, modelado con los datos de una ciudad"""
    def __init__(self, nro_id, nombre, longitud, latitud, provincia, habitantes):
        self.id = nro_id
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.provincia = provincia
        self.habitantes = habitantes
    
    def id(self):
        """Devuelve el id de la ciudad"""
        return self.id

    def nombre(self):
        """Devuelve el nombre de la ciudad"""
        return self.nombre

    def coordenadas(self):
        """Devuelve una tupla (longitud, latitud)"""
        return (self.longitud, self.latitud)

    def provincia(self):
        """Devuelve el numero de provincia de la ciudad"""
        return self.provincia

    def habitantes(self):
        """Devuelve la cantidad de habitantes de la ciudad"""
        return self.habitantes

class Ruta(object):
    """Almacena el puntaje y distancia de una ruta entre dos ciudades."""
    def __init__(self, nro_id, id_ciudad1, id_ciudad2, distancia, puntaje):
        self.id = nro_id
        self.id_ciudad1 = id_ciudad1
        self.id_ciudad2 = id_ciudad2
        self.distancia = distancia
        self.puntaje = puntaje
    
    def id(self):
        """Devuelve el id de la ruta"""
        return self.id

    def ciudades(self):
        """Devuelve una tupla, con las ciudades que une (ciudad1, ciudad2)"""
        return (self.ciudad1, self.ciudad2)

    def distancia(self):
        """Devuelve la distancia abarcada por la ruta"""
        return self.distancia

    def puntaje(self):
        """Devuelve el puntaje de la ruta"""
            return self.puntaje