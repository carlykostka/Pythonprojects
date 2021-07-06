import random


def check_if_correct(users_guess, random_number):
    if int(users_guess) == random_number:
        print('Your guess is correct! ')
        return True 
    if int(users_guess) < random_number:
        print('Your guess was low, guess again. ')
    elif int(users_guess) > random_number:
        print('Your guess was high, guess again. ')
    return False

users_guess = input('Guess a random number between 0 and 10: ')

# random_number = random.randint(0,10)
random_number = random.randint(0,10)
# print(random_number)
correct = False
# loop this (while loop)
count = 0
while correct is False:
    count = count + 1
    is_correct = check_if_correct(users_guess, random_number)
    if is_correct is False:
        users_guess = input('Guess a random number between 0 and 10: ')
    else:
        print('It took you: ' + str(count) + ' times')
        correct = True


# print('The correct answer was: ')
# print(random_number)