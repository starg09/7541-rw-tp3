from collections import defaultdict

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
    def __init__(self, nro_id, id_ciudad1, id_ciudad2, distancia, puntaje):
        self.id = nro_id                # Un integer
        self.id_ciudad1 = id_ciudad1    # Un integer
        self.id_ciudad2 = id_ciudad2    # Un integer
        self.distancia = distancia      # Un integer
        self.puntaje = puntaje          # Un float
    
    def ciudades(self):
        """Devuelve una tupla, con las ciudades que une (ciudad1, ciudad2)"""
        return (self.ciudad1, self.ciudad2)
