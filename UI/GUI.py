from Domain.Constants import size, COLUMN_COUNT, ROW_COUNT, BLUE, BLACK, RED, YELLOW,\
    SQUARE_SIZE, RADIUS, PLAYER_PIECE, AI_PIECE, height, width
import pygame


class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.update()
        self.font = pygame.font.SysFont("monospace", 75)

    def draw_board(self, board):
        """
        Display the Board using pygame
        """
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE,
                                                     SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                        int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(self.screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                          height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif board[r][c] == AI_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                             height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

    def piece_refresh(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARE_SIZE))

    def cpu_win(self):
        label = self.font.render("Computer wins!!", True, YELLOW)
        self.screen.blit(label, (40, 10))

    def player_win(self):
        label = self.font.render("You win!!", True, RED)
        self.screen.blit(label, (40, 10))

    def draw_player_piece(self, pos_x):
        pygame.draw.circle(self. screen, RED, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
