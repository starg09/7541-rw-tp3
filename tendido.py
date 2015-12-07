Prim (Grafo G)
       /* Inicializamos todos los nodos del grafo. 
       La distancia la ponemos a infinito y el padre de cada nodo a NULL
        Encolamos, en una cola de prioridad 
                  donde la prioridad es la distancia, 
               todas las parejas <nodo,distancia> del grafo*/
       por cada u en V[G] hacer
           distancia[u] = INFINITO
           padre[u] = NULL
           Añadir(cola,<u,distancia[u]>)
       distancia[u]=0
       mientras !esta_vacia(cola) hacer
           // OJO: Se entiende por mayor prioridad aquel nodo cuya distancia[u] es menor.
           u = extraer_minimo(cola) //devuelve el minimo y lo elimina de la cola.
           por cada v adyacente a 'u' hacer
               si ((v ∈ cola) && (distancia[v] > peso(u, v)) entonces
                   padre[v] = u
                   distancia[v] = peso(u, v)
                   Actualizar(cola,<v,distancia[v]>)