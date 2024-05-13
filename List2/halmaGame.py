import random
import copy
import time
import sys

class Board:
    def __init__(self, size=16):
        self.size = size
        self.board = self.generate_initial_state()

    def generate_initial_state(self):
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
            # Player 1 pieces in the top left corner
        for i in range(2):
            for j in range(5 - i):
                board[i][j] = 1
        # Player 2 pieces in the bottom right corner
        for i in range(14, 16):
            for j in range(11, 16 - (i - 14)):
                board[i][j] = 2
        return board

    def apply_move(self, move, player):
        (x1, y1), (x2, y2) = move
        self.board[x1][y1] = 0
        self.board[x2][y2] = player

    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))
        print("-------------------------------------------------------")


class TreeNode:
    def __init__(self, move, board_state, parent=None):
        self.move = move
        self.board_state = board_state
        self.parent = parent
        self.children = []

    def add_child(self, move, board_state):
        child = TreeNode(move, board_state, parent=self)
        self.children.append(child)
        return child

class Strategies:
    @staticmethod
    def distance_to_goal_heuristic(board, current_player):
        player1_distance = sum(i+j for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1)
        player2_distance = sum(abs(i - 15) + abs(j - 15) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 2)       
        return player2_distance if current_player == 2 else player1_distance

    @staticmethod
    def center_control_heuristic(board, current_player):
        player1_center_distance = sum(abs(i - 7) + abs(j - 7) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1)
        player2_center_distance = sum(abs(i - 7) + abs(j - 7) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 2)
        return player2_center_distance if current_player == 2 else player1_center_distance

    @staticmethod
    def edge_occupancy_heuristic(board, current_player):
        player1_edge_count = sum(1 for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1)
        player2_edge_count = sum(1 for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 2)
        return player2_edge_count if current_player == 2 else player1_edge_count


    @staticmethod
    def advanced_goal_distance_heuristic(board, current_player):
        if current_player == 1:
            target_x, target_y = 15, 15  # Target coordinates for player 1
            multiplier = -1
        else:
            target_x, target_y = 0, 0    # Target coordinates for player 2
            multiplier = 1

        distance = 0
        pieces_in_goal = 0
        goal_zone_limit = 5  

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == current_player:
                    dist = abs(target_x - i) + abs(target_y - j)
                    distance += dist
                    if dist <= goal_zone_limit:
                        pieces_in_goal += 1

        return distance - 10 * pieces_in_goal

    @staticmethod
    def piece_count_heuristic(board, current_player):
        player1_pieces = sum(1 for row in board for cell in row if cell == 1)
        player2_pieces = sum(1 for row in board for cell in row if cell == 2)
        return player2_pieces if current_player == 2 else player1_pieces

    @staticmethod
    def mobility_heuristic(board, current_player):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Possible directions
        mobility = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == current_player:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 0:
                            mobility += 1  # Increase mobility count if the adjacent square is empty

        return mobility
    
    @staticmethod
    def formation_heuristic(board, current_player):
        formation_value = 0
       
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == current_player:
                    
                    neighbors = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == current_player:
                                neighbors += 1
                    formation_value += neighbors  # Higher values for more clustered pieces

        return formation_value
    
    @staticmethod
    def random_heuristic(board, current_player):
        return random.randint(0, 10)
    
    @staticmethod
    def goal_zone_stability_heuristic(board, current_player):
        goal_zone_penalty = 0  
        
        if current_player == 1:
            goal_zone = [(i, j) for i in range(11, 16) for j in range(11, 16)] 
        else:
            goal_zone = [(i, j) for i in range(5) for j in range(5)]  

        
        for i, j in goal_zone:
            if board[i][j] == current_player:
                goal_zone_penalty -= 50 
        return goal_zone_penalty


    @staticmethod
    def strategy_one(current_node, current_player):
        return 0.9 * Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.1 * Strategies.piece_count_heuristic(current_node.board_state, current_player)
    
    @staticmethod
    def strategy_two(current_node, current_player):
        return 0.60 * Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.20 * Strategies.edge_occupancy_heuristic(current_node.board_state, current_player) + 0.2 * Strategies.advanced_goal_distance_heuristic(current_node.board_state, current_player)
    
    @staticmethod
    def strategy_three(current_node, current_player):
        return 0.60 * Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.20 * Strategies.center_control_heuristic(current_node.board_state, current_player) + 0.20 * Strategies.piece_count_heuristic(current_node.board_state, current_player)
    
    @staticmethod
    def strategy_four(current_node, current_player):
        return Strategies.random_heuristic(current_node.board_state, current_player) + 0.60 * Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.20 * Strategies.piece_count_heuristic(current_node.board_state, current_player)
    
    @staticmethod
    def strategy_five(current_node, current_player):
        return 0.50 * Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.50 * Strategies.piece_count_heuristic(current_node.board_state, current_player) + 0.20 * Strategies.center_control_heuristic(current_node.board_state, current_player)

    @staticmethod
    def strategy_six(current_node, current_player):
        return Strategies.random_heuristic(current_node.board_state,current_player)*0.05 + 0.3* Strategies.distance_to_goal_heuristic(current_node.board_state, current_player) + 0.10 * Strategies.mobility_heuristic(current_node.board_state, current_player) + 0.10 * Strategies.formation_heuristic(current_node.board_state, current_player) + Strategies.goal_zone_stability_heuristic(current_node.board_state, current_player) *0.2

    @staticmethod
    def generate_random_strategy():

        heuristics = [
            Strategies.distance_to_goal_heuristic,
            Strategies.center_control_heuristic,
            Strategies.edge_occupancy_heuristic,
            Strategies.piece_count_heuristic,
            Strategies.mobility_heuristic,
            Strategies.formation_heuristic,
            Strategies.advanced_goal_distance_heuristic
        ]
        
        num_heuristics = random.randint(1, len(heuristics))

        selected_heuristics = random.sample(heuristics, num_heuristics)

        weights = [random.random() for _ in range(num_heuristics)]
        weight_sum = sum(weights)
        normalized_weights = [w / weight_sum for w in weights]
        

        def random_strategy(board, current_player):
            score = 0
            for heuristic, weight in zip(selected_heuristics, normalized_weights):
                score += weight * heuristic(board, current_player)
            return score
        
        return random_strategy


