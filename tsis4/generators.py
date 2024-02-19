# N = 4
# gen = [i**2 for i in range(N)]
# print(gen)

#------------------------------------------------------
# n = int(input())
# gen = [str(i) for i in range(n) if i%2 == 0]
# print(', '.join(gen))

#------------------------------------------------------
# def generator(n):
#     gen = [i for i in range(0, n) if i%3 == 0 or i%4 == 0]
#     return gen

# print(generator(12))

#------------------------------------------------------
# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2

# for num in squares(1, 5):
#     print(num)

#------------------------------------------------------
# n = 10

# a = [i for i in range(10, -1, -1)]
# print(a)
