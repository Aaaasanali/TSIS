import os
import string


p = r'C:\Users\User\Desktop\Python'
f = open('text.txt', 'r+')

# for i in os.listdir():
#   if os.path.isdir(os.path.join(p, i)):
#     print(os.path.join(p, i))
# print('\n')
# for i in os.listdir():
#   if os.path.isfile(os.path.join(p, i)):
#     print(os.path.join(p, i))
# print('\n')
# for i, dirs, files in os.walk(p):
#   for dir in dirs:
#     print(os.path.join(i, dir))
#   for file in files:
#     print(os.path.join(i, file))
# print('\n')
# print(f.writable())
# print(f.readable())
# print(f.seekable())
# print('\n')
# if os.path.exists(p):
#     directory, filename = os.path.split(p)
#     print("Directory:", directory)
#     print("Filename:", filename)
# else:
#   print('Path does not exist bruh')

# count = 0
# for line in f:
#   count = count+1
# print(count)

# list = ('hello', 'bruh', 'btch', '\nAAAbabaad')
# for i in list:
#   f.write(i)

# for char in string.ascii_uppercase:
#   file_name = char + '.txt'
#   new_file = open(file_name, 'w')

# f1 = open('row.txt', 'r')
# for line in f1:
#   f.write(line)
# for line in f:
#   print(line.strip())

# path_to_remove = r'C:\Users\User\Desktop\Python\dsajkh.txt'
# if os.path.exists(path_to_remove):
#   os.remove(path_to_remove)
# else:
#   print('path does not exist btruhSDA')
