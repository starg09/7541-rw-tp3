def prim(inicio, rutas, ciudades):
    mst = set()
    por_visitar = []
    visitados = set(inicio)
    heappush(por_visitar, (0,inicio))
    while (len(por_visitar) != 0):
        actual = heappop(por_visitar)
        if (actual[1] not in visitados):
            union(visitados,set(actual[1]))
            for id_vecino, rutas in rutas[actual[1]]:


