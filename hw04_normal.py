import re
import os


def filter_(string):
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z']
    result = []
    add_list = ''
    for i in string:
        if i not in alphabet_upper:
            add_list += i
        elif add_list != '':
            result.append(add_list)
            add_list = ''
        else:
            continue
    result.append(add_list)
    return result


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# string_lower = r'[a-z]{1,10}'
# a = re.findall(string_lower, line)
# print(a, '\n')
#
# b = filter_(line)
# print(b)
#
# print(len(a))
# print(len(filter_(line)))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
         'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
         'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
         'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
         'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
         'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
         'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
         'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
         'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
         'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
         'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
         'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
         'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
         'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
         'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

"""***********************************************"""
string_upper = r'[a-z]{2}[A-Z]{1,}[A-Z]{2}'
string_upper_2 = r'[A-Z]{1,}'
a = re.findall(string_upper, line_2)

b = []
for i in a:
    b.extend(re.findall(string_upper_2, i))
b = [i[0:-2] for i in b]

print(b, '\n')
"""***********************************************"""

line_2_str = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)

print('Список с использованием модуля re: \n',line_2_str)

symbol_1 = list(map(lambda x: chr(x), list(range(65, 91))))
symbol_2 = list(map(lambda x: chr(x), list(range(97, 123))))
line_new = list(line_2)

lst = []
i = len(line_new) - 1

while i >= 0:
    if line_new[i] in symbol_2:
        lst.append(line_new[i])
    elif line_new[i] in symbol_1 and i <= len(line_new) - 3 and line_new[i + 1] in symbol_1 and line_new[
        i + 2] in symbol_1:
        lst.append(line_new[i])
    else:
        lst.append(' ')
    i -= 1
lst.reverse()

i = 0
lst2 = []
register = True

while i <= len(lst) - 1:
    if lst[i] in symbol_2:
        register = True
    if lst[i] in symbol_1 and lst[i - 1] in symbol_2 and lst[i - 2] in symbol_2:
        lst2.append(lst[i])
        register = False
    elif lst[i] in symbol_1 and register == False:
        lst2.append(lst[i])
    else:
        lst2.append(' ')
    i += 1
str_2 = ''.join(lst2).split(' ')

line_str_3 = [i for i in str_2 if i != '']
print('Список без использованием модуля re: \n', line_str_3)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random

count_num = 2500

num_list = [random.randint(0, 9) for _ in range(count_num)]
new_list = ''.join(list(map(lambda x: str(x), num_list)))

print(new_list)

path = os.path.join('files', 'Task-3.txt')

with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(new_list))

with open(path, 'r', encoding='UTF-8') as file:
    task_line = file.read()

help_1 = [0, 0]
help_2 = [task_line[0], task_line[0]]

for i in task_line:
   if i == help_2[1]:
      help_1[1] += 1
      if help_1[1] > help_1[0]:
         help_1[0] = help_1[1]
         help_2[0] = help_2[1]
   else:
      help_1[1] = 1
      help_2[1] = i
print(str(help_1[0]) * int(help_2[0]))

with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(new_list) + '\n')
    file.write(str(help_1[0]) * int(help_2[0]))
