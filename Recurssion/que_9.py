'''
Problem statement
Given a string, compute recursively a new string where all 'x' chars have been removed.
'''

def removeX(string):
    if len(string) == 0:
        return string
    smallOut = removeX(string[1:])
    if string[0] == 'x':
        return '' + smallOut
    else:
        return string[0] + smallOut

# Main
string = input()
print(removeX(string))

