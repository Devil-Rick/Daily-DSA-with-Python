'''
Problem statement
Given a string S, remove consecutive duplicates from it recursively.
'''

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == string[1]:
        smallOut = removeConsecutiveDuplicates(string[1:])
        return smallOut
    else:
        smallOut = removeConsecutiveDuplicates(string[1:])
        return string[0] + smallOut

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))