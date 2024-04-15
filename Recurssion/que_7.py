'''
Check Palindrome
You are given a string and you have to tell if it is a Palindrome or not.
Note: A Palindrome is a string that is same when reversed. For example: 'BOB', 
'TENET' are Palindromes, while 'TENT' is not a Palindrome
'''

# cook your dish here
def check_palindrome(s, n):
    #Write your code here
    li = len(s) - 1 - n
    
    if (n > len(s)//2):
        return 'Yes'
    
    if (s[n] != s[li]):
        return 'No'
    
    return check_palindrome(s, n+1)
    
s = input()
print(check_palindrome(s, 0))
