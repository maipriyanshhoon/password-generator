import string
import random


# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    # length of password from the user
    length = int(input("Enter password length: "))
    username = input("Enter your Username or Email ID: ")
    website = input("Enter website name: ")

    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list
    return f'{username} and your password is "{"".join(password)}"                 WEBSITE: {website}\n'


# invoking the function
password_generated = generate_random_password()

f = open("password.txt", "a")
f.write(password_generated)
f.close()
