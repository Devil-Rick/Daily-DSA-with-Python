'''
Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array.
Return -1 if it is not present in the array.
First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.
'''


def firstIndex(arr, x):
    # Please add your code here
    if len(arr) == 0:
        return -1
    if arr[0] == x:
        return 0
    
    smallList = firstIndex(arr[1:], x)
    if smallList == -1:
        return -1
    else:
        return smallList + 1
    
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
