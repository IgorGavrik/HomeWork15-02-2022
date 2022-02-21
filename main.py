# 10.1. Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
# with open('text1.txt') as my_file:
#     print(f"Печать первой строки файла\n{my_file.readline()}")
# with open('text1.txt') as my_file:
#     line = my_file.readlines()
#     print(f"Печать 5-ой строки\n{line[4]}")
# with open('text1.txt') as my_file:
#     line = my_file.readlines()
#     print("Печать первых пяти строк")
#     for i in range(5):
#         print(line[i])
# with open('text1.txt') as my_file:
#     line = my_file.readlines()
#     print("Печать s1-й по s2-ю")
#     for i in range(2):
#         print(line[i])
# with open('text1.txt') as my_file:
#     print(f"Печать всего файла\n{my_file.read()}\n")

# 10.02. Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
# n = int(input("Введите количество добавляемых записей: "))
# with open('6strok.txt', 'w') as my_file:
#     my_file.writelines([input("Введите строки: ")+"\n" for i in range(n)])
# with open('6strok.txt') as my_file:
#     print(my_file.read())

# 10.03. В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
# with open('test.txt') as my_file:
#     print(f'Содержимое файла до ввода трёх дополнительных строк\n{my_file.read()}')
# with open('test.txt', 'a') as my_file:
#     my_file.writelines([input("Введите новую строку: ")+"\n" for i in range(3)])
# with open('test.txt') as my_file:
#     print(f'Содержимое файла после ввода трёх дополнительных строк\n{my_file.read()}')

# 10.04. Имеется текстовый файл. Переписать в другой файл все
# его строки с заменой в них символа 0 на символ 1 и
# наоборот.
# with open('test.txt') as my_file:
#     print("Печать исходного файла\n", my_file.read())
# new = []
# with open('test.txt') as my_file:
#     for line in my_file.readlines():
#         nst = ""
#         for i in line:
#             if i=="0":
#                 nst = nst+"1"
#             elif i=="1":
#                 nst = nst+"0"
#             else:
#                 nst = nst + i
#         new.append(nst)
# with open('newfile.txt', "w") as my_file_new:
#     my_file_new.writelines(new)
# with open('newfile.txt') as my_file_new:
#     print("Печать изменённого файла\n", my_file_new.read())

# # 10.05. Имеется текстовый файл. Все четные строки этого файла
# # записать во второй файл, а нечетные — в третий файл.
# # Порядок следования строк сохраняется.
# with open('text2.txt') as my_file:
#     a = my_file.readlines()
#     print(f"Имеется текстовый файл:\n{a}")
#     for i in range(len(a)):
#         if (i+1)%2>0:
#             with open('third_file.txt', 'a') as third_file:
#                 third_file.writelines(a[i])
#         else:
#             with open('second_file.txt', 'a') as second_file:
#                 second_file.writelines(a[i])
# with open('second_file.txt') as second_file:
#     print(f"\nСодержимое второго файла с чётными строками первого:\n"
#           f"{second_file.readlines()}")
# with open('third_file.txt') as third_file:
#     print(f"\nСодержимое третьего файла с нечётными строками первого:\n"
#           f"{third_file.readlines()}")

# 10.06. Имеются два текстовых файла с одинаковым числом
# строк. Выяснить, совпадают ли их строки. Если нет, то
# получить номер первой строки, в которой эти файлы
# отличаются друг от друга.
# with open('text1.txt') as my_file:
#     print(f"Печать исходного файла {my_file.name}\n{my_file.read()}\n")
# with open('text2.txt') as my_file:
#     print(f"Печать исходного файла {my_file.name}\n{my_file.read()}\n")
# with open('text1.txt') as my_file:
#     a = my_file.readlines()
# with open('text2.txt') as my_file:
#     b = my_file.readlines()
# for i in range(len(a)):
#     if not a[i]==b[i]:
#         print(f"Файлы не совпадают в {i+1} строке")
#         break
