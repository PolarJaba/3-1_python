# f)
# Необходимо выделить все подстроки длиной более 3х символов

input_string = input('Enter any string: ').split()
sub_string = []

for word in input_string:
    # строки менее 3х символов не учитываются
    if len(word) < 3:
        pass
    # строка длиной три будет единственной подстрокой
    elif len(word) == 3:
        sub_string.append(word)
    # подсчет всех подстрок остальных слов, включая слово целиком
    else:
        k = len(word) - 2
        n = 0
        while n < k:
            sub_string.append(word[n]+word[n+1]+word[n+2])
            if k-n != 1:
                sub_string.append(word[n:])
            n += 1

print(sub_string)
print(input_string)