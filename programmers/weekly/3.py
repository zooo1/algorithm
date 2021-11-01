def solution(game_board, table):
    def find_empty_space(r, c, space):
        board_visited[r][c] = True
        space.append((r, c))
        for i in range(4):
            tr = r + dx[i]
            tc = c + dy[i]
            if 0 <= tr < ROW and 0 <= tc < COL and game_board[tr][tc] == 0 and not board_visited[tr][tc]:
                find_empty_space(tr, tc, space)


    ROW = len(game_board)
    COL = len(game_board[0])
    dx = [ 1, 0, -1, 0]
    dy = [ 0, 1, 0, -1]
    board_visited = [[False for _ in range(COL)] for _ in range(ROW)]
    table_visited = [[False for _ in range(COL)] for _ in range(ROW)]
    empty_spaces = []
    puzzle_spaces = []



    for row in range(ROW):
        for col in range(COL):
            if game_board[row][col] == 0 and board_visited[row][col] == False:
                empty_space = []
                find_empty_space(row, col, empty_space)
                empty_spaces.append(empty_space)
            
            if table[row][col] == 1 and table_visited[row][col] == False:
                puzzle_space = []
                find_empty_space(row, col, puzzle_space)
                puzzle_spaces.append(puzzle_space)
    
    print(puzzle_spaces)
    

    answer = -1
    return answer


print(
  solution(
    [
      [1, 1, 0, 0, 1, 0],
      [0, 0, 1, 0, 1, 0],
      [0, 1, 1, 0, 0, 1],
      [1, 1, 0, 1, 1, 1],
      [1, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 0, 0],
    ],
    [
      [1, 0, 0, 1, 1, 0],
      [1, 0, 1, 0, 1, 0],
      [0, 1, 1, 0, 1, 1],
      [0, 0, 1, 0, 0, 0],
      [1, 1, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0],
    ],
  ),
)
