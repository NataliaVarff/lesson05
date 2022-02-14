# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# задача решена.

# txt_file2

with open('txt_file2.txt') as file2:
        print(file2.read())


# подсчет количества строк
with open('txt_file2.txt', 'r') as file2:
    spisok = (file2.readlines())
    stroki = len(spisok)
    print(f'Количество строк в файле: {stroki}')

# подсчет количества слов в строках
with open('txt_file2.txt', 'r') as file2:
    line = ()
    for line in file2:
        words = len(line.split( ))
        print(f'Количество слов в строке: {words}')

