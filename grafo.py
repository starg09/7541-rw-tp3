from collections import defaultdict

import pprint
pp = pprint.PrettyPrinter(indent=4)


class Grafo(object):
	"""
	Estructura grafo. Se utiliza defaultdict para evitar tener que los campos se creen solo a medida que se necesita.

	"aristas" es una lista de tuplas entre nodos. Los nodos pueden nombrarse con un string o con un integer.
	"unsentido" establece si los las aristas tienen sentido o no. (Por defecto van en ambos sentidos)
	"""
	def __init__(self, aristas, unsentido=False):
		self._grafo = defaultdict(set)
		self._unsentido = unsentido
		self.agregar_arista(aristas)	

	def agregar_arista(self, aristas):
		"""
		Agrega la lista de aristas entregada al grafo
		"""
		for nodo1, nodo2 in aristas:
			self.agregar(nodo1, nodo2)
	def agregar(self, nodo1, nodo2):
		"""
		Agrega la arista del nodo 1 al 2. Si la arista no es en un solo sentido, tambien se agrega a la inversa.
		"""

		self._grafo[nodo1].add(nodo2)
		if (not self._unsentido):
			self._grafo[nodo2].add(nodo1)
	def borrar(self, nodo):
		"""
		Borra todas las referencias al nodo
		"""

		for nodo_int, aristas in self._grafo.iteritems():
			try:
				aristas.remove(nodo)
			except KeyError:
				pass
		try:
			del self._grafo[nodo]
		except KeyError:
			pass
	def __str__(self):
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))

def main():
    pass


if __name__ == "__main__":
    main()