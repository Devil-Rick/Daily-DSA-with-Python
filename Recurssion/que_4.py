'''
Problem statement
Given an array of length N and an integer x, you need to find if x is 
present in the array or not. Return true or false.
'''

def checkNumber(arr, x):
    if len(arr) == 0:
       return False

    if arr[0] == x:
        return True
    
    smallArr = checkNumber(arr[1:], x)
    return smallArr

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')

