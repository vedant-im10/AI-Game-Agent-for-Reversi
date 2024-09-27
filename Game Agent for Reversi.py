import time

PLAYER_COLOR = None
BOARD_SIZE = 12
EMPTY, BLACK, WHITE = '.', 'X', 'O'
DIRECTIONS = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

POSITIONAL_WEIGHTS = {
    (0, 0): 1000, (0, 1): -800, (0, 2): 500, (0, 3): 80, (0, 4): 80, (0, 5): 80, 
    (0, 6): 80, (0, 7): 80, (0, 8): 80, (0, 9): 500, (0, 10): -800, (0, 11): 1000,
    
    (1, 0): -800, (1, 1): -800, (1, 2): 200, (1, 3): -50, (1, 4): -50, (1, 5): -50, 
    (1, 6): -50, (1, 7): -50, (1, 8): -50, (1, 9): 200, (1, 10): -800, (1, 11): -800,
    
    (2, 0): 500, (2, 1): 200, (2, 2): 300, (2, 3): 0, (2, 4): 0, (2, 5): 0, 
    (2, 6): 0, (2, 7): 0, (2, 8): 0, (2, 9): 300, (2, 10): 200, (2, 11): 500,
    
    (3, 0): 80, (3, 1): -50, (3, 2): 0, (3, 3): -100, (3, 4): 5, (3, 5): 5, 
    (3, 6): 5, (3, 7): 5, (3, 8): -100, (3, 9): 0, (3, 10): -50, (3, 11): 80,
    
    (4, 0): 80, (4, 1): -50, (4, 2): 0, (4, 3): 5, (4, 4): 10, (4, 5): 10, 
    (4, 6): 10, (4, 7): 10, (4, 8): 5, (4, 9): 0, (4, 10): -50, (4, 11): 80,
    
    (5, 0): 80, (5, 1): -50, (5, 2): 0, (5, 3): 5, (5, 4): 10, (5, 5): 15, 
    (5, 6): 15, (5, 7): 10, (5, 8): 5, (5, 9): 0, (5, 10): -50, (5, 11): 80,
    
    (6, 0): 80, (6, 1): -50, (6, 2): 0, (6, 3): 5, (6, 4): 10, (6, 5): 15, 
    (6, 6): 15, (6, 7): 10, (6, 8): 5, (6, 9): 0, (6, 10): -50, (6, 11): 80,
    
    (7, 0): 80, (7, 1): -50, (7, 2): 0, (7, 3): 5, (7, 4): 10, (7, 5): 10, 
    (7, 6): 10, (7, 7): 10, (7, 8): 5, (7, 9): 0, (7, 10): -50, (7, 11): 80,
    
    (8, 0): 80, (8, 1): -50, (8, 2): 0, (8, 3): -100, (8, 4): 5, (8, 5): 5, 
    (8, 6): 5, (8, 7): 5, (8, 8): -100, (8, 9): 0, (8, 10): -50, (8, 11): 80,
    
    (9, 0): 500, (9, 1): 200, (9, 2): 300, (9, 3): 0, (9, 4): 0, (9, 5): 0, 
    (9, 6): 0, (9, 7): 0, (9, 8): 0, (9, 9): 300, (9, 10): 200, (9, 11): 500,
    
    (10, 0): -800, (10, 1): -800, (10, 2): 200, (10, 3): -50, (10, 4): -50, (10, 5): -50, 
    (10, 6): -50, (10, 7): -50, (10, 8): -50, (10, 9): 200, (10, 10): -800, (10, 11): -800,
    
    (11, 0): 1000, (11, 1): -800, (11, 2): 500, (11, 3): 80, (11, 4): 80, (11, 5): 80, 
    (11, 6): 80, (11, 7): 80, (11, 8): 80, (11, 9): 500, (11, 10): -800, (11, 11): 1000,
}


