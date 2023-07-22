# c) print the second largest value
import numpy as np

lst = np.random.randint(0, 100, size = (20)).tolist()
first_max = max(lst)
second_max = 0

for i in range(len(lst)):
    if lst[i] > second_max and lst[i] < first_max:
        second_max = lst[i]

print(second_max)