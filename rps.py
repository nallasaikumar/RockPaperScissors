import random

# dictionary 
# {key : value, key1 : value, key2: value }

# Scissors -> loose(Paper)
# Rock     -> loose(Scissors)
# Paper    -> loose(Rock)

code_choice = {1 : "Scissors", 2 : "Rock", 3 : "Paper"}
game_words = ('Scissors', 'Rock', 'Paper')

no_of_times = int(input('Enter no of times you wish to play with computer'))

computer_score = 0
user_score = 0

start = 0

while start <= no_of_times:
    lost = 0
    
    computer_choice = random.choice(game_words)  
    user_choice = int(input("Please select 1.Scissors 2.Rock & 3.Paper "))
    print(f'The user choice is, {code_choice[user_choice]}')
    
    if computer_choice == code_choice[user_choice]:
        pass
#         print('The Match is Draw. And its a tie')
    else:
        if computer_choice == 'Scissors':
            if code_choice[user_choice] == 'Paper':
                lost = 1
        elif computer_choice == 'Rock':
            if code_choice[user_choice] == 'Scissors':
                lost = 1
        elif computer_choice == 'Paper':
            if code_choice[user_choice] == 'Rock':
                lost = 1  # if lost is 1 means user lost it. else he won

        if lost == 0:
#             print(f'User Won, cheers!!! Computers choice is {computer_choice}')
            user_score = user_score + 1
        else:
#             print(f'User Lost, Computers choice is {computer_choice}')
            computer_score = computer_score + 1
    start = start + 1

if user_score > computer_score:
    print(f'User won the match by {user_score - computer_score} points')
elif user_score < computer_score:
    print(f'Computer won the match by {computer_score - user_score} points')
else:
    print('Its a Draw')
