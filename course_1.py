import random
# def first():
#     ''' С клавиатуры вводится 7-значное число. Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 цифры.'''
#     chislo = input("7-значное число")
#     chet, nechet, a, j = 0, 0, 0, 0
#     spis = []
#     for i in chislo:
#         i = int(i)
#         j += 1
#         a += i
#         if j == 1 or j == 3 or j == 6:
#             spis.append(i)
#         if i % 2 == 0:
#             chet += 1
#         else:
#             nechet += 1
#     if chet > nechet:
#         print(a)
#     else: print(spis[0] * spis[1] * spis[2])
#
# first()

'''def test_first(chislo="1234567"):
    chet = 0
    nechet = 0

    for el in chislo:
       if int(el) % 2 == 0:
           chet += 1
       else:
           nechet += 1
    if chet > nechet:
       return sum([int(el) for el in chislo])
    else:
       return int(chislo[0]) * int(chislo[2]) * int(chislo[5])

assert test_first() == 18
assert test_first("2345678") == 35'''


def second(spis_1=[23, 19, 2, 0, 9, 509, 290, 7], spis_2=0):
    '''Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел. Количество введенных чисел в список и искомая
    цифра задаются с клавиатуры. Числа выбираются рандомно.'''
    return spis_1.count(spis_2)

assert second() == 1
assert second([1, 1, 1, 3145, 2567, 223, 56354, 123, 534, 2, 3, 4, 5, 6, 7, 8, 1], 1) == 4