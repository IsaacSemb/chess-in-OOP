

notes = """
    chess pieces deal in coordinates
    chessboard deals in chess positions
    
    """

class ChessBoard:
    def __init__(self, board_state=None):
        
        self.new_board = {
                'A8':None, 'B8':None, 'C8':None, 'D8':None, 'E8':None, 'F8':None, 'G8':None, 'H8':None,
                'A7':None, 'B7':None, 'C7':None, 'D7':None, 'E7':None, 'F7':None, 'G7':None, 'H7':None,
                'A6':None, 'B6':None, 'C6':None, 'D6':None, 'E6':None, 'F6':None, 'G6':None, 'H6':None,
                'A5':None, 'B5':None, 'C5':None, 'D5':None, 'E5':None, 'F5':None, 'G5':None, 'H5':None,
                'A4':None, 'B4':None, 'C4':None, 'D4':None, 'E4':None, 'F4':None, 'G4':None, 'H4':None,
                'A3':None, 'B3':None, 'C3':None, 'D3':None, 'E3':None, 'F3':None, 'G3':None, 'H3':None,
                'A2':None, 'B2':None, 'C2':None, 'D2':None, 'E2':None, 'F2':None, 'G2':None, 'H2':None,
                'A1':None, 'B1':None, 'C1':None, 'D1':None, 'E1':None, 'F1':None, 'G1':None, 'H1':None, 
            }
        if not board_state:
            self.board_positions = self.new_board            
        else:
            self.board_positions = board_state
            
        self.letter_number_mappings = { 'A': 1, 'B': 2,'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8 }
    
    def update_chessboard(self, board_arrangement):
        self.__init__()
        for piece in board_arrangement:
            self.board_positions[piece.position_on_board] = piece

        
    
            
        
    def get_letter_mapping_from_number(self, test_number):
        """
        it takes in a number and 
        converts it to the corresponding letter
        used for getting chess positions from coordinates
        """
        
        for letter, number in self.letter_number_mappings.items():
            # print(letter,number)
            if number==test_number:
                return letter
        raise Exception("The number has no corresponding letter on the chess board ")

    def get_number_mapping_from_letter(self, ltr):
        """
        it takes in a letter and 
        converts it to the corresponding number
        used for getting coordinates from chess positions
        """
        for letter, number in self.letter_number_mappings.items():
            # print(letter,number)
            if letter==ltr.upper():
                return number
            
        raise Exception("The letter doesnt exist on the chess board")


    def is_chess_position_valid(self, position):
        """
        checks a chess position eg A1, G5 
        whether its a valid chess position on the chess board
        """
        position = position.upper()
        return True if position in self.board_positions else False


    def is_coordinate_valid(self, coordinate):
        """
        checks a coordinate eg (1,3), (8,8) 
        whether its a valid chess coordinate
        coordinates strictly range from 1 to 8 
        """
        return True if 1<=coordinate[0]<=8 and 1<=coordinate[1]<=8 else False

    def get_coordinate_from_chess_position(self, position):
        """
        takes in a VALID chess position like A1 or G2
        It then converts its to chess board coordinate like (1,1)
        """
        if not self.is_chess_position_valid(position):
            return "position doesnt exist "
        position = position.upper()
        return int(self.get_number_mapping_from_letter(position[0])), int(position[1])


    def get_chess_position_from_coordinate(self, coordinate):
        """
        takes in a coordinate and 
        converts it into a chess position on the chess board
        """
        
        if not self.is_coordinate_valid(coordinate):
            return "position doesn't exist on board"
        letter = self.get_letter_mapping_from_number (coordinate[0])
        number = coordinate[1]
        return letter+str(number)


    def is_chess_position_taken(self, position):
        """
        checks the input position on chessboard instance 
        for whether it is filled or not and returns a boolean 
        """
        if not self.is_chess_position_valid(position):
            return "position doesnt exist"
        return self.board_positions[position]

    def is_coordinate_taken(self, coordinate):
        if not self.is_coordinate_valid(coordinate):
            return "coordinate is not valid"
        return self.board_positions[self.get_chess_position_from_coordinate(coordinate)]
    
    def fill_position(self, position, chess_piece='CHESS OBJECT HERE'):
        """
        A piece entering a board position
        """
        self.board_positions[position]=chess_piece
        
        
    def unfill_position(self, position):
        """
        A piece leaving a board position
        """
        self.board_positions[position]=None
    
    def update_postion( self, from_position, to_position ):
        self.unfill_position(from_position)
        self.fill_position(to_position)

    def is_chess_position_taken(self, position):
        """checks the board instance for whether the position in question is taken """
        if not self.is_chess_position_valid(position):
            raise Exception("Invalid Chess Position")
        
        return  self.board_positions[position] if self.board_positions[position] else None

    def is_coordinate_taken(self, coordinate):
        """checks the board instance for whether the coordinate in question is taken """
        return self.is_chess_position_taken(self.get_chess_position_from_coordinate(coordinate))
    
    def reveal_piece_in_position(self, position):
        return self.is_chess_position_taken(position.upper())



class ChessPiece:
    """
    representation of the base class of a chess piece in chess
    """
    
    def __init__( self,  position_on_board, chess_board: ChessBoard ,color=None, upper_limit = 8, lower_limit = 1,):
        self.position_on_board = position_on_board.upper()
        self.chess_board = chess_board        
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.color = color
        
    def get_possible_positions(self):
        pass
    
    def move_to_position(self,new_position):
        self.position_on_board = new_position
        
    def get_coordinate_from_chess_position(self, position):
        if not self.chess_board.is_chess_position_valid(position):
            return "position doesnt exist"
        position = position.upper()
        return int(self.chess_board.get_number_mapping_from_letter(position[0])), int(position[1])

    def __repr__(self):
        return f"<{self.color} {self.__class__.__name__} @ {self.position_on_board}>"

class Rook(ChessPiece):
    """
    Representation of the Rook in chess
    """
    
    def get_possible_positions(self, current_position):
        
        possible_coordinates = []
        
        x_cor, y_cor = self.get_coordinate_from_chess_position(current_position)

        # print(f'current: ({x_cor},{y_cor})')

        # getting upper coordinates
        # the y coordinate ie the letter is constant
        # print('ABOVE THE POSITION')
        for i in range(y_cor+1,self.upper_limit+1):
            crd = (x_cor,i)
            if self.chess_board.is_coordinate_taken(crd):
                if self.chess_board.is_coordinate_taken(crd).color != self.color:
                    possible_coordinates.append(crd)
                    if isinstance(self.chess_board.is_coordinate_taken(crd),King):
                        continue
                break
            # print(crd)
            possible_coordinates.append(crd)

        # print('BELOW THE POSITION')
        # getting lower coordinates
        # the y coordinate ie the letter is constant    
        for i in range(y_cor-1,self.lower_limit-1,-1):
            crd = (x_cor,i)
            if self.chess_board.is_coordinate_taken(crd):
                if self.chess_board.is_coordinate_taken(crd).color != self.color:
                    possible_coordinates.append(crd)
                    if isinstance(self.chess_board.is_coordinate_taken(crd),King):
                        continue
                break
            # print(crd)
            possible_coordinates.append(crd)
            

        # print('RIGHT OF THE POSITION')
        # getting coordinates in the right of the piece
        # the letter is constant (y-cor)
        for i in range(x_cor+1,self.upper_limit+1):
            crd = (i,y_cor)
            if self.chess_board.is_coordinate_taken(crd):
                if self.chess_board.is_coordinate_taken(crd).color != self.color:
                    possible_coordinates.append(crd)
                    if isinstance(self.chess_board.is_coordinate_taken(crd),King):
                        continue
                break
            # print(crd)
            possible_coordinates.append(crd)

            

        # print('LEFT OF THE POSITION')
        for i in range(x_cor-1,self.lower_limit-1,-1):
            crd = (i,y_cor)
            if self.chess_board.is_coordinate_taken(crd):
                if self.chess_board.is_coordinate_taken(crd).color != self.color:
                    possible_coordinates.append(crd)
                    if isinstance(self.chess_board.is_coordinate_taken(crd),King):
                        continue
                break
            # print(crd)
            possible_coordinates.append(crd)


        possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        # print(f'Possible coordinates: {possible_coordinates}')
        # print(f'Possible positions: {possible_positions}')
        
        return possible_positions


class Pawn(ChessPiece):
    
    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        # print(f'current: ({x_cor},{y_cor})')

        all_coords = {
            'north':(x_cor+0, y_cor+1), # North 
            'northwest':(x_cor-1, y_cor+1), # North 
            'northeast':(x_cor+1, y_cor+1), # North 
        }

        # check for valid
        for direction, crd in all_coords.items():
            if self.chess_board.is_coordinate_valid(crd):
                if self.chess_board.is_coordinate_taken(crd):
                    if self.chess_board.is_coordinate_taken(crd).color != self.color and direction!='north':
                        possible_coordinates.append(crd)
                    continue
                elif direction=='north':
                    possible_coordinates.append(crd)
                        
        
        # PLAYER TWO MOVES SOUTH FOR PAWNS SO YOU NEED TO CATER FOR THAT 
        # check for enpass
        # check for promotion
        

        possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        # print(f'Possible coordinates: {possible_coordinates}')
        # print(f'Possible positions: {possible_positions}')
        
        return possible_positions


class Knight(ChessPiece):

    # current_position = 'C4'

    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        # print(f'current: ({x_cor},{y_cor})')

        all_coords = [
            # upwards
            (x_cor-1, y_cor+2),
            (x_cor+1, y_cor+2),
            # downwards
            (x_cor-1, y_cor-2),
            (x_cor+1, y_cor-2),
            # left wards
            (x_cor+2, y_cor+1),
            (x_cor+2, y_cor-1),
            # right wards
            (x_cor-2, y_cor+1),
            (x_cor-2, y_cor-1),
        ]

        # check for valid
        for crd in all_coords:
            if self.chess_board.is_coordinate_valid(crd):
                if self.chess_board.is_coordinate_taken(crd):
                    if self.chess_board.is_coordinate_taken(crd).color == self.color:
                        continue
                possible_coordinates.append(crd)



        possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        # print(f'Possible coordinates: {possible_coordinates}')
        # print(f'Possible positions: {possible_positions}')
        
        return possible_positions
        




class Bishop(ChessPiece):
    
    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        # print(f'current: ({x_cor},{y_cor})')

        # getting north west diagonal coordinates
        # manipulation coordinate (-1,1)
        # print('North West diagonal')
        in_bound = True
        i = 1
        while in_bound:
            new_coord = ( x_cor-i , y_cor+i )
            if self.chess_board.is_coordinate_valid(new_coord):
                if self.chess_board.is_coordinate_taken(new_coord):
                    if self.chess_board.is_coordinate_taken(new_coord).color != self.color:
                        possible_coordinates.append(new_coord)
                        if isinstance(self.chess_board.is_coordinate_taken(new_coord),King):
                            i+=1
                            continue
                    break
                # print(new_coord)
                possible_coordinates.append(new_coord)
                i+=1
            else:
                in_bound = False

        # getting north east diagonal coordinates
        # manipulation coordinate (1,1)
        # print('North East diagonal')
        in_bound = True
        i = 1
        while in_bound:
            new_coord = ( x_cor+i , y_cor+i )
            if self.chess_board.is_coordinate_valid(new_coord):
                if self.chess_board.is_coordinate_taken(new_coord):
                    if self.chess_board.is_coordinate_taken(new_coord).color != self.color:
                        possible_coordinates.append(new_coord)
                        if isinstance(self.chess_board.is_coordinate_taken(new_coord),King):
                            i+=1
                            continue
                    break
                # print(new_coord)
                possible_coordinates.append(new_coord)
                i+=1
            else:
                in_bound = False

        # getting south east diagonal coordinates
        # manipulation coordinate (1,-1)
        # print('South East diagonal')
        in_bound = True
        i = 1
        while in_bound:
            new_coord = ( x_cor+i , y_cor-i )
            if self.chess_board.is_coordinate_valid(new_coord):
                if self.chess_board.is_coordinate_taken(new_coord):
                    if self.chess_board.is_coordinate_taken(new_coord).color != self.color:
                        possible_coordinates.append(new_coord)
                        if isinstance(self.chess_board.is_coordinate_taken(new_coord),King):
                            i+=1
                            continue
                    break
                # print(new_coord)
                possible_coordinates.append(new_coord)
                i+=1
            else:
                in_bound = False

        # getting south west diagonal coordinates
        # manipulation coordinate (1,-1)
        # print('South West diagonal')
        in_bound = True
        i = 1
        while in_bound:
            new_coord = ( x_cor-i , y_cor-i )
            if self.chess_board.is_coordinate_valid(new_coord):
                if self.chess_board.is_coordinate_taken(new_coord):
                    if self.chess_board.is_coordinate_taken(new_coord).color != self.color:
                        possible_coordinates.append(new_coord)
                        if isinstance(self.chess_board.is_coordinate_taken(new_coord),King):
                            i+=1
                            continue
                    break
                # print(new_coord)
                possible_coordinates.append(new_coord)
                i+=1
            else:
                in_bound = False


        possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        # print(f'Possible coordinates: {possible_coordinates}')
        # print(f'Possible positions: {possible_positions}')
        
        return possible_positions



class King(ChessPiece):

    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        print(f'current King: ({x_cor},{y_cor})')

        all_coords = [
            (x_cor+0, y_cor+1), # N
            (x_cor+1, y_cor+1), # NE
            (x_cor+1, y_cor+0), # E
            (x_cor+1, y_cor-1), # SE
            (x_cor+0, y_cor-1), # S
            (x_cor-1, y_cor-1), # SW
            (x_cor-1, y_cor+0), # W
            (x_cor-1, y_cor+1), # NW
        ]

        # check for valid
        for index, crd in enumerate(all_coords):
            
            # delete this
            print(index+1,'->', crd, self.chess_board.get_chess_position_from_coordinate(crd))
            
            if self.chess_board.is_coordinate_valid(crd):
                if not self.chess_board.is_coordinate_taken(crd):
                    # check if it is safe ie not in check
                    possible_coordinates.append(crd)
        
        king_possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]
        
        # check if it causes check
        checked_positions = []
        for position, piece in self.chess_board.board_positions.items():
            
            
            # if board position is filled
            if piece and piece.color != self.color and not isinstance(piece, King) :
                # get all places that piece can move
                positions = piece.get_possible_positions(position)
                checked_positions.extend(positions)
        
        safe_positions = list(set(king_possible_positions)-set(checked_positions))



        # print(f'Possible coordinates: {possible_coordinates}')
        # print(f'Possible positions: {possible_positions}')
        
        return safe_positions
    
    def in_check(self):
        checked_positions = []
        for position, piece in self.chess_board.board_positions.items():
            # if board position is filled
            if piece and piece.color != self.color :
                # get all places that piece can move
                positions = piece.get_possible_positions(position)
                checked_positions.extend(positions)
        return True if self.position_on_board in set(checked_positions) else False
        



