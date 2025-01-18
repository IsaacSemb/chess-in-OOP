
chess_board_X = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chess_board_coords_X = [ 0, 1, 2, 3, 4, 5, 6, 7 ]

chess_board_Y = [ '1', '2', '3', '4', '5', '6', '7', '8' ]
chess_board_coords_Y = [ 0, 1, 2, 3, 4, 5, 6, 7 ]

letter_coordinate_mappings = {
    'A': 1, 
    'B': 2, 
    'C': 3, 
    'D': 4, 
    'E': 5, 
    'F': 6, 
    'G': 7, 
    'H': 8
    
}

POSSIBLE_BOARD_POSITIONS = [
    'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
    'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
    'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
    'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
    'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
    'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
    'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
    'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 
]


# check whether a position exists on the board 
# takes in chess positions and args
def is_valid(position):
    position = position.upper()
    return True if position in POSSIBLE_BOARD_POSITIONS else False

# check whether a coordinate is valid 
# valid coordinates range from 1 to 8 for both X and Y 
def is_coordinate_valid(coordinate):
    X,Y = coordinate
    return True if 1<= X <= 8 and 1<= Y <= 8 else False


# derive a coordinate from a chess position
def get_coordinate(position):
    if not is_valid(position):
        return "position doesnt exist on the chessboard "
    position = position.upper()
    return int(letter_coordinate_mappings[position[0]]), int(position[1])

# helper function to convert a coordinate position to the letter mapping
def get_letter_from_coordinate(coordinate):
    for letter, number in letter_coordinate_mappings.items():
        # print(letter,number)
        if number==coordinate:
            return letter
    print("doesn't exist")
    return False

def get_position_from_coordinate(coordinate):
    if not is_coordinate_valid(coordinate):
        return "position doesn't exist on board"
    letter = get_letter_from_coordinate(coordinate[0])
    number = coordinate[1]
    return letter+str(number)







































