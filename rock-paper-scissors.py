import random

# 1D dictionary of different option spellings and their associated numbers
user_dict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
r = ('rock', 'Rock', 'ROCK')
p = ('paper', 'Paper', 'PAPER')
s = ('scissors', 'Scissors', 'SCISSORS')
user_dict = dict.fromkeys(r, 1)
user_dict.update(dict.fromkeys(p, 2))
user_dict.update(dict.fromkeys(s, 3))

# 1D dictionary of computer's number choice and associated spelling
comp_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
play_again = 0

# while the user chooses to play again...
while play_again == 0:

    #reset scores
    user = 0
    comp = 0

    #get user's choice and random computer choice
    print ("Choose Rock, Paper, or Scissors: ")
    user = input()
    print ("You chose", user)
    comp = random.randint(1, 3)
    print ("Computer chose", comp_dict[comp])

    # Conditions that indicate a TIE, WIN, or LOSS, and ask to play again
    if user_dict[user] == comp:
        print ("You tied. Would you like to play again? Enter 1 for Yes, 2 for no: ")
        play_again = int(input())-1

    elif (user_dict[user] == 3 and comp == 2) or (user_dict[user] == 1 and comp == 3) or (user_dict[user] == 2 and comp == 1):
        print ("Congrats, you won! Would you like to play again? Enter 1 for Yes, 2 for no: ")
        play_again = int(input())-1

    elif (comp == 3 and user_dict[user] == 2) or (comp == 1 and user_dict[user] == 3) or (comp == 2 and user_dict[user] == 1):
        print ("You lost. Would you like to play again? Enter 1 for Yes, 2 for no: ")
        play_again = int(input())-1

# if user is not playing again, print and exit
print("Thanks for playing. Goodbye.")
