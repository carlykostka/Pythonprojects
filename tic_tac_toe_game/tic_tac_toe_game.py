# Imports
import random

# Globals
theBoard = {'1': ' ', '2': ' ', '3': ' ','4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '} 


# Functions
# print the board
#     |   |
#  ___|___|___
#     |   |
#  ___|___|___
#     |   |
#     |   |

def show_board():
    print(theBoard['1'] + '  |' + theBoard['2'] + '  |' + theBoard['3'])
    print('___|___|___')
    print(theBoard['4'] + '  |' + theBoard['5'] + '  |' + theBoard['6'])
    print('___|___|___')
    print(theBoard['7'] + '  |' + theBoard['8'] + '  |' + theBoard['9'])
    print('   |'   '   |')

# prompts user to enter number
def user_intro():
    print('Welcome to Tic Tac Toe')
    print('------------------------')
    print('To play:')
    print('    Enter a number 1-9 ')
    print('    1 being the upper left corner of the board ')
    print('    and 9 being the lower right corner of the board')
    print('    You will need to enter a number in accordance to where you want to place your play')
    print('    You will take turns playing against eachother')
    print('    Whoever gets 3 in a row first wins! Good luck!!')
    return input('Ready to Play? ')

#player names 
def player_name(player_number):
    print("Player " + player_number)
    return input("Enter the name : ")

# changes the board according to user input
def user_prompt(player_name):
    correct = False
    while correct is False:
        answer = int(input(player_name + ', Enter number in accordance to the space you want to play: '))
        if answer>10 or answer<0:
            print('That answer is invalid. Enter a number 1-9.')
        elif theBoard[str(answer)] == ' ':
            correct = True
        else:
            print('That spot is taken, try again')
    return answer
    

# function to update board base on user input
def update_play(guess, turn):
    theBoard[str(guess)] = turn

# who wins
def winner(turn):
    if theBoard['1'] == turn and theBoard['2'] == turn and theBoard['3'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['4'] == turn and theBoard['5'] == turn and theBoard['6'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['7'] == turn and theBoard['8'] == turn and theBoard['9'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['1'] == turn and theBoard['4'] == turn and theBoard['7'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['2'] == turn and theBoard['5'] == turn and theBoard['8'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['3'] == turn and theBoard['6'] == turn and theBoard['9'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['1'] == turn and theBoard['5'] == turn and theBoard['9'] == turn:
        print(turn, 'wins!')
        return True
    if theBoard['3'] == turn and theBoard['5'] == turn and theBoard['7'] == turn:
        print(turn, 'wins!')
        return True
    return False 

#tie
def board_full(): 
    full = True
    for x in theBoard:
        if(x.count(' ') > 0):
            full = False
    print('Tie!')
    return full

# end of game
def again():
    end = input('Play again (y/n)? ')
    while end != "n" and end != "y":
        end = input('Please enter a valid response. ')
    if end == "n":
        print('Thank you! Goodbye ')
        raise SystemExit()
    elif end == "y":
        return end

# Main
if __name__ == '__main__':
    response = user_intro()
    if response == 'no':
        raise SystemExit()
    player1 = player_name(str(1))
    player2 = player_name(str(2))
    turn = 'X'
    current_player_name = player1
    player1_score = 0 
    player2_score = 0 
    while True:
        show_board()
        for x in range(1,10):
            player_input = user_prompt(current_player_name)
            update_play(player_input, turn)
            show_board()
            won = winner(turn)
            if won is True: 
                break
            if turn == 'X':
                turn = 'O'
                current_player_name = player2
            elif turn == 'O': 
                turn = 'X'
                current_player_name = player1
        if not won:
            board_full()
        if won is True:
            if turn == 'X': 
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1
        print('SCOREBOARD')
        print('-----------')
        print(player1 + ' score: ' + str(player1_score))
        print(player2 + ' score: ' + str(player2_score)) 
        print('-----------')
        recall = again()
        theBoard = {'1': ' ', '2': ' ', '3': ' ','4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        if recall == 'no':
            break
    # if response =='no':
    #     raise SystemExit()



