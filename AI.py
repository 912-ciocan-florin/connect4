import random
import math
from copy import deepcopy

from Domain.Constants import COLUMN_COUNT, WINDOW_LENGTH, ROW_COUNT, AI_PIECE, PLAYER_PIECE, EMPTY


class AI:

    @staticmethod
    def evaluate_window(window, piece):
        """
        Compute a score for the given board for the possible move did with the given piece type
        :param window: given Board object
        :param piece: type of the piece to know which player move we evaluate
        :return: Score computed according to the game logic
        """
        score = 0
        # Assign correct opponent piece depending on the given piece
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = AI_PIECE

        # Compute score according to the game logic
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0

        # Score center column
        center_array = [int(i) for i in list(board.board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board.board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board.board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score positive sloped diagonal
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board.board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        # Check negatively sloped diagonals
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board.board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def minimax(self, repo, depth, alpha, beta, maximizing_player):
        valid_locations = repo.get_valid_locations()
        is_terminal = repo.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if repo.winning_move(AI_PIECE):
                    return None, 100000000000000
                elif repo.winning_move(PLAYER_PIECE):
                    return None, -10000000000000
                else:
                    # Game is over, no more valid moves
                    return None, 0
            else:
                # Depth is zero
                return None, self.score_position(repo.board, AI_PIECE)
        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = repo.get_next_open_row(col)
                b_copy = deepcopy(repo)
                b_copy.drop_piece(row, col, AI_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = repo.get_next_open_row(col)
                b_copy = deepcopy(repo)
                b_copy.drop_piece(row, col, PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
