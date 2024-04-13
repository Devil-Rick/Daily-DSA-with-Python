'''
Problem statement
Given an array of length N, you need to find and 
return the sum of all elements of the array.
'''

def sumArray(arr):
    # Please add your code here
    if len(arr) == 0:
        return 0
    
    smallArr = sumArray(arr[1:])
    return arr[0] + smallArr

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
