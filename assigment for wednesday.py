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

def k(pal):
    if pal == pal[::-1]:
        return "it is palindrome"
    else:
        return "it is not palindrome "

x = input("Enter: ")
out =k(x)
print(out)


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
