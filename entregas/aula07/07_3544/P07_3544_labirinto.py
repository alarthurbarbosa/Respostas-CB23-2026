
import random
from collections import deque


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """
    Questão 1: Gera um labirinto perfeito de m x n células lógicas usando
    Busca em Profundidade (DFS) Iterativa com uma pilha explícita.
    """
    # Grade expandida: (2m + 1) x (2n + 1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Matriz para controlar células lógicas visitadas
    visited = [[False] * n for _ in range(m)]

    # Pilha explícita para substituir a recursão (armazena coordenadas lógicas (x, y))
    stack = []

    # Inicia na sala lógica (0, 0) -> coordenada real (1, 1)
    start_x, start_y = 0, 0
    visited[start_x][start_y] = True
    maze[2 * start_x + 1][2 * start_y + 1] = room
    stack.append((start_x, start_y))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        x, y = stack[-1]

        # Encontra vizinhos lógicos não visitados
        unvisited_neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                unvisited_neighbors.append((nx, ny, dx, dy))

        if unvisited_neighbors:
            # Escolhe um vizinho aleatório
            nx, ny, dx, dy = random.choice(unvisited_neighbors)

            # Marca como visitado e derruba a parede intermediária
            visited[nx][ny] = True
            maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
            maze[2 * nx + 1][2 * ny + 1] = room

            # Empilha o próximo nó
            stack.append((nx, ny))
        else:
            # Backtracking: remove o topo da pilha quando não há caminhos
            stack.pop()

    # Posiciona o queijo em uma sala aleatória (evitando a sala inicial 1,1)
    while True:
        rx = random.randint(0, m - 1)
        ry = random.randint(0, n - 1)
        if rx != 0 or ry != 0:
            maze[2 * rx + 1][2 * ry + 1] = cheese
            break

    return maze


def solve_and_display_maze(maze, start=(1, 1), path_symbol='.'):
    """
    Questão 2: Encontra o caminho de `start` até o queijo no labirinto gerado
    utilizando Busca em Largura (BFS) para garantir o caminho mínimo.
    Exibe o labirinto resolvido no terminal.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Localiza a posição do queijo no labirinto
    cheese_pos = None
    for r in range(rows):
        for c in range(cols):
            val = maze[r][c]
            # O queijo é qualquer valor que não seja sala aberta (0, ' ') ou parede (1, 'W')
            if val not in (0, 1, ' ', 'W'):
                cheese_pos = (r, c)
                break
        if cheese_pos:
            break

    if not cheese_pos:
        print("Erro: Queijo não foi encontrado no labirinto.")
        return maze

    # Fila para BFS e dicionário de predecessores para reconstruir o caminho
    queue = deque([start])
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    found = False

    while queue:
        curr = queue.popleft()

        if curr == cheese_pos:
            found = True
            break

        r, c = curr
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # Células válidas não podem ser paredes (1 ou 'W')
                is_wall = (maze[nr][nc] in (1, 'W'))
                if not is_wall and (nr, nc) not in parent:
                    parent[(nr, nc)] = curr
                    queue.append((nr, nc))

    if not found:
        print("Caminho não encontrado!")
        return maze

    # Reconstrução do caminho percorrido
    path_coords = set()
    curr = cheese_pos
    while curr is not None:
        path_coords.add(curr)
        curr = parent[curr]

    # Cria uma cópia formatada para exibição
    solved_maze = [list(row) for row in maze]
    for r, c in path_coords:
        if (r, c) != start and (r, c) != cheese_pos:
            solved_maze[r][c] = path_symbol

    return solved_maze


def print_maze(maze):
    """Imprime a matriz do labirinto linha por linha de forma legível."""
    for row in maze:
        print("".join(str(cell) for cell in row))


if __name__ == '__main__':
    m, n = 10, 14
    random.seed(10110)

    # Exemplo 1: Com caracteres customizados (' ', 'W', '*')
    room_char = ' '
    wall_char = 'W'
    cheese_char = '*'

    print("=== LABIRINTO GERADO (DFS ITERATIVO) ===")
    maze = generate_maze(m, n, room=room_char, wall=wall_char, cheese=cheese_char)
    print_maze(maze)

    print("\n=== LABIRINTO RESOLVIDO (CAMINHO ATÉ O QUEIJO - BFS) ===")
    solved_maze = solve_and_display_maze(maze, start=(1, 1), path_symbol='.')
    print_maze(solved_maze)