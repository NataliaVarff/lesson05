# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Задача решена

with open('file5.txt','w') as file5:
    file5.write("1 2 3 4")


with open('file5.txt', 'r') as file5:
    a = list(file5.readline().split( ))
    a_int = [int(n) for n in a]
    print(a)
    print(a_int)
    x = sum(a_int, start=0)
    print(f'result is {x}')



