# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

# txt_file3.txt
# Задача решена


with open('txt_file3.txt', 'r', encoding='utf-8') as file3:
    sal = []
    poor = []
    my_list = file3.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append((i[0]))
        sal.append(i[1])
print(f'Фамилии сотрудников с окладом меньше 20000р.:{poor}')
# print(sal)
# print(len(sal))
aver_sal = sum((int(n) for n in sal), start=0) / len(sal)
print(f'Средняя величина дохода : {aver_sal}')