class Queen(ChessPiece):

    # current_position = 'C4'
    def __init__(self, position_on_board, chess_board, upper_limit=8, lower_limit=1):
        super().__init__(position_on_board, chess_board, upper_limit, lower_limit)
        self.borrowed_movements: list[Rook|Bishop] = [Rook(position_on_board,chess_board,self.color), Bishop(position_on_board,chess_board,self.color)]

    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        print(f'current Queen: ({x_cor},{y_cor})')

        possible_positions = [ variant.get_possible_positions(current_position ) for variant in self.borrowed_movements  ]
        possible_positions = [position for sublist in possible_positions for position in sublist]
        print(f'all_queen_positions: {possible_positions}')
        
        return possible_positions



    
# rook = Rook('black','A1')
# rook.get_possible_positions('A1')


class ChessPlayer:
    def __init__(self, chess_board, name='Player', board_arrangement=None):
        self.name = name
        self.chess_board = chess_board
        self.board_arrangement = board_arrangement
    
    def select_piece(self, position):
        return [piece for piece in self.board_arrangement if piece.position_on_board == position][0]
    
    def __repr__(self):
        return f"< {self.__class__.__name__} {self.name} >"

            
            
            
class ChessPlayerLight(ChessPlayer):
    def __init__(self, chess_board:ChessBoard, name='Player', board_arrangement=None):
        super().__init__(chess_board, name, board_arrangement)
        
        if board_arrangement:
            self.board_arrangement = board_arrangement
        else:
            self.board_arrangement=[
                # back row
                Rook('A1',self.chess_board,'light'),
                Knight('B1',self.chess_board,'light'),
                Bishop('C1',self.chess_board,'light'),
                King('D1',self.chess_board,'light'),
                Queen('E1',self.chess_board,'light'),
                Bishop('F1',self.chess_board,'light'),
                Knight('G1',self.chess_board,'light'),
                Rook('H1',self.chess_board,'light'),
                
                # front row 
                # Pawn('A2',self.chess_board,'light'),
                # Pawn('B2',self.chess_board,'light'),
                # Pawn('C2',self.chess_board,'light'),
                # Pawn('D2',self.chess_board,'light'),
                # Pawn('E2',self.chess_board,'light'),
                # Pawn('F2',self.chess_board,'light'),
                # Pawn('G2',self.chess_board,'light'),
                # Pawn('H2',self.chess_board,'light'),
                ]
        
