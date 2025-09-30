
# todo Escriba una funcion que reciba dos numeros y devuelva su MCD

import math

# def MCD(one, two):
#     if one < 0:
#         print(f"The numbers entered cannot be less than zero and cannot be negative")
#         return

#     if two < 0:
#         print(f"The numbers entered cannot be less than zero and cannot be negetive")
#         return

#     a = abs(one)
#     b = abs(two)

#     # ? Ensure that 'No' is the largest number.
#     if b > a:
#         a, b = a, b
#         # ? The cycle continues as long as b is not zero.
#     while b:
#         # ? Trade a for b, and b for the remainder of a % b
#         a, b = b, a % b
#     return a


# numOne = 48
# numTwo = 18

# print(f"The MCD of {numOne} and {numTwo} is: {MCD(numOne, numTwo)}")

num1 = 48
num2 = 18
print(f"The MCD of {num1} and {num2} is: {math.gcd(num1, num2)}")
