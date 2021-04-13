from string import ascii_letters
from random import randint, choice, shuffle

def random_letter():
    random_letter = choice(ascii_letters)
    return random_letter

def random_number():
    random_number = randint(0, 9)
    return random_number

def generate_password(password_length):
    password = []
    final_password = []
    n_letters = randint(1,password_length)
    n_numbers = password_length - n_letters
    for i in range(n_letters):
        password.append(random_letter())
    for j in range(n_numbers):
        password.append(str(random_number()))

    shuffle(password)
    final_password = "".join(password)
    return final_password

def user_interface():
    password_length = int(input("How long it will be? (min 6)\n"))
    if(password_length >= 6):
        print("Generating...")
        password = generate_password(password_length)
        print("Your Password is: {}".format(password))
    else:
        print("Minimum 6, please")

user_interface()