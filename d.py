# d) delete all duplicates from list
# this method works with any lst content 
# (for example lst = ['hello', 1, 7, 7, 'hi', [1, 2], 10, 'hello', [1, 2], [3, 1]]) 
import numpy as np

lst = np.random.randint(0, 10, size=(10)).astype(str).tolist()
print(lst)

def del_duplicates(n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    return l

returned = del_duplicates(lst)

print(returned)