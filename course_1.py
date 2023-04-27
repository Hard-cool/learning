from random import randint
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


# def thirst (word="HjkyLMu"):
#     '''Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
#      (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.'''
#     verh, niz, glas = 0, 0, 0
#     spis = ['a', 'e', 'y', 'u', 'i', 'o', 'A', 'E', 'Y', 'U', 'I', 'O']
#     for i in range(len(word) - 1):
#         if word[i].isupper() and word[i + 1].isupper():
#             verh += 1
#         if word[i].islower() and word[i + 1].islower():
#             niz += 1
#     for i in range(len(word)):
#         if spis.count(word[i]) > 0:
#             glas += 1
#     kol = len(word)
#     return {"Bolshie bukvi": verh, "Malenkie bukvi": niz, "Bukv stolko": kol, "Glasnih stoka": glas, "Soglasnih stoka": kol - glas}
#
# assert thirst() == {'Bolshie bukvi': 1, 'Malenkie bukvi': 2, 'Bukv stolko': 7, 'Glasnih stoka': 2, 'Soglasnih stoka': 5}
# assert thirst("KAValeriStIBeGali") == {'Bolshie bukvi': 3, 'Malenkie bukvi': 6, 'Bukv stolko': 17, 'Glasnih stoka': 8, 'Soglasnih stoka': 9}
# assert thirst("K") == {'Bolshie bukvi': 0, 'Malenkie bukvi': 0, 'Bukv stolko': 1, 'Glasnih stoka': 0, 'Soglasnih stoka': 1}

# def fourth(spis_elem=[1, 10, 83, 29, 29, 1, "d", "artem", "qwerty", "qwerty"]):
#     '''Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#     Элементы нужно выводить в том порядке, в котором они встречаются в списке.'''
#     otvet = []
#     for el in spis_elem:
#         if spis_elem.count(el) == 1:
#             otvet.append(el)
#     return otvet
# assert fourth() == [10, 83, "d", "artem"]
# assert fourth(['jskhdf1', 190, 190, 190, 20, 'fd', 'fd', 'a']) == ['jskhdf1', 20, 'a']
def perebor(kort):

    sum, max, min = 0, 0, kort[randint(0, len(kort))]
    for el in kort:
        sum += el
        if el > max:
            max = el
        if el < min:
            min = el
    return sum, kort.index(max) + 1, kort.index(min) + 1

def fifth(kort_1=(35, 78, 21, 37, 2, 98, 6, 100, 231), kort_2=(45, 21, 124, 76, 5, 23, 91, 234)):
    '''Даны два кортежа:
    C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
    C_2 = (45, 21,124,76,5,23,91,234)
    Необходимо определить:
    1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
    2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей'''
    sum_1, sum_2, max_1, max_2, min_1, min_2 = 0, 0, 0, 0, 0, 0
    sum_1, max_1, min_1 = perebor(kort_1)
    sum_2, max_2, min_2 = perebor(kort_2)
    if sum_1 > sum_2:
        print('Сумма больше в кортеже - 1')
    else:
        print('Сумма больше в кортеже - 2')
    print('В первом кортеже порядковый номер минимального числа = {}, а максимального = {}'.format(min_1, max_1))
    print('Во втором кортеже порядковый номер минимального числа = {}, а максимального = {}'.format(min_2, max_2))

fifth()