'''
Replace all Occurances of a with b in a string
'''

def rep_String(arr, a, b, si):
    arr = list(arr)
    if len(arr) == si:
        return arr
    
    if arr[si] == a:
        arr[si] = b
    
    n_arr = rep_String(arr, a, b, si+1)
    return (''.join(n_arr))

print(rep_String('aabcchhaabsaa', 'a', 'b', 0))
