import heapq
from collections import deque

labirinto = [
    "...............",
    "I#############.",
    ".#.............",
    ".#.############",
    ".#.............",
    ".#############.",
    ".#....###......",
    "..........####.",
    ".#.###########.",
    "..............F",
]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))

inicio = achar(labirinto, 'I')
saida  = achar(labirinto, 'F')


DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo

grafo = montar_grafo(labirinto)


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))

def montar_caminho(pai, saida):
    caminho = []
    v = saida
    while v is not None:
        caminho.append(v)
        v = pai[v]
    caminho.reverse()
    return caminho

def dfs_visitar(grafo, v, saida, visitados, pai):
    visitados.add(v)
    if v == saida:
        return True
    for w in grafo[v]:
        if w not in visitados:
            pai[w] = v
            if dfs_visitar(grafo, w, saida, visitados, pai):
                return True
    return False

def dfs(grafo, inicio, saida):
    visitados = set()
    pai = {inicio: None}
    dfs_visitar(grafo, inicio, saida, visitados, pai)
    return montar_caminho(pai, saida), len(visitados)

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    pai = {inicio: None}
    fila = deque([inicio])
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        if v == saida:
            break
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                pai[w] = v
                fila.append(w)
    return montar_caminho(pai, saida), len(ordem)

def h(v, saida):
    return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

def gulosa(grafo, inicio, saida):
    visitados = {inicio}
    pai = {inicio: None}
    fronteira = [(h(inicio, saida), inicio)]
    ordem = []
    while fronteira:
        _, v = heapq.heappop(fronteira)
        ordem.append(v)
        if v == saida:
            break
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                pai[w] = v
                heapq.heappush(fronteira, (h(w, saida), w))
    return montar_caminho(pai, saida), len(ordem)


caminho_dfs, visitadas_dfs = dfs(grafo, inicio, saida)
print("DFS")
desenhar(labirinto, caminho_dfs)

caminho_bfs, visitadas_bfs = bfs(grafo, inicio, saida)
print("\nBFS")
desenhar(labirinto, caminho_bfs)

caminho_gulosa, visitadas_gulosa = gulosa(grafo, inicio, saida)
print("\nGulosa")
desenhar(labirinto, caminho_gulosa)

print("\nalgoritmo | tamanho do caminho | casas visitadas")
print("DFS       |", len(caminho_dfs) - 1, "|", visitadas_dfs)
print("BFS       |", len(caminho_bfs) - 1, "|", visitadas_bfs)
print("Gulosa    |", len(caminho_gulosa) - 1, "|", visitadas_gulosa)
