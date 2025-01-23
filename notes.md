

I have a chessboard implementation where each piece type is represented by its own class. 
For the King class, I have a method that calculates all possible moves for the King and returns a set of valid destinations.

To ensure the King doesn’t move into a position that would put it in check, 
I’ve added logic within this method to loop through all other pieces on the board. 
This logic computes the possible destinations for these pieces and removes any overlapping positions from the King’s potential moves 
(i.e., positions where the King would be in check).

However, I’ve run into an issue with recursion: 
when this method evaluates the opponent's King, 
it triggers the same logic in the opponent King’s class, 
which loops over all other pieces as well. 
This eventually leads back to the original King, creating an infinite recursion.

How can I resolve this issue and prevent this recursive behavior when checking the possible moves of the Kings?



