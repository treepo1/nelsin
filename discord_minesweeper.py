import random


BOMBA = 1 
NADA = 0
DESCONHECIDO = -1
BANDEIRA = -2



def generate_grid():
    grid = list()
    piece = None
    bomb = False
    for _ in range(9):
        linha = []
        for __ in range(9):
            bomb = random.random() < 0.2
            if bomb:
                piece = BOMBA
            else:
                piece = NADA
            linha.append(piece)
        grid.append(linha)
    return grid




player_grid = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1]

]

simbolos = {
    '-1': '.',
    '-2': 'F'
}

def show_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if player_grid[i][j] == DESCONHECIDO or player_grid[i][j]== BANDEIRA:
                print(simbolos[str(player_grid[i][j])], end = ' ')
            else:
                print(player_grid[i][j], end = ' ')
        print()

moves = [(-1,0),(1,0),(1,-1),(0,-1),(1,1),(-1,-1),(0,1),(-1,1)]


def count(linha,coluna,grid):
    count = 0
    for move in moves:
        mov_linha = move[0]
        mov_coluna = move[1]
        if (linha+mov_linha) <= 8 and (coluna+mov_coluna)<=8:
            if grid[linha + mov_linha][coluna + mov_coluna] == 1 and (linha+mov_linha)>=0 and (coluna+mov_coluna)>=0:
                count+=1
    return count


def click(linha,coluna,grid,player_grid):
    if grid[linha][coluna] == BOMBA:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == NADA:
                    player_grid[i][j] == count(i,j)
                elif grid[i][j] == BOMBA:
                    player_grid[i][j] = 'B'
        print("BOOM!")
    elif grid[linha][coluna] == NADA and count(linha,coluna)!=0:
        player_grid[linha][coluna] = count(linha,coluna)
    else:
        player_grid[linha][coluna] = 0
        white_cells = [(linha,coluna)]
        while len(white_cells) > 0:
            white_cell = white_cells.pop()
            for move in moves:
                contador = 0
                linha = white_cell[0] + move[0]
                coluna = white_cell[1] + move[1]
                if (linha<=8 and linha>=0) and (coluna<=8 and coluna>=0):
                    if (player_grid[linha][coluna] == DESCONHECIDO) and (grid[linha][coluna] == NADA):
                        player_grid[linha][coluna] = count(linha,coluna)
                        if (linha,coluna) not in white_cells and (count(linha,coluna) == 0):
                            white_cells.append(white_cell)
                        else:
                            player_grid[linha][coluna] = count(linha,coluna)


def set_flag(linha,coluna,player_grid):
    if player_grid[linha][coluna] == BANDEIRA:
        player_grid[linha][coluna] = DESCONHECIDO
    else:
        player_grid[linha][coluna] = BANDEIRA