'''
POSITIONAL_WEIGHTS = {
    (0, 0): 1000, (0, 1): -800, (0, 2): 500, (0, 3): 80, (0, 4): 80, (0, 5): 80, 
    (0, 6): 80, (0, 7): 80, (0, 8): 80, (0, 9): 500, (0, 10): -800, (0, 11): 1000,
    
    (1, 0): -800, (1, 1): -800, (1, 2): 200, (1, 3): -50, (1, 4): -50, (1, 5): -50, 
    (1, 6): -50, (1, 7): -50, (1, 8): -50, (1, 9): 200, (1, 10): -800, (1, 11): -800,
    
    (2, 0): 500, (2, 1): 200, (2, 2): 200, (2, 3): 0, (2, 4): 0, (2, 5): 0, 
    (2, 6): 0, (2, 7): 0, (2, 8): 0, (2, 9): 200, (2, 10): 200, (2, 11): 500,
    
    (3, 0): 80, (3, 1): -50, (3, 2): 0, (3, 3): 5, (3, 4): 5, (3, 5): 5, 
    (3, 6): 5, (3, 7): 5, (3, 8): 5, (3, 9): 0, (3, 10): -50, (3, 11): 80,
    
    (4, 0): 80, (4, 1): -50, (4, 2): 0, (4, 3): 5, (4, 4): 10, (4, 5): 10, 
    (4, 6): 10, (4, 7): 10, (4, 8): 5, (4, 9): 0, (4, 10): -50, (4, 11): 80,
    
    (5, 0): 80, (5, 1): -50, (5, 2): 0, (5, 3): 5, (5, 4): 10, (5, 5): 15, 
    (5, 6): 15, (5, 7): 10, (5, 8): 5, (5, 9): 0, (5, 10): -50, (5, 11): 80,
    
    (6, 0): 80, (6, 1): -50, (6, 2): 0, (6, 3): 5, (6, 4): 10, (6, 5): 15, 
    (6, 6): 15, (6, 7): 10, (6, 8): 5, (6, 9): 0, (6, 10): -50, (6, 11): 80,
    
    (7, 0): 80, (7, 1): -50, (7, 2): 0, (7, 3): 5, (7, 4): 10, (7, 5): 10, 
    (7, 6): 10, (7, 7): 10, (7, 8): 5, (7, 9): 0, (7, 10): -50, (7, 11): 80,
    
    (8, 0): 80, (8, 1): -50, (8, 2): 0, (8, 3): 5, (8, 4): 5, (8, 5): 5, 
    (8, 6): 5, (8, 7): 5, (8, 8): 5, (8, 9): 0, (8, 10): -50, (8, 11): 80,
    
    (9, 0): 500, (9, 1): 200, (9, 2): 200, (9, 3): 0, (9, 4): 0, (9, 5): 0, 
    (9, 6): 0, (9, 7): 0, (9, 8): 0, (9, 9): 200, (9, 10): 200, (9, 11): 500,
    
    (10, 0): -800, (10, 1): -800, (10, 2): 200, (10, 3): -50, (10, 4): -50, (10, 5): -50, 
    (10, 6): -50, (10, 7): -50, (10, 8): -50, (10, 9): 200, (10, 10): -800, (10, 11): -800,
    
    (11, 0): 1000, (11, 1): -800, (11, 2): 500, (11, 3): 80, (11, 4): 80, (11, 5): 80, 
    (11, 6): 80, (11, 7): 80, (11, 8): 80, (11, 9): 500, (11, 10): -800, (11, 11): 1000,
}

'''

# is_valid_move checks if a move is legal by player and piece position.
def is_valid_move(black_pieces, white_pieces, player, row, col):
    if (col, row) in black_pieces or (col, row) in white_pieces:
        return False
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    valid = False
    for dx, dy in DIRECTIONS:
        x, y = col + dx, row + dy
        if (x, y) in opponent_pieces:
            while (x, y) in opponent_pieces:
                x += dx
                y += dy
                if (x, y) in (black_pieces if player == BLACK else white_pieces):
                    valid = True
                    break
    return valid

# calculate_mobility counts legal moves available for a player.
def calculate_mobility(black_pieces, white_pieces, player):
    player_pieces = black_pieces if player == BLACK else white_pieces
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    return len(get_legal_moves(player_pieces, opponent_pieces, player))

# calculate_frontier_disks counts the player's pieces on the board's frontier, vulnerable to flipping.
def calculate_frontier_disks(black_pieces, white_pieces, player):
    frontier_disks = 0
    player_pieces = black_pieces if player == BLACK else white_pieces
    for x, y in player_pieces:
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and (nx, ny) not in player_pieces and (nx, ny) not in (white_pieces if player == BLACK else black_pieces):
                frontier_disks += 1
                break
    return frontier_disks

def count_stable_disks(black_pieces, white_pieces, player):
    def is_disk_stable(disk, player_pieces, opponent_pieces):
        x, y = disk
        if (x == 0 or x == BOARD_SIZE - 1) and (y == 0 or y == BOARD_SIZE - 1):
            return True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                if (nx, ny) in player_pieces:
                    break
                elif (nx, ny) in opponent_pieces:
                    nx += dx
                    ny += dy
                else:
                    return False
        return True

    # Initialize counters
    stable_black = stable_white = 0

    # Check every disk on the board
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if (x, y) in black_pieces:
                if is_disk_stable((x, y), black_pieces, white_pieces):
                    stable_black += 1
            elif (x, y) in white_pieces:
                if is_disk_stable((x, y), white_pieces, black_pieces):
                    stable_white += 1

    myScore = stable_black if player == BLACK else stable_white
    opScore = stable_white if player == BLACK else stable_black
    return 100*(myScore-opScore/(myScore+opScore+1))