class HalmaGame:
    def __init__(self, strategyPlayerOne, strategyPlayerTwo):
        self.board_size = 16
        self.board = Board()
        self.current_node = TreeNode(None, self.board.board)
        self.current_player = 1
        self.players = [1, 2]
        self.num_players = 2
        self.rounds = 0
        self.visited_nodes = 0
        self.alpha_beta_pruning = 0
        self.winner = None
        self.strategy = {}
        self.strategy[1] = strategyPlayerOne
        self.strategy[2] = strategyPlayerTwo
        self.draw_rounds_limit = 100


    def setBoard(self, board):
        self.board = board

    def setStrategyForPlayer(self, player, strategy):
        self.strategy[player] = strategy

    def switch_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % self.num_players]

    def game_over(self):
        
        player1_wins = True
        player2_wins = True

        # Define the winning zones for each player
        player1_target_zone = [(14, 15), (15, 14), (15, 15)]  # Generally the bottom right corner or similar
        player2_target_zone = [(0, 0), (0, 1), (1, 0)]       # Generally the top left corner or similar

        # Check if all player 1 pieces are in player 2's starting zone
        for i in range(14, 16):
            for j in range(11, 16):
                if self.current_node.board_state[i][j] != 1:
                    player1_wins = False
                    break

        # Check if all player 2 pieces are in player 1's starting zone
        for i in range(2):
            for j in range(5):
                if self.current_node.board_state[i][j] != 2:
                    player2_wins = False
                    break

        # Assess if there's a winner
        if player1_wins:
            self.winner = 1
            return True
        if player2_wins:
            self.winner = 2
            return True

        
       
        if self.rounds >= self.draw_rounds_limit:  
            self.winner = None  # Indicate a draw
            return True

        return False

    def evaluate_board(self):
        strategy_number = self.strategy[self.current_player]
        if  strategy_number == 1:
            return Strategies.strategy_one(self.current_node, self.current_player)
        elif strategy_number == 2:
            return Strategies.strategy_two(self.current_node, self.current_player)
        elif strategy_number == 3:
            return Strategies.strategy_three(self.current_node, self.current_player)
        elif strategy_number == 4:
            return Strategies.strategy_four(self.current_node, self.current_player)
        elif strategy_number == 5:
            return Strategies.strategy_five(self.current_node, self.current_player)
        elif strategy_number == 6:
            return Strategies.strategy_six(self.current_node, self.current_player)
        else:
            return Strategies.generate_random_strategy()(self.current_node.board_state, self.current_player)
    
    def generate_moves(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.current_node.board_state[i][j] == self.current_player:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            new_x, new_y = i + dx, j + dy
                            if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size:
                                if self.current_node.board_state[new_x][new_y] == 0:
                                    board_copy = copy.deepcopy(self.current_node.board_state)
                                    board_copy[new_x][new_y] = self.current_player
                                    board_copy[i][j] = 0
                        
                                    self.current_node.add_child(((i, j), (new_x, new_y)), board_copy)
                                else:
                                    new_x, new_y = new_x + dx, new_y + dy
                                    if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size:
                                        if self.current_node.board_state[new_x][new_y] == 0:
                                            board_copy = copy.deepcopy(self.current_node.board_state)
                                            board_copy[new_x][new_y] = self.current_player
                                            board_copy[i][j] = 0
                                            self.current_node.add_child(((i, j), (new_x, new_y)), board_copy)     
    
    
    def minimax(self, depth, alpha, beta, maximizing_player=True):
        if depth == 0 or self.game_over():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = -sys.maxsize
            if not self.current_node.children:
                self.generate_moves()
            for child in self.current_node.children:
                self.current_node = child
                self.visited_nodes += 1
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.current_node = self.current_node.parent
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    self.alpha_beta_pruning += 1
                    break 
            return max_eval
        else:
            min_eval = sys.maxsize
            if not self.current_node.children:
                self.generate_moves()
            for child in self.current_node.children:
                self.current_node = child
                self.visited_nodes += 1
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.current_node = self.current_node.parent
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    self.alpha_beta_pruning += 1
                    break
            return min_eval

    def best_move(self, depth):
        best_move = None
        alpha = -sys.maxsize
        beta = sys.maxsize
        max_eval = -sys.maxsize
        if not self.current_node.children:
            self.generate_moves()
        for child in self.current_node.children:
            self.current_node = child
            self.visited_nodes += 1
            eval = self.minimax(depth - 1, alpha, beta, False)
            self.current_node = self.current_node.parent
            if eval > max_eval:
                max_eval = eval
                best_move = child
            alpha = max(alpha, eval)
        return best_move

    def play_with_alpha_beta(self, depth):
        start_time = time.time()
        while not self.game_over():
         
            child = self.best_move(depth)
            if child is None:
                break
            self.current_node = child
            self.visited_nodes += 1
            print("Move", self.current_node.move)
            print("Player", self.current_player)
            self.rounds += 1
            self.board.apply_move(self.current_node.move, self.current_player)
            self.board.print_board()
            self.switch_player()

        end_time = time.time()
        print("Total Rounds:", self.rounds)
        if self.winner is not None:
            print("Winner is player number:", self.winner)
        else:
            print("Draw")
        print("Visited Nodes:", self.visited_nodes)
        print("Runtime:", end_time - start_time, "seconds")
        print("Strategy of Player 1:", self.strategy[1])
        print("Strategy of Player 2:", self.strategy[2])



game = HalmaGame(7,7)
game.play_with_alpha_beta(2)