class ChessPlayerDark(ChessPlayer):
    def __init__(self, chess_board, name='Player', board_arrangement=None):
        super().__init__(chess_board, name, board_arrangement)
        
        if board_arrangement:
            self.board_arrangement = board_arrangement
        else:
            self.board_arrangement=[
                # back row
                Rook('A8', self.chess_board,'dark'),
                Knight('B8', self.chess_board,'dark'),
                Bishop('C8', self.chess_board,'dark'),
                King('D8', self.chess_board,'dark'),
                Queen('E8', self.chess_board,'dark'),
                Bishop('F8', self.chess_board,'dark'),
                Knight('G8', self.chess_board,'dark'),
                Rook('H8', self.chess_board,'dark'),
                
                # front row 
                # Pawn('A7', self.chess_board,'dark'),
                # Pawn('B7', self.chess_board,'dark'),
                # Pawn('C7', self.chess_board,'dark'),
                # Pawn('D7', self.chess_board,'dark'),
                # Pawn('E7', self.chess_board,'dark'),
                # Pawn('F7', self.chess_board,'dark'),
                # Pawn('G7', self.chess_board,'dark'),
                # Pawn('H7', self.chess_board,'dark'),
                            
            ]

# STARTING A GAME

def switch_turns(active_player, inactive_player):
    new_active_player=inactive_player
    new_inactive_player= active_player
    return new_active_player, new_inactive_player