def disk_count(black_pieces, white_pieces, player):
    player_pieces = black_pieces if player == BLACK else white_pieces
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    player_disk = len(player_pieces)
    opponent_disk = len(opponent_pieces)
    return ((player_disk-opponent_disk)/(player_disk+opponent_disk+1))*100

def count_corner_captures(black_pieces, white_pieces, player):
    corners = [(0, 0), (0, BOARD_SIZE-1), (BOARD_SIZE-1, 0), (BOARD_SIZE-1, BOARD_SIZE-1)]
    player_pieces = black_pieces if player == BLACK else white_pieces
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    capture_count_player = sum(1 for corner in corners if corner in player_pieces)
    capture_count_opponent = sum(1 for corner in corners if corner in opponent_pieces)
    return ((capture_count_player-capture_count_opponent)/(capture_count_player + capture_count_opponent + 1))*100

def evaluate_board(black_pieces, white_pieces, player, game_phase):
    mobility_score = calculate_mobility(black_pieces, white_pieces, player)
    frontier_discs_score = calculate_frontier_disks(black_pieces, white_pieces, player)
    corner_capture_score = count_corner_captures(black_pieces, white_pieces, player)
    disk_count_score = disk_count(black_pieces, white_pieces, player)
    count_stable_score = count_stable_disks(black_pieces, white_pieces, player)
    
    # Positional advantage
    player_pieces = black_pieces if player == BLACK else white_pieces
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    player_score = sum(POSITIONAL_WEIGHTS[piece] for piece in player_pieces)
    opponent_score = sum(POSITIONAL_WEIGHTS[piece] for piece in opponent_pieces)
    positional_advantage = ((player_score - opponent_score)/(player_score + opponent_score + 1)*100)
    
    # Adjust weights based on game phase
    if game_phase == 'opening':
        return (10 * mobility_score) + (corner_capture_score * 100) + (disk_count_score * 2) + (positional_advantage * 10) + (count_stable_score* 10)
    
    elif game_phase == 'midgame':
        return (5 * mobility_score) + (corner_capture_score * 500) - (frontier_discs_score * 3) + (disk_count_score * 200) + (positional_advantage * 20) + (count_stable_score * 20)
    else:  # endgame
        return (corner_capture_score * 200) - (frontier_discs_score * 5) + (disk_count_score * 50) + (positional_advantage * 5) + (count_stable_score*40)


# make_move executes a move, flipping opponent pieces as necessary.
def make_move(black_pieces, white_pieces, player, row, col):
    if not is_valid_move(black_pieces, white_pieces, player, row, col):
        return False, black_pieces, white_pieces
    if player == BLACK:
        new_black_pieces = set(black_pieces)
        new_white_pieces = set(white_pieces)
        new_black_pieces.add((col, row))
    else:
        new_black_pieces = set(black_pieces)
        new_white_pieces = set(white_pieces)
        new_white_pieces.add((col, row))
    
    # Flip opponent pieces
    for dx, dy in DIRECTIONS:
        x, y = col + dx, row + dy
        pieces_to_flip = []
        while (x, y) in (new_white_pieces if player == BLACK else new_black_pieces):
            pieces_to_flip.append((x, y))
            x += dx
            y += dy
        if (x, y) in (new_black_pieces if player == BLACK else new_white_pieces):
            for px, py in pieces_to_flip:
                if player == BLACK:
                    new_black_pieces.add((px, py))
                    new_white_pieces.discard((px, py))
                else:
                    new_white_pieces.add((px, py))
                    new_black_pieces.discard((px, py))
    
    return True, new_black_pieces, new_white_pieces

# get_legal_moves lists all legal moves for a player, prioritized by positional weights.
def get_legal_moves(black_pieces, white_pieces, player):
    legal_moves = []
    opponent_pieces = white_pieces if player == BLACK else black_pieces
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if is_valid_move(black_pieces, white_pieces, player, y, x):
                legal_moves.append((x, y))
    legal_moves.sort(key=lambda move: POSITIONAL_WEIGHTS[move], reverse=True)
    return legal_moves

# iterative_deepening_best_move and minimax work together, adjusting search depth based on time limit and maximizing player advantage.
def iterative_deepening_best_move(black_pieces, white_pieces, player, max_depth, time_limit):
    global PLAYER_COLOR
    best_move = None
    best_eval = float('-inf') if player == BLACK else float('inf')
    start_time = time.time()
    game_phase = determine_game_phase(black_pieces, white_pieces)
    
    for depth in range(1, max_depth + 1): 
        move, eval = minimax(black_pieces, white_pieces, player, depth, float('-inf'), float('inf'), player == BLACK, game_phase)
        if (player == BLACK and eval > best_eval) or (player == WHITE and eval < best_eval):
            best_move = move
            best_eval = eval
        
        if time.time() - start_time > time_limit:
            break
    
    return best_move

