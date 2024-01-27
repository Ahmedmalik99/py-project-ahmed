# assigment 1

# q = [5, 4, 2, 7]
#
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))
# d = int(input("enter a number: "))
#
# if q[0] == a:
#     print("index", q[0], "=", a)
#
# else:
#    print ("index does not match")
#
# if q[1] == b:
#     print("index", q[1], "=", b)
# else:
#    print ("index does not match")
#
# if q[2] == c:
#     print("index", q[2], "=", c)
#
# else:
#     print ("index does not match")
#
# if q[3] == d:
#     print("index", q[3], "=", d)
#
# else:
#     print("index does not match")


# assigment 2

# n = 216
# x = str(n)
# z = int(n) % int(x[0])
#
# if z == 0:
#     print("2")
#
# z2 = int(n) % int(x[1])
#
# if z2 == 0:
#     print(1)
#
#
# z3 = int(n) % int(x[2])
#
# if z3 == 0:
#     print(6)




# assigment 3

# for num1

# arr = [90, 100, 78, 89, 67]
#
# a = []
#
# if arr[4] > arr[0]:
#     print(arr[0])
#
# elif arr[4] > arr[1]:
#     print(arr[1])
#
#
# elif arr[4] > arr[2]:
#     print(arr[2])
#
# elif arr[4] > arr[3]:
#     print(arr[3])
#
# else:
#     a.append(arr[4])
#
#
# # for num2
#
# if arr[2] > arr[0]:
#     print(arr[0])
#
# elif arr[2] > arr[1]:
#     print(arr[1])
#
#
# elif arr[2] < arr[4]:
#     print(arr[4])
#
# elif arr[2] > arr[3]:
#     print(arr[3])
#
# else:
#     a.append(arr[2])
#
# # for num3
#
# if arr[3] < arr[3]:
#     print(arr[3])
#
# elif arr[3] > arr[1]:
#     print(arr[1])
#
#
# elif arr[3] < arr[2]:
#     print(arr[2])
#
# elif arr[3] < arr[4]:
#     print(arr[4])
#
# else:
#     a.append(arr[3])
#
#
# # for num4
#
# if arr[0] < arr[3]:
#     print(arr[3])
#
# elif arr[0] > arr[1]:
#     print(arr[1])
#
#
# elif arr[0] < arr[2]:
#     print(arr[2])
#
# elif arr[0] < arr[4]:
#     print(arr[4])
#
# else:
#     a.append(arr[0])
#
# # for num5
#
# if arr[1] < arr[3]:
#     print(arr[3])
#
# elif arr[1] > arr[1]:
#     print(arr[1])
#
#
# elif arr[1] < arr[0]:
#     print(arr[2])
#
# elif arr[1] < arr[4]:
#     print(arr[4])
#
# else:
#     a.append(arr[1])
#
# print(a)
#
#
# len1 = len(a)
#
# print( "lenth of a sorted list is", len1,"so the lenth of a sorted list is odd so the formula for it will be n+1/2")
#
# print (a)
# print("n+1/2")
# len3 = (len1 + 1, "/2")
# print (len3)
# len3 = (len1 + 1)
#
# result = int(len3 / 2)
# print (result)
#
# print("the",result,"value in sorted list is" ,a[2])



# assigment num4


# a = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
#
# b = []
# for num in a:
#     if num not in b:
#         b.append(num)
#
# print("Original List", a)
# print("List without duplicates", b)


# assigment num5

# a = int(input("Enter a number: "))
# b = 0
#
# for digit in str(a):
#     b += int(digit)
#
# print(str(b) == str(b)[::-1])


# assigment num6

# a = [2, 3, 6, 7, 0]
#
# a1 = str(a)
#
# b = input("enter a number: ")
#
# for i in range(len(a1)):
#     if b == a1[i]:
#         print(f"{b} is present in the list at position {i}")



# assigment num7 multiplication table

# Get input from the user
# user_input = int(input("Enter a number: "))
#
# print(f"Multiplication Table for number {user_input}:")
# for i in range(1, 11):
#         result = user_input * i
#         print(f"{user_input} x {i} = {result}")



# assigment num8


# Write a program to take input names of 10 friends and make a list of friend names using for loop.



# b = []
#
# # b = str(b1)
#
# for i in range(1,11):
#     a = input("Enter a name: ")
#     b.append(a)
#
#
# print (b)


# assigment : write a program to add two integer lists using for loop and make another list using append function.


# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
#
# c = []
#
# for i in range(len(a)):
#     c.append(a[i] + b[i])
#
# print(c)


# # assigment : write a program to print the sum of a list elements.
#
#
# a = [4, 5, 3, 8]
#
# b = 0
#
# for i in a :
#     b += i
#
# print(b)



# assigment : Write a program print the even and odd numbers lesser than 100.

# for even numbers
# print("Even numbers less than 100: ")
# for num in range(0 ,100 , 2):
#     print(num , end ="" )
#
# # for odd numbers
#
# print()
# print("Odd numbers less than 100")
# for num in range(1, 100, 2):
#     print(num , end ="" )

# assigment :Write a program to display convert the list of string numbers into list of integers.



# # List of string numbers
# a = ["2", "5", "9"]
#
# b = [int(num) for num in a]
#
# print(b)


#
# # assigment

# for i in "*":
#     for j in range(0, 6, 1):
#         c = " " * (6 - j)
#
#         b = c + i * j
#         print(b)










