'''
Problem Statement
Check if a list id sorted or not
'''
def check_list(x):
    if len(x) == 0 or len(x) == 1:
        return True
    if x[0] > x[1]:
        return False
    smallList = check_list(x[1:])
    return smallList
    
print(check_list([1, 2, 3, 4, 5]))
