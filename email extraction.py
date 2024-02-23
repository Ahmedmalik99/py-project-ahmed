# import re
# with open("regex.txt","r") as f:
#     text = f.read()
#     pattern = 'From:.+'
#     matches = re.findall(pattern, text)
#     for i in matches:
#      print(i)
#
# reg = 'From:\s.\s+'
# matches = re.findall(reg, i)
#
# print(matches)

# import re
#
# with open("regex.txt", "r") as f:
#     text = f.read()
#     pattern =  'From: (.+) <(.+)>'
#     matches = re.findall(pattern, text)
#     for i, j in matches:
#         print("Username:", i)
#         print("Email:", j)

# import re
#
# with open("regex.txt", "r") as f:
#     text = f.read()
#     pattern = ' From: (.+) <(.+)>'
#     matches = re.findall(pattern, text)
#     for i in matches:
#         print("Username: ", i )
#
#     for j in matches:
#         print("Email: ", j )






# class shapes :
#     def __init__(self,l,w):
#         self.lenth = l
#         self.width = w
#
#     def draw (self):
#
#         print(f"{self.lenth * self.width}")
#
# shape1 = shapes(10,15)
#
# shape1.draw()