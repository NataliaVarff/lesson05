# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# задача решена

my_tfile = open('my_txt_file.txt', 'w')

if my_tfile.writable():
    strings = [input('your name >> '), input('your city >> '), input('your gender >> ')]
    for i in strings:
        my_tfile.write(i + '\n')
    print(strings)
else:
    print('empty space')


my_tfile.close()

######

my_tfile1 = open('my_txt_file1.txt', 'w')

if my_tfile1.writable():
    strings = ['Nata\n', 'Moscow\n', 'Female\n']
    print(my_tfile1.writelines(strings))
else:
    print('empty space')

my_tfile1.close()



