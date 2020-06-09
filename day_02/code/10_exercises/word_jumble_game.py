# Word Jumble Game

# The computer picks a random word
# Presents it to the user in a jumbled fashion
# Allows the user to guess
# Will repeat for 10 words
# Finally give a score

# perk  --> kper

import random


# Words used in the game

words = ['apples', 'laptop', 'giraffe', 'monkey', 'compact' ]

# random.choice()
# random.shuffle()


# Gaming Loop

points = 0
random.shuffle(words)
for word in words:

    # Jumble the word
    lw = list(word)
    random.shuffle(lw)
    jw = ''.join(lw)

    # Present to the user
    print('\nThe computer has chosen a word...')
    print(jw)

    # Take the user input
    uw = input('Guess this word --> ')   

    # Compare and set  the points
    if(uw == word):
        points += 1

    # ----
    print('-'*60 + '\n\n')

# Print the results

print('POINTS : ', points)
