'''
Problem statement
Given an array of length N and an integer x, you need to find and return the last index of 
integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, 
return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def last_index(arr, ele, si):
    if len(arr) == si:
        return -1
    
    smallList = last_index(arr, ele, si+1)
    if smallList != -1:
        return smallList
    else:
        if arr[si] == ele:
            return si
        return -1


x = int(input())
arr = list(int(i) for i in input().strip().split(' '))
ele = int(input())
print(last_index(arr, ele, 0))