import math
import sys
import random
import pygame

from Domain.Constants import PLAYER, CPU, SQUARE_SIZE, PLAYER_PIECE, AI_PIECE
from UI.GUI import GUI


class UI:
    def __init__(self, service, ai):
        self._service = service
        self._gui = None
        self._ai = ai

    def start_gui(self):
        self._gui = GUI()
        self._gui.draw_board(self._service.repo.board.board)
        turn = random.randint(PLAYER, CPU)
        game_over = False
        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    self._gui.piece_refresh()
                    pos_x = event.pos[0]
                    if turn == PLAYER:
                        self._gui.draw_player_piece(pos_x)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._gui.piece_refresh()
                    # Ask for Player Input
                    if turn == PLAYER:
                        pos_x = event.pos[0]
                        col = int(math.floor(pos_x / SQUARE_SIZE))

                        if self._service.is_valid_location(col):
                            row = self._service.get_next_open_row(col)
                            self._service.drop_piece(row, col, PLAYER_PIECE)

                            if self._service.winning_move(PLAYER_PIECE):
                                self._gui.player_win()
                                game_over = True

                            turn += 1
                            turn = turn % 2

                            self._gui.draw_board(self._service.repo.board.board)

            # Ask for CPU Input
            if turn == CPU and not game_over:
                col, minimax_score = self._ai.minimax(self._service.repo, 5, -math.inf, math.inf, True)

                if self._service.is_valid_location(col):
                    row = self._service.get_next_open_row(col)
                    self._service.drop_piece(row, col, AI_PIECE)

                    if self._service.winning_move(AI_PIECE):
                        self._gui.cpu_win()
                        game_over = True

                    self._gui.draw_board(self._service.repo.board.board)

                    turn += 1
                    turn = turn % 2

            if game_over:
                pygame.time.wait(5000)

    def start_console(self):
        # Print welcome message and present the board
        print('START GAME')
        print(self._service.repo.board)

        # 'Randomly' choose who start the game
        turn = random.randint(PLAYER, CPU)

        # Game starts
        game_over = False
        while not game_over:
            # Ask for PLAYER console input if GUI not used
            if turn == PLAYER and not game_over:
                done = False
                while not done:
                    # Player's input
                    col = input('Insert column: ')

                    # Validate the the Player's input
                    if '0' <= col <= '6' and len(col) == 1:
                        done = True
                        col = int(col)
                        if self._service.is_valid_location(col):
                            # Put player's piece in the selected column
                            row = self._service.get_next_open_row(col)
                            self._service.drop_piece(row, col, PLAYER_PIECE)

                            # Print game table after player's move
                            print('YOU:')
                            print(self._service.repo.board)

                            # Check if the Player pieces are in the winning position
                            if self._service.winning_move(PLAYER_PIECE):
                                print('You win!!')
                                game_over = True

                            # Player's turn finished
                            turn += 1
                            turn = turn % 2
                            done = True
                        else:
                            print('Column FULL!')
                    else:
                        print('Invalid column!')

            # Ask for CPU Input
            if turn == CPU and not game_over:
                col, minimax_score = self._ai.minimax(self._service.repo, 5, -math.inf, math.inf, True)

                if self._service.is_valid_location(col):
                    row = self._service.get_next_open_row(col)
                    self._service.drop_piece(row, col, AI_PIECE)

                    print('CPU: ')
                    print(self._service.repo.board)

                    if self._service.winning_move(AI_PIECE):
                        print('Computer wins!!')
                        game_over = True

                    turn += 1
                    turn = turn % 2

    def start(self):

        print('! Connect 4 !')
        print('1. Start game in console')
        print('2. Start game with GUI')
        cmd = input('Enter command number: ')

        try:
            if cmd == '1':
                self.start_console()
            elif cmd == '2':
                self.start_gui()
            else:
                print('Invalid command!')
        except ValueError:
            pass
