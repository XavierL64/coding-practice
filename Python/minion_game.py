# Exercise: The Minion Game
# In this game, two players (Stuart and Kevin) compete by creating substrings from a given string.
# Stuart's substrings must begin with a consonant, while Kevin's must begin with a vowel.
# Each substring scores points equal to the number of times it appears in the string.
# The winner is the player with the highest total score.

def minion_game(string):
    # Define vowels in uppercase since the input string is in uppercase.
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Calculate the length of the input string.
    length = len(string)
    
    # Initialize scores for both players.
    kevin = 0
    stuart = 0
    
    # For each index in the string, calculate the number of substrings starting at that index.
    # The number of substrings from index i is (length - i).
    for i in range(length):
        if string[i] in vowels:
            # If the letter is a vowel, add the number of possible substrings to Kevin's score.
            kevin += (length - i)
        else:
            # Otherwise, add to Stuart's score.
            stuart += (length - i)
    
    # Determine the winner or declare a draw.
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    # Read input, strip any extraneous whitespace, and start the game.
    s = input().strip()
    minion_game(s)
