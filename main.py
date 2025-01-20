

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
        
        return  True if self.board_positions[position] else False

    def is_coordinate_taken(self, coordinate):
        """checks the board instance for whether the coordinate in question is taken """
        return self.is_chess_position_taken(self.get_chess_position_from_coordinate(coordinate))













class ChessPiece:
    """
    representation of the base class of a chess piece in chess
    """
    
    def __init__( self,  position_on_board, chess_board: ChessBoard , upper_limit = 8, lower_limit = 1,):
        self.position_on_board = position_on_board.upper()
        self.chess_board = chess_board        
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        
    def get_possible_positions(self):
        pass
    
    def move_to_position(self,new_position):
        self.position_on_board = new_position
        
    def get_coordinate_from_chess_position(self, position):
        if not self.chess_board.is_chess_position_valid(position):
            return "position doesnt exist"
        position = position.upper()
        return int(self.chess_board.get_number_mapping_from_letter(position[0])), int(position[1])


class Rook(ChessPiece):
    """
    Representation of the Rook in chess
    """
    # def __init__(self, *args, **kwargs):
    #     super().__init__( *args, **kwargs)
    
    def __init__(self, position_on_board, chess_board, upper_limit=8, lower_limit=1):
        super().__init__(position_on_board, chess_board, upper_limit, lower_limit)
        
        
            
        # current_position = 'B3'
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
                break
            # print(crd)
            possible_coordinates.append(crd)

        # print('BELOW THE POSITION')
        # getting lower coordinates
        # the y coordinate ie the letter is constant    
        for i in range(y_cor-1,self.lower_limit-1,-1):
            crd = (x_cor,i)
            if self.chess_board.is_coordinate_taken(crd):
                break
            # print(crd)
            possible_coordinates.append(crd)
            

        # print('RIGHT OF THE POSITION')
        # getting coordinates in the right of the piece
        # the letter is constant (y-cor)
        for i in range(x_cor+1,self.upper_limit+1):
            crd = (i,y_cor)
            if self.chess_board.is_coordinate_taken(crd):
                break
            # print(crd)
            possible_coordinates.append(crd)

            

        # print('LEFT OF THE POSITION')
        for i in range(x_cor-1,self.lower_limit-1,-1):
            crd = (i,y_cor)
            if self.chess_board.is_coordinate_taken(crd):
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

        all_coords = [
            (x_cor+0, y_cor+1), # North only
        ]

        # check for valid
        for crd in all_coords:
            if self.chess_board.is_coordinate_valid(crd):
                if not self.chess_board.is_coordinate_taken(crd):
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
                if not self.chess_board.is_coordinate_taken(crd):
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
            new_coord = ( x_cor-i , y_cor-i )
            if self.chess_board.is_coordinate_valid(new_coord):
                if self.chess_board.is_coordinate_taken(new_coord):
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

        print(f'current: ({x_cor},{y_cor})')

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
        for crd in all_coords:
            if self.chess_board.is_coordinate_valid(crd):
                if not self.chess_board.is_coordinate_taken(crd):
                    # check if it is safe ie not in check
                    possible_coordinates.append(crd)



        possible_positions = [ self.chess_board.get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        print(f'Possible coordinates: {possible_coordinates}')
        print(f'Possible positions: {possible_positions}')
        
        return possible_positions
    



class Queen(ChessPiece):

    # current_position = 'C4'
    def __init__(self, position_on_board, chess_board, upper_limit=8, lower_limit=1):
        super().__init__(position_on_board, chess_board, upper_limit, lower_limit)
        self.borrowed_movements: list[Rook|Bishop] = [Rook(position_on_board,chess_board), Bishop(position_on_board,chess_board)]

    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor  = self.chess_board.get_coordinate_from_chess_position(current_position)

        print(f'current: ({x_cor},{y_cor})')

        possible_positions = [ variant.get_possible_positions(current_position ) for variant in self.borrowed_movements  ]
        possible_positions = [position for sublist in possible_positions for position in sublist]
        print(f'all_queen_positions: {possible_positions}')
        
        return possible_positions



    
# rook = Rook('black','A1')
# rook.get_possible_positions('A1')


class Player:
    def __init__(self, name='Player'):
        self.name = name
    
    # def move_chess_piece(self, chess_piece: BaseChessPiece):


# trials
CB = ChessBoard()
# CB.fill_position('G7')

queen = Queen('A1',CB)
print(queen.position_on_board)
queen.get_possible_positions(queen.position_on_board)
