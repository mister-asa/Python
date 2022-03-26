# 1
my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
     my_f.writelines(line)
     line = input('Введите текст \n')
     if not line:
         break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()




# 2
my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n{content}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
     print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()





# 3
with open('sal.txt', 'r') as my_file:
     sal = []
     poor = []
     my_list = my_file.read().split('\n')
     for i in my_list:
         i = i.split()
         if int(i[1]) < 20000:
            poor.append(i[0])
         sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')





# 4
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file_4.txt', 'r') as file_obj:
     #content = file_obj.read().split('\n')
     for i in file_obj:
         i = i.split(' ', 1)
         new_file.append(rus[i[0]] + '  ' + i[1])
     print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
     file_obj_2.writelines(new_file)





# 5
def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()






# 6 получилось решить только при вводе чисел без знаков и букв

#import json

subj = {}
with open('file_6.txt', 'r') as init_f:
     for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(int(lecture) + int(practice) + int(lab))
print(f'Общее количество часов по предмету - \n {subj}')






# 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
     for line in file:
         name, firm, earning, damage = line.split()
         profit[name] = int(earning) - int(damage)
         if profit.setdefault(name) >= 0:
             prof = prof + profit.setdefault(name)
             i += 1
     if i != 0:
         prof_aver = prof / i
         print(f'Прибыль средняя - {prof_aver:.2f}')
     else:
         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
     pr = {'средняя прибыль': round(prof_aver)}
     profit.update(pr)
     print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
     json.dump(profit, write_js)

     js_str = json.dumps(profit)
     print(f'Создан файл с расширением json со следующим содержимым: \n '
            f' {js_str}')