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
# def second(spis_1=[23, 19, 2, 0, 9, 509, 290, 7], spis_2=0):
#     '''Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел. Количество введенных чисел в список и искомая
#     цифра задаются с клавиатуры. Числа выбираются рандомно.'''
#     return spis_1.count(spis_2)
#
# assert second() == 1
# assert second([1, 1, 1, 3145, 2567, 223, 56354, 123, 534, 2, 3, 4, 5, 6, 7, 8, 1], 1) == 4


def thirst (word="HjkyLMu"):
    '''Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
     (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.'''
    verh, niz, glas = 0, 0, 0
    spis = ['a', 'e', 'y', 'u', 'i', 'o', 'A', 'E', 'Y', 'U', 'I', 'O']
    for i in range(len(word) - 1):
        if word[i].isupper() and word[i + 1].isupper():
            verh += 1
        if word[i].islower() and word[i + 1].islower():
            niz += 1
    for i in range(len(word)):
        if spis.count(word[i]) > 0:
            glas += 1
    kol = len(word)
    return {"Bolshie bukvi": verh, "Malenkie bukvi": niz, "Bukv stolko": kol, "Glasnih stoka": glas, "Soglasnih stoka": kol - glas}

assert thirst() == {'Bolshie bukvi': 1, 'Malenkie bukvi': 2, 'Bukv stolko': 7, 'Glasnih stoka': 2, 'Soglasnih stoka': 5}
assert thirst("KAValeriStIBeGali") == {'Bolshie bukvi': 3, 'Malenkie bukvi': 6, 'Bukv stolko': 17, 'Glasnih stoka': 8, 'Soglasnih stoka': 9}
assert thirst("K") == {'Bolshie bukvi': 0, 'Malenkie bukvi': 0, 'Bukv stolko': 1, 'Glasnih stoka': 0, 'Soglasnih stoka': 1}
