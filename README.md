# aedii-labirinto

Atividade da aula 9 de AEDII: sair de um labirinto usando DFS, BFS e busca gulosa.
Cada casa livre do labirinto vira um vértice, e casas livres vizinhas são ligadas por uma aresta, aí é só buscar um caminho no grafo.

## Para executar:

```bash
python3 labirinto.py
```

## o labirinto

10 x 15, com "I" = início, "F" = saída, "#" = parede e "." = casa livre

```
...............
I#############.
.#.............
.#.############
.#.............
.#############.
.#....###......
..........####.
.#.###########.
..............F
```

Montei pensando em três coisas:

- uma rota curta, que desce pela esquerda e vai reto pela última linha
- uma rota longa, que sobe pro canto e desce em zigue-zague pela direita
- um corredor na linha 7 que aponta pra saída mas termina numa parede, pra enganar a gulosa

## implementações

Usei o montar_grafo e o desenhar da aula sem alterar nada. As três buscas seguem o mesmo esqueleto, o que muda é a estrutura:

- **DFS**: recursão, vai o mais fundo possível e volta quando não tem vizinho novo
- **BFS**: fila com deque, visita em camadas de distância a partir do início
- **gulosa**: fila de prioridade com heapq, sempre tira a casa com menor h

Cada uma devolve "(caminho, casas_visitadas)".
O caminho é montado com um dicionário pai, que guarda de qual casa a busca chegou em cada vértice. No final é somente sair da saída e ir voltando de pai em pai até o início, depois inverter.

Casas visitadas = quantas casas saíram da estrutura (contando início e saída)

## resultados

| algoritmo | tamanho do caminho | casas visitadas |
|---|---|---|
| DFS | 48 | 49 |
| BFS | 22 | 67 |
| gulosa | 24 | 25 |

Tamanho do caminho em passos

A BFS achou o menor caminho porque anda em camadas, então ela chega na saída pelo menor número de passos.
A DFS tenta subir antes de descer, caiu na rota longa e ficou com ela.
A gulosa entrou no corredor da linha 7 porque o h ia diminuindo, bateu na parede em (7, 10) e teve que dar a volta, por isso 24 em vez de 22.
