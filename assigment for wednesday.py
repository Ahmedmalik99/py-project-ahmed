# # assigment for num 55555
#                     5555


# a = "5"
#
# for i in range(5,0,-1):
#     print(a * i)


# assigment to print 1
#                    33
#                    555
#                    7777
#                    99999

#
#
# for i in range(1, 10, 2):
#     print(str(i) * int((i + 1) / 2))


# assigment for #55555
#               4444
#               333

#
# for i in range (5,0,-1):
#     print((str(i) * int((i))))


# assigment 1
#           2 1
#           3 2 1
#           4 3 2 1
#           5 5 3 2 1

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()


# assigment 5




# assigment 6


a = 5

# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
#
# for i in range(a - 1, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end= " ")
#     print()



# assigment for reverse the string


# def k(a):
#     return a[::-1]
#
# x = input("Enter your name: ")
#
# out = k(x)
#
# print(out)


# assigment for counting the vowels in string


# assigment to make a calculator


# def cal(n1, op, n2):
#     if op == "+":
#         return n1 + n2
#
#     elif op == "-":
#         return n1 - n2
#
#     elif op == "*":
#         return n1 * n2
#
#     elif op == "/":
#         return n1 / n2
#
#     else:
#         return "operator does not  match "
#
#
# num1 = int(input("Enter a number: "))
# opr = input("Enter a operator: ")
# num2 = int(input("Enter a number: "))
#
# out = cal(num1 , opr , num2)
#
# print(out)



# assigment for palindrome

# def k(pal):
#     if pal == pal[::-1]:
#         return "it is palindrome"
#     else:
#         return "it is not palindrome "
#
# x = input("Enter: ")
# out =k(x)
# print(out)


# assigment to find vowels

# def k(str):
#     vowels = "aeiouAEIOU"
#     counter = 0
#     for i in str:
#         if i in vowels:
#             counter = counter + 1
#     return counter
#
# a = input("Enter a string: ")
# out = k(a)
# print(f"Number of vowels in the string: {out}")

# assigment to check the num is prime

# def k(a):
#     factors = []
#     for i in range(1, a + 1):
#         r = a % i
#         if r == 0:
#             factors.append(i)
#     return factors
#
# a = int(input("Enter any number: "))
# out = k(a)
# print(f"{a} is divisible by {out}")



# assigment

#
# 1 : Create a list of words
# word_list = ["ahmed", "kazim", "abdullah", "ayan"]
#
#  2: Create a string from the list
# word_string = ' '.join(word_list)
#
# 3 : Capitalize the first letter of the entire string
# capitalized_string = word_string.capitalize()
#
#  4 : Find and print the index of the first occurrence of the letter 'a' in the string
# index_of_a = capitalized_string.find('a')
# print(f"Index of 'a': {index_of_a}")
#
# 5 : Count and print the number of occurrences of the letter 'a'
# count_of_a = capitalized_string.count('a')
# print(f"Number of occurrences of 'a': {count_of_a}")
#
#  6 : Replace 'a' with 'x'. Print the modified string
# modified_string = capitalized_string.replace('a', 'b')
# print(f"Modified string after replacing 'a' with 'x': {modified_string}")
#
# 7 : Remove leading and trailing whitespaces. Print the modified string
# trimmed_string = modified_string.strip()
# print(f" removing leading whitespaces: {trimmed_string}")
#
# 8 : Split the string back into a list. Print the resulting list
# resulting_list = trimmed_string.split()
# print(f"Print the resulting list: {resulting_list}")



# assigment


# Ask the user to input a username
# def check_username(username):
#     if len(username) >= 8:
#         if not username[0].isdigit():
#             print("Username is valid.")
#         else:
#             print("Username must not start with a number.")
#     else:
#         print("Username must have at least 8 characters.")
#
# user_username = input("Enter your username: ")
# check_username(user_username)
#
# # Take input as 'a'
# a = input("Enter your username: ")
# name(a)




# assigment for pasword

# a = input("Enter your password: ")
#
# special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?`~"
#
# for i in a:
#     if i in special_characters:
#         if len(a) >= 8 and (i.isupper() for i in a):
#             print("Password strength: Strong")
#         else:
#             print("Password strength: Weak")
#             print("Password should be at least 8 characters long and contain at least one uppercase letter.")




# assigment for utility

# for 1

import random
import string

def generate_password(length=8):
    if length < 8: length = 8
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    for i in range(8))

# for 2

def check_username(username):
    if len(username) >= 8:
        if not username[0].isdigit():
            print("Username is valid.")
            return True
        else:
            print("Username must not start with a number.")
            return False
    else:
        print("Username must have at least 8 characters.")
        return False

# for 3

def valid_email(email):
    if email.find('@') == -1:
        return "Valid email address."
    else:
        return "Invalid email address."

# for 4

import random

def number_guessing_game():
    flag = "red"
    while flag == "red":
        lucky_number = random.randint(1, 10)
        input_value = int(input("Guess a number between 1 and 10: "))
        if input_value == lucky_number:
            print("Congratulations! Your guess is correct.")
            flag = "green"
        else:
            print("Please try again.")

# for 5

def cal(n1, op, n2):
    if op == "+":
        return n1 + n2

    elif op == "-":
        return n1 - n2

    elif op == "*":
        return n1 * n2

    elif op == "/":
        return n1 / n2

    else:
        return "operator does not  match "



a = "1 : generate password"
b = "2 : check valid username"
c = "3 : check valid email address"
d = "4 : play a number guessing game"
e = "5 : calculator"

print(a)
print(b)
print(c)
print(d)
print(e)

flag = "red"
while flag == "red":
    x = input("choose a utility (1-5) : ")

    if x == "1":
        print(f"Generated password: ", generate_password())

    if x == "2":
        user_username = input("Enter your username: ")
        check_username(user_username)

    if x == "3":
        email = input("Enter an email address: ")
        result = valid_email(email)
        print(result)


    if x == "4":
        number_guessing_game()

    if x == "5":
        num1 = int(input("Enter a number: "))
        opr = input("Enter a operator: ")
        num2 = int(input("Enter a number: "))
        result = cal(num1, opr, num2)
        print(f" your answer is {result}")
        flag = "green"
    else:
        print("Please choose a utility between (1-5).")




