from AI import AI
from Domain.Board import Board
from Domain.Constants import ROW_COUNT, COLUMN_COUNT
from Repo.repo import Repo
from Service.service import Service
from UI.UI import UI

board = Board(ROW_COUNT, COLUMN_COUNT)
repo = Repo(board)
service = Service(repo)

ai = AI()

ui = UI(service, ai)

ui.start()
