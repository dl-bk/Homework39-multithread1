# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.

import threading
import random
import os
import math


FILE = "nums.txt"

def random_fill(filepath):
    lst = [random.randint(0, 100) for _ in range(10)]
    with open(filepath, 'w', encoding='UTF-8') as wfile:
        for num in lst:
            wfile.write(str(num) + '\n')

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_file(file_path_r, file_path_w):
    primes = []
    try:
        with open(file_path_r, 'r') as rfile:
            for line in rfile:
                number = int(line.strip())
                if is_prime(number):
                    primes.append(number)
        
        with open(file_path_w, 'w') as wfile:
            for num in primes:
                wfile.write(str(num) + "\n")
    except FileNotFoundError:
        print(f"File '{file_path_r}' not found.")

def factor(file_path_r, file_path_w):
    factorials = []
    with open(file_path_r, 'r') as rfile:
        for line in rfile:
            number = int(line.strip())
            factorials.append(math.factorial(number))
    
    with open(file_path_w, 'w') as wfile:
        for num in factorials:
            wfile.write(str(num) + "\n")

fill_thread = threading.Thread(target=random_fill, args=(FILE, ))

fill_thread.start()
fill_thread.join()

primes_thread = threading.Thread(target=find_primes_in_file, args=('nums.txt', 'primes.txt'))
factorials_thread = threading.Thread(target=factor, args=('nums.txt', 'factorials.txt'))

primes_thread.start()
factorials_thread.start()

primes_thread.join()
factorials_thread.join()

 