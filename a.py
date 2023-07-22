# a) delete elements are on even positions

import numpy as np

lst = np.random.randint(0, 100, size=(50)).astype(str).tolist()
print(lst)
a = np.array(lst).astype(int)
len_a = len(a)
k = 0
n = 0

while k < len_a:
    if k % 2 == 0:
        a = np.delete(a, n)
        n += 1
    k += 1

print(a) 

# or delete even elements of array ???
import numpy as np

lst = np.random.randint(0, 100, size=(100)).astype(str).tolist()
print(lst)
a = np.array(lst).astype(int)
a = [x for x in a if x % 2 != 0]
print(a)
