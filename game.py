from chess import chess_board, chess_positions

class Converter:

    @staticmethod
    def pos_to_coords(pos1, pos2):
        positions = [pos1, pos2]
        coords = []
        for pos in positions:
            x = 0
            for rows in chess_positions:
                y=0
                x+=1
                for el in rows:
                    y+=1
                    if el == pos:
                        coords.append([x, y])
        return coords
    @staticmethod
    def pos_to_name(pos):
        for row, row_ in zip(chess_board, chess_positions):
            for piece, piece_ in zip(row, row_):
                if pos == piece_:
                    return piece

    @staticmethod
    def pos_to_piece(pos1:str, pos2:str):
        Coords = Converter.pos_to_coords(pos1, pos2)
        return [chess_board[Coords[0][0]-1][Coords[0][1]-1],chess_board[Coords[1][0]-1][Coords[1][1]-1]]

    @staticmethod
    def coords_to_pos(coords:list):
        return [chess_positions[coords[0][0]-1][coords[0][1]-1], chess_positions[coords[1][0]-1][coords[1][0]-1]] 

    @staticmethod
    def coords_to_piece(coords:list):
        return [chess_board[coords[0][0]-1][coords[0][1]-1], chess_board[coords[1][0]-1][coords[1][0]-1]] 

def is_move_valid(i_move, f_move):
    moves = [i_move, f_move]
    is_valid = []
    for move in moves:
        for rows in chess_positions:
            for element in rows:
                if (element == move):
                    is_valid.append(True)
    if (len(is_valid) == 2):
        return True
    else:
        return False
            

if __name__ == "__main__":
    print(Converter.pos_to_coords("e2", "e5"))
    
    
