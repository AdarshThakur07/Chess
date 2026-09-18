from chess import chess_positions, chess_board
from game import Converter
class Pawn:
    def __init__(self, pos, color):
        self._ipos = pos[0]
        self._fpos = pos[1]
        self._fsquare = Converter.pos_to_name(pos[1])
        self._name = Converter.pos_to_name(pos[0])
        self._color = color
        
        if (Converter.pos_to_name(self._fpos) == ".") :
            if(self._ipos[0] == self._fpos[0]):
                self.move_forward(pos)
        

    def move_forward(self, pos):
        if Converter.pos_to_name(pos[1]) == ".":
            piece1, piece2 = (Converter.pos_to_coords(self._ipos, self._fpos))[0], (Converter.pos_to_coords(self._ipos, self._fpos))[1]
            # if piece1[0] - 2 == piece2[0] or piece1[0] - 1 == piece2[0]:

    
            if self._color == "white":
                if piece1[0] - 1 == piece2[0]:
                    chess_board[piece2[0]-1][piece2[1]-1] = chess_board[piece1[0]-1][piece1[1]-1]
                    chess_board[piece1[0]-1][piece1[1]-1] = "."
                elif "2" in self._ipos and piece1[0] - 2 == piece2[0] or piece1[0] - 1 == piece2[0]:
                    chess_board[piece2[0]-1][piece2[1]-1] = chess_board[piece1[0]-1][piece1[1]-1]
                    chess_board[piece1[0]-1][piece1[1]-1] = "."
            elif self._color == "black":
                if piece1[0] - 1 == piece2[0]:
                    chess_board[piece2[0]-1][piece2[1]-1] = chess_board[piece1[0]-1][piece1[1]-1]
                    chess_board[piece1[0]-1][piece1[1]-1] = "."
                elif "7" in self._ipos and piece1[0] + 2 == piece2[0] or piece1[0] + 1 == piece2[0]:
                    chess_board[piece2[0]-1][piece2[1]-1] = chess_board[piece1[0]-1][piece1[1]-1]
                    chess_board[piece1[0]-1][piece1[1]-1] = "."

