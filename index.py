# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# i = 0
# while  i <= 10:
#     if i % 2 == 1: break
#     print(i)
#     i += 1

# i = 0

# while int(input('Enter number')) >0 :
#     pass 

# for i in range(100000):
#     if int(input('Enter number')) < 0: break


# a = int(input('Enter 1st number:'))
# b = int(input('Enter 2nd number:'))

# if b == 0:
#     i = 1
#     while True:
#         # Если пользователь ввёл 0 большке 3 раз
#         if i > 3:
#             print('Stupid asshole')
#         else: print('aaaaaa!')
#         b = int(input('Enter 2nd number:'))
#         print('Stupid asshole')
#         if b != 0:
#                 print(a / b)
#                 break
#         i+=1
# else:
#     print(a / b)

# a = int(input('Enter 1st number:'))
# while True:
#     try:
#         b = int(input('Enter 2nd number:'))
#         print(a / b)
#         break
#     except:
#          print('Please enter non-zero value')


# a = int(input('Enter 1st number:'))
# b = int(input('Enter 2nd number:'))
# if b == 0
# while True:
#     try:
#         b = int(input('Enter 2nd number:'))
#         if b != 0:
#             print(a / b)
#         break
# else:
#         print(a / b)

# a = int(input('Enter 1st number:'))
# i = 0
# while True:
#     b = int(input('Enter 2nd number:'))
#     try:
#          print(a / b)
#          break
#     except:
#         if i > 3: print('Please enter non-zero value')
#         else: print('Stupid assful')
#         i += 1

# while True:

#     a = int(input('Enter positive number:'))
#     if a >  0: break
#     else: print('You were asked to enter positive number:')


while True:
        try:
         a = int(input('Enter positive number:'))
         if a <  0: raise ValueError('You were asked to enter positive number:')
         else: break
        except ValueError as ve:
            print(ve)
    