# create a chess board
CB = ChessBoard()

print("\n--------board arrangement original at initiation-----------\n")
print(CB.board_positions)

# populate the chess board
player1 = ChessPlayerLight(name = 'Isaac', chess_board=CB)
player2 = ChessPlayerDark(name = 'Semb', chess_board=CB)

active_player = player1
inactive_player = player2

print("\033[31mThis is red text\033[0m")
gameover = False
while not gameover:

    print("\n--------chess players created-----------\n")
    print('active Player',active_player)
    print('inactive Player',inactive_player)


    continuesss = input("continue? (any key to continue / qqq to quit) : ")
    if continuesss.lower() == 'qqq':
        break


    print("\n--------player 1 (light) board arrangement-----------\n")
    print(active_player.board_arrangement)

    print("\n--------player 2 (light) board arrangement-----------\n")
    print(inactive_player.board_arrangement)

    print("\n--------mapping players board arrangements onto chess board-----------\n")
    general_board_arrangement = active_player.board_arrangement + inactive_player.board_arrangement
    CB.update_chessboard(general_board_arrangement)
    print(CB.board_positions)

    print("\n--------ask player for piece to move-----------\n")
    print('Avialable pieces')
    for i in active_player.board_arrangement:
        print(i)
    player_piece_to_move_position:ChessPiece = input("select a position of piece to move: ").upper()
    
    if player_piece_to_move_position.lower() == 'QQQ':
        break
    
    print()
    
    actual_piece_to_move:ChessPiece = CB.reveal_piece_in_position(player_piece_to_move_position)
    print( "Chosen piece:", actual_piece_to_move)

    print("\n--------chess board with respect to the piece-----------\n")
    print(actual_piece_to_move.chess_board.board_positions)

    print(f"\n--------showing available options for that piece {actual_piece_to_move} -----------\n")
    places_to_go = actual_piece_to_move.get_possible_positions(actual_piece_to_move.position_on_board)
    print(places_to_go)

    print("\n--------ask player for where to place that piece-----------\n")
    new_position_to_move = input(f"select a position for {player_piece_to_move_position} to move: ").upper()
    
    if new_position_to_move.lower() == 'QQQ':
        break

    if new_position_to_move not in places_to_go:
        print(f"{new_position_to_move} NOT IN \npossible  positions: {places_to_go}")

    else:
        # moving pice from source to destination
        print(f"moving {actual_piece_to_move} from {actual_piece_to_move.position_on_board} to {new_position_to_move}")
        
        # check if destination has a piece to displace
        opponent_piece_in_destination = CB.reveal_piece_in_position(new_position_to_move)
        print(opponent_piece_in_destination)
        
        # if there is opponent piece
        if opponent_piece_in_destination:
            print(opponent_piece_in_destination)
            
            # remove it in opponent board arrangement
            for piece in inactive_player.board_arrangement:
                if piece == opponent_piece_in_destination:
                    print (f"found piece {piece}")
                    break
            
            # displace piece
            print("\n-------- new player 2 board arrangement-----------\n")
            inactive_player.board_arrangement.remove(piece)
            print(inactive_player.board_arrangement)
            
            # change location of displacer to that position
            # look for displacer
            print("\n-------- player 1 board arrangement before change-----------\n")
            print (actual_piece_to_move)
            print(active_player.board_arrangement)
            
            for piece in active_player.board_arrangement:
                if piece == actual_piece_to_move:
                    print (f"found piece {piece}")
                    break
            print(piece.position_on_board)
            piece.position_on_board=new_position_to_move
            print(piece.position_on_board)
            print("\n-------- player 1 board arrangement AFTER change-----------\n")
            print(active_player.board_arrangement)
        
        # update_board
        print("\n-------- player 1 and 2 boards -----------\n")
        print(active_player.board_arrangement, len(active_player.board_arrangement) )
        print(inactive_player.board_arrangement, len(inactive_player.board_arrangement) )
        
        print()
        
        new_board_arrangement = active_player.board_arrangement + inactive_player.board_arrangement
        print(new_board_arrangement)
        
        print("\n-------- OLD BOARD -----------\n")
        print(CB.board_positions)
        
        print("\n-------- NEW BOARD -----------\n")
        CB.update_chessboard(new_board_arrangement)
        print(CB.board_positions)
        
        active_player, inactive_player = switch_turns( active_player, inactive_player )

# print()
# source_position = input('choose a piece to move: ').upper()

# chosen_piece:ChessPiece = player1.select_piece(source_position)

# print(f'You have picked up {chosen_piece}')

# print()

# desitnation_position = input(
#     f"""
#     choose a spot to place it
#     available positions are {chosen_piece.get_possible_positions(source_position)}
#     PICK ONE: """
#     ).upper()

# print()


