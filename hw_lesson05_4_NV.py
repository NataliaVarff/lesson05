# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Задача решена


file = open('txt_file4.txt','r')
lst = file.readlines()
lst2=[]
rus = ['Один', 'Два', 'Три', 'Четыре']
eng = ['One', 'Two', 'Three','Four']
p = 0
for i in lst:
    lst2.append(i.replace(eng[p], rus[p]))
    p += 1
file2 = open('txt_file4upd.txt', 'w')
file2.writelines(lst2)
file.close()
file2.close()