alpha = float('-inf')
beta = float('inf')

def minimax(black_pieces, white_pieces, player, depth, alpha, beta, maximizing_player=True, game_phase=None):
    global PLAYER_COLOR
    if depth == 0 or game_over(black_pieces, white_pieces):
        return None, evaluate_board(black_pieces, white_pieces, player, game_phase)
    
    if PLAYER_COLOR != player:
    # if player == PLAYER_COLOR:
        max_eval = float('-inf')
        best_move = None
        for move in get_legal_moves(black_pieces, white_pieces, player):
            _, new_black_pieces, new_white_pieces = make_move(black_pieces, white_pieces, player, move[1], move[0])
            _, eval = minimax(new_black_pieces, new_white_pieces, WHITE if player == BLACK else BLACK, depth - 1, alpha, beta, False)
            eval = max(eval, max_eval)
            
            if(max_eval <= eval):
                best_move = move
            max_eval = max(max_eval, eval)
            
            if max_eval >= beta:
                return best_move, max_eval
            alpha = max(alpha, max_eval)
        return best_move, max_eval
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_legal_moves(black_pieces, white_pieces, player):
            _, new_black_pieces, new_white_pieces = make_move(black_pieces, white_pieces, player, move[1], move[0])
            _, eval = minimax(new_black_pieces, new_white_pieces, WHITE if player == BLACK else BLACK, depth - 1, alpha, beta, True)
            
            if(eval <= min_eval):
                best_move = move
            min_eval = min(min_eval, eval)
            if min_eval <= alpha:
                return best_move, min_eval  
            beta = min(beta, min_eval)
        return best_move, min_eval

def read_input(file_path):
    global PLAYER_COLOR
    black_pieces = set()
    white_pieces = set()
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        player = lines[0].strip()
        PLAYER_COLOR = BLACK if player == 'X' else WHITE
        time_black, time_white = map(float, lines[1].split())
        for y, line in enumerate(lines[2:14]):
            for x, char in enumerate(line):
                if char == 'X':
                    black_pieces.add((x, y))
                elif char == 'O':
                    white_pieces.add((x, y))
    return black_pieces, white_pieces, player, time_black, time_white

def write_output(move, file_path):
    col_letter = chr(move[0] + ord('a'))
    row_number = move[1] + 1
    with open(file_path, 'w') as file:
        file.write(f"{col_letter}{row_number}\n")

# game_over checks if the game has ended.
def game_over(black_pieces, white_pieces):
    return not get_legal_moves(black_pieces, white_pieces, BLACK) and not get_legal_moves(black_pieces, white_pieces, WHITE)

def determine_game_phase(black_pieces, white_pieces):
    total_pieces = len(black_pieces) + len(white_pieces)
    empty_squares = BOARD_SIZE**2 - total_pieces
    if empty_squares > 100:
        return 'opening'
    elif empty_squares > 50:
        return 'midgame'
    else:
        return 'endgame'

def get_time_adjusted_depth(remaining_time, game_phase):
    #depth_settings = {
     #   'opening': [(280, 4), (250, 6), (200, 5), (150, 4), (100, 3), (10, 2)],
      #  'midgame': [(200, 6), (150, 5), (100, 4), (10, 3)],
       # 'endgame': [(160, 7), (110, 6), (60, 5), (10, 4)]
    #}
    depth_settings = {
        'opening': [(260, 4), (100, 3), (10, 2)],
        'midgame': [(200, 4), (100, 4), (10, 3)],
        'endgame': [(160, 4), (110, 4), (60, 3), (10, 2)]
    }
    for time_threshold, depth in depth_settings[game_phase]:
        if remaining_time > time_threshold:
            return depth
    return 1

def quick_move(black_pieces, white_pieces, player):
    legal_moves = get_legal_moves(black_pieces, white_pieces, player)
    return legal_moves[0] if legal_moves else None

def execute_game_logic(file_path_input, file_path_output, time_limit):
    black_pieces, white_pieces, player, time_black, time_white = read_input(file_path_input)
    remaining_time = time_black if player == BLACK else time_white
    game_phase = determine_game_phase(black_pieces, white_pieces)

    if remaining_time < 5:
        move = quick_move(black_pieces, white_pieces, player)
    else:
        adjusted_depth = get_time_adjusted_depth(remaining_time, game_phase)
        move = iterative_deepening_best_move(black_pieces, white_pieces, player,adjusted_depth, time_limit)
    write_output(move, file_path_output)

execute_game_logic('input.txt', 'output.txt', time_limit = 5.0)