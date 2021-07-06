#make a function that adds two numbers together and gives output 

# User Prompt

def add_two_numbers(number_1, number_2):
    return number_1 + number_2

if __name__ == '__main__':
    print('Enter any two numbers to add them together: ')

    number_one = int(input('Enter first number: '))
    number_two = int(input('Enter second number: '))
    sum = add_two_numbers(number_one, number_two)
    # print('Sum: ' + str((add_two_numbers(number_onet, number_two) + 5)))

    print('Sum: ' + str(sum))
