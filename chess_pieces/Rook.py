from coordinates import (
    UPPER_LIMIT,
    LOWER_LIMIT,
    POSSIBLE_BOARD_POSITIONS,
    is_valid_chess_position,
    is_valid_coordinate,
    get_coordinate_from_chess_position,
    get_chess_position_from_coordinate    
) 

class Rook:
    
    def __init__(self,color, current_position):
        self.color = color
        self.current_position = current_position
        
    def get_possible_positions(self, current_position):
        possible_coordinates = []
        x_cor, y_cor = coordinate = get_coordinate_from_chess_position(current_position)

        print(f'current: {coordinate}')

        # getting upper coordinates
        # the y coordinate ie the letter is constant
        print('ABOVE THE POSITION')
        for i in range(y_cor+1,UPPER_LIMIT+1):
            print((x_cor,i))
            possible_coordinates.append((x_cor,i))

        print('BELOW THE POSITION')
        # getting lower coordinates
        # the y coordinate ie the letter is constant    
        for i in range(y_cor-1,LOWER_LIMIT-1,-1):
            print((x_cor,i))
            possible_coordinates.append((x_cor,i))
            

        print('RIGHT OF THE POSITION')
        # getting coordinates in the right of the piece
        # the letter is constant (y-cor)
        for i in range(x_cor+1,UPPER_LIMIT+1):
            print((i,y_cor))
            possible_coordinates.append((x_cor,i))
            

        print('LEFT OF THE POSITION')
        for i in range(x_cor-1,LOWER_LIMIT-1,-1):
            print((i,y_cor))
            possible_coordinates.append((x_cor,i))

        possible_positions = [ get_chess_position_from_coordinate(i) for i in possible_coordinates ]

        print(f'Possible coordinates: {possible_coordinates}')
        print(f'Possible positions: {possible_positions}')
        return possible_positions
    
rook = Rook('black','A1')
rook.get_possible_positions('A1')
