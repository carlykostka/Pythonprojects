import random 
import string

def random_password(all, length):
    
    if __name__ == '__main__':  
        print('Hi! Welcome to password generator! ')
        
greeting = print('Hi! Welcome to password generator!' )
length = int(input('Enter the length of passowrd: '))
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

all = lowercase + uppercase + numbers + symbols

temp = random.sample(all, length)

password = " ".join(temp)

print(password)
