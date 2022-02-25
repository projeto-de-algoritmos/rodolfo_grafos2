
class Algoritmos:
    def dijkstra(self,grafo,inicio):
        length = len(grafo)
        type_ = type(grafo)
        if type_ == list:
            nodes = [i for i in range(length)]
        elif type_ == dict:
            nodes = grafo.keys()

        visitado = [inicio]
        caminho = {inicio:{inicio:[]}}
        nodes.remove(inicio)
        distancia_grafo = {inicio:0}
        pre = next = inicio

        while nodes:
            distancia = float('inf')
            for v in visitado:
                for d in nodes:
                    nova_distancia = grafo[inicio][v] + grafo[v][d]
                    if nova_distancia <= distancia:
                        distancia = nova_distancia
                        next = d
                        pre = v
                        grafo[inicio][d] = nova_distancia


            caminho[inicio][next] = [i for i in caminho[inicio][pre]]
            caminho[inicio][next].append(next)

            distancia_grafo[next] = distancia

            visitado.append(next)
            nodes.remove(next)

        return distancia_grafo, caminho

    def kruskal(self,grafo):
        assert type(grafo)==dict

        nodes = grafo.keys()   
        visited = set()
        caminho = []
        next = None

        while len(visited) < len(nodes):
            distance = float('inf') 
            for s in nodes:
                for d in nodes:
                    if s in visited and d in visited or s == d:
                        continue
                    if grafo[s][d] < distance:
                        distance = grafo[s][d]
                        pre = s
                        next = d

            caminho.append((pre, next))
            visited.add(pre)
            visited.add(next)

        return caminho

algoritmno = Algoritmos()

grafo_dicionario = {
                "df":{"df": 0, "go": 2, "mg": 1, "rs": 4, "sp":3},
                "go":{"df": 1, "go": 0, "mg": 4, "rs": 2, "sp":2},
                "mg":{"df": 2, "go": 1, "mg": 0, "rs":1, "sp":4},
                "rs":{"df": 3, "go": 5, "mg": 2, "rs":0,"sp":1},
                "sp":{"df": 3, "go": 5, "mg": 2, "rs":4,"sp":0},
}

grafo_dicionario = {
                "df":{"df": 0, "go": 2, "mg": 1, "rs": 4, "sp":3},
                "go":{"df": 1, "go": 0, "mg": 4, "rs": 2, "sp":2},
                "mg":{"df": 2, "go": 1, "mg": 0, "rs":1, "sp":4},
                "rs":{"df": 3, "go": 5, "mg": 2, "rs":0,"sp":1},
                "sp":{"df": 3, "go": 5, "mg": 2, "rs":4,"sp":0},
}

print('Exemplo de Dijkstra:')
distancia, caminho = algoritmno.dijkstra(grafo_dicionario, 'df')
print (distancia, '\n', caminho)

print('\nExemplo de Kruskal:')
caminho = algoritmno.kruskal(grafo_dicionario)
print caminho

