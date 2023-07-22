# b) find all words with vowels amount more than 3
import re

lst = ['main', 'string', 'input', 'hero', 'cut', 'creation', 'CREATION']
vowels = r'\b(?:\w*[aeiou]){4,}\w*'
lst_txt = str(lst)
print(re.findall(vowels, lst_txt, re.I))