###########  1
def div(*args):
    try:
        arg1 = int(input("введи число q "))
        arg2 = int(input("введи число z "))
        res = arg1 / arg2
    except ValueError:
        return 'ошибка! только число'
    except ZeroDivisionError:
        return "не правильное число z! на ноль делить нельзя"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("на ноль делить нельзя")
    '''


print(f'result  {div()}')



#############  2
'''
name = input('укажи имя')
surname = input('укажи фамилию')
year = int(input('год рождения'))
city = input('место жительства')
email = input('email')
telephone = input('какой телефон')
'''
def my_func (name, surname, year, city, email, telephone):
      return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name = 'Гоша', surname = 'Литвак', year = '1979', city = 'Орел', email = '123@mail.ru', telephone = '565-565-565'))



############ 3
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')



############# 4
def my_func(x, y):
    return 1 / x ** abs(y)
    # return x ** y


print(my_func(2, -3))


##############  6
def int_func(*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()



############  5
import sys

result = 0
while True:
     line = input("Enter number or special token q fo exite: ")
     tokens = line.split(" ")
     for token in tokens:
         try:
             number = float(token)
             result += number
         except:
             if token == 'q':
                 print(f"You sum is {result}. Program is terminated")
                 exit(0)
             else:
                 print(f"You sum is {result}. Input error", file=sys.stderr)
                 exit(1)
#print(result)
# #exit()




##############  6
def int_func(*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()