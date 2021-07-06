# import
import random

# global 
rock = 1
paper = 2
scissors = 3
possible = [rock, paper, scissors]

# User Intro
def user_intro():
    print('Hi! Welcome to the game of Rock, Paper, Scissors')
    print('To get started:')
    print('     You will need to choose either: ')
    print('     [1] for rock, [2] for paper, or [3] for scissors to beat the computer ')
    print('     Basic rules include: ')
    print('         Rock beats scissors')
    print('         Paper beats rock')
    print('         Scissors beats paper')
    print('         Any time you want to quit the game just enter the key "q" ')
    return input('Ready to play?: ')

# player name
def player():
    return input('Enter your name: ')

# play again 
def again():
    end = input('Play again (y/n)? ')
    while end != "n" and end != "y":
        end = input('Please enter a valid response. ')
    if end == "n":
        print('Thank you! Goodbye ')
        raise SystemExit()
    elif end == "y":
        return end

def terminate_game(player_input):
    if player_input == 'q':
        print('Thank you! Goodbye. ')
        raise SystemExit()


#game
def game(player_guess, computer):
    if str(player_guess) == computer: 
        print('Both put ' + player_guess + ', Tie!')
    elif player_guess == rock: 
        if computer == scissors: 
            print('Rock beats scissors! ' + player1 + ' wins!')
            return True 
        else:
            print('Paper beats rock! Computer wins.')
            return False
    elif player_guess == paper:
        if computer == rock:
            print('Paper beats rock! ' + player1 + ' wins!')
            return True
        else:
            print('Scissors beats paper! Computer wins.')
            return False
    elif player_guess == scissors:
        if computer == paper:
            print('Scissors beats paper! ' + player1 + ' wins!')
            return True
        else:
            print('Rock beats scissors! Computer wins.')
            return False

# main
if __name__ == '__main__':
    response = user_intro()
    if response == 'no':
        raise SystemExit()
    player1 = player()
    player_guess_score = 0
    computer_score = 0
    while True: 
        player_input = input(player1 + ', rock, paper or scissors? ')
        if player_input > str(3) or player_input < str(1):
            very_end = terminate_game(player_input)
            print('Please enter a valid input')
            continue
        player_guess = int(player_input)
        computer = random.choice(possible)
        winner = game(player_guess, computer)
        if winner is True:
            player_guess_score = player_guess_score + 1
        else:
            computer_score = computer_score + 1
        print('Player score: ' + str(player_guess_score))
        print('Computer score: ' + str(computer_score))


        #recall = again()


