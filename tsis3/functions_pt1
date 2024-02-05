# import random
# def convertToGrams(ounces):
#   return 28.3495231 * ounces

# print(convertToGrams(7))

# ---------------------------
# def convertToCentigrade(F):
#     return (5 / 9)*(F-32)
# temp = 2
# print(convertToCentigrade(temp))

#-----------------------------
# def solve(numheads, numlegs):
#     rabbits = int((numlegs - numheads*2)/2)
#     chicken = int(numheads - rabbits)
#     return rabbits, chicken
# print(solve(35, 94))

#------------------------------
# def isPrime(el):
#    if(type(el) == str):
#       return False
#    if(el == 1):
#       return True
#    elif el > 1:
#       for i in range(2, el):
#         if el%i == 0:
#           return False
#    return True
      
# def filter_prime(list):
#   res = []
#   for i in list:
#       if(isPrime(i)):
#          res.append(i)
#   return res

# list = [2, " ", 4, " ", 5, " ", 6, " ", 7, " ", 9, " ", 13]
# print(filter_prime(list))

#--------------------------------
# def permute(data, i, length): 
#     if i==length: 
#         print(''.join(data))
#     else: 
#         for j in range(i,length):
#             data[i], data[j] = data[j], data[i] 
#             permute(data, i+1, length) 
#             data[i], data[j] = data[j], data[i]
  
       
# string = str(input())
# length = len(string)
# data = list(string)
# i = 0
# permute(data, i, length)


#--------------------------------------
# def reverse(st):
#     sent = st.split()
#     res = ''
#     for i in range(len(sent)-1, -1, -1):
#         res += str(sent[i]) + " "
#     return res  
# s = str(input())
# print(reverse(s))


#---------------------------------------
# def has_33(nums):
#     count = 0
#     for i in nums:
#         if i == 3:
#             count = count+1
#         else:
#             count = 0
#         if count == 2:
#             return True
#     return False
            

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 3, 3]))


#-------------------------------------
# def spy_game(nums):
#     count = 0
#     for i in nums:
#         if i == 0 and count != 2:
#             count = count+1
#         if i == 7 and count == 2:
#             return True
#     return False
          

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))


#------------------------------------
# def volume(R):
#     return 4/3 * 3.14 * R**3

# print(volume(4))


#------------------------------------
# def isUnique(item, list):
#     count = 0
#     for i in list:
#         if item == i and count == 0:
#             count = count+1
#         elif item == i and count == 1:
#             return False
#     return True
# def filter(list):
#     res = []
#     for i in list:
#         if isUnique(i, list):
#             res.append(i)
#     return res
    
# list = ["bruh", "bruh", "hi", "hi", 2]
# print(filter(list))


#-------------------------------
# def isPalindrome(string):
#     if string == string[::-1]:
#         return True
#     return False
# s = "cocain"
# print(isPalindrome(s))


#-----------------------------
# def histogram(list):
#     for i in list:
#         print("*"*i)

# list = [1, 2, 3, 4, 7]
# histogram(list)


#-----------------------------
# name = input("Hello! What is your name?\n")
# print("Well,", name + ", I am thinking of a number between 1 and 20.")
# randomNum = random.randint(1, 20)
# count = 0
# while True:
#     num = int(input("Take a guess.\n"))
#     if num > randomNum:
#         print("Your guess is too high.")
#         count = count+1
#     elif num == randomNum:
#         count = count+1
#         break
#     else:
#         print("Your guess is too low.")
#         count = count+1
# print("Good job,", name + ", You guessed my number in", count, "guesses!")
      
