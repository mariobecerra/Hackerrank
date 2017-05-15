# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game

# Note: I had some help with this one because my original code was running stupidly slow

vowels = ['A', 'E', 'I', 'O', 'U']

def minion_game(string):
    # your code goes here
    n = len(string)    
    stuart = 0
    kevin = 0
    i = 0
    for letter in string:
        if(letter in vowels): kevin += (n - i)
        else: stuart += (n - i)
        i += 1
    if(kevin == stuart): out = 'Draw'
    elif kevin > stuart: out = 'Kevin ' + str(kevin)
    else: out = 'Stuart ' + str(stuart)
    print(out)
