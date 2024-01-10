# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран. 

import random
import threading

lst = []

def find_sum(arr):
    summ = sum(arr)
    print(summ)
    return summ

def avg(arr):
    avarage = sum(arr) / len(arr)
    print(avarage)
    return avarage

def random_fill():
    global lst
    lst = [random.randint(0,100) for _ in range(10)]
    print(lst)
    return lst



t1 = threading.Thread(target=random_fill)


t1.start()

t1.join()

t2 = threading.Thread(target=find_sum, args=(lst, ))
t3 = threading.Thread(target=avg, args=(lst, ))

t2.start()
t3.start()

t2.join()
t3.join()