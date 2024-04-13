'''
Problem statement
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1
'''


def power_func(a,b):
    if b == 0:
        return 1
    small_output = power_func(a, (b-1))
    output = a * small_output
    return output

a, b = input().split()
a = int(a)
b = int(b)

print(power_func(a,b))