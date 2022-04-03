# 1
from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Inpute time work: "))
    rate = int(input("Inpute ratet: "))
    prize = int(input("Inpute prize: "))
    print((time_work * rate) + prize)

# или


# 1
def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()





# 2
my_list = [ 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]

print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')





# 3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')




# 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')




# 5
from functools import reduce


def my_func(el_p, el):
     return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')






# 6
from itertools import cycle, count

v_start = int(input('Start number: '))
v_stop = v_start * 2 + 10 + 1

# v.1
for i in count(v_start):
    if i < v_stop:
        print(i)
    else:
        break
del i

# v.2
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break







# 7


