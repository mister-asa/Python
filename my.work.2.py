############### 1
my_list = [-8, True, 92, 'True', 11.1, None]
def my_type(el):
     for el in range(len(my_list)):
         print(type(my_list[el]))
     return
my_type(my_list)

################ 2
el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
     my_list.append(input("Введите следующее значение списка "))
     i += 1

for elem in range(int(len(my_list)/2)):
         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
         el += 2
print(my_list)

############## 3
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
         print(seasons_dict.get(1))
         print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
     print(seasons_dict.get(2))
     print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
     print(seasons_dict.get(3))
     print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
     print(seasons_dict.get(4))
     print(seasons_list[3])
else:
         print("Такого месяца не существует")


############## 4
my_str = input("введите строку ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
     my_word = my_str.split()
     if len(str(my_word)) <= 10:
         print(f" {num} {my_word [el]}")
         num += 1
     else:
         print(f" {num} {my_word [el] [0:10]}")
         num += 1


############## 5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
     for el in range(len(my_list)):
         if my_list[el] == digit:
             my_list.insert(el + 1, digit)
             break
         elif my_list[0] < digit:
             my_list.insert(0, digit)
         elif my_list[-1] > digit:
             my_list.append(digit)
         elif my_list[el] > digit and my_list[el + 1] < digit:
             my_list.insert(el + 1, digit)
     print(f"текущий список - {my_list}")
     digit = int(input("Введите число "))


############## 6
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
     control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
     if control == 'Q':
         break
     num += 1
     if control == 'A':
         print(f'\n Current analytics \n {"-" * 30}')
         for key, value in analytics.items():
             print(f'{key[:25]:>30}: {value}')
             print("-" * 30)
     for f in features.keys():
         feature_ = input(f'Input feature "{f}"')
         features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
         analytics[f].append(features[f])
     goods.append((num, features))




goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
     my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                     'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
     my_list.append((n, my_dict))
     n += 1
     my_analys = dict(
         {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
          'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)