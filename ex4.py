# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом
# і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу
# із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.
import threading
import os

PATH = 'dir'
word = 'joy'

def search_files(path, word):
    matching_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, 'r', encoding='utf-8') as rfile:
                    content = rfile.read()
                    if word in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")
    all_text = []    
    for file in matching_files:
        with open(file, 'r', encoding="UTF-8") as rfile:
            content = rfile.read()
            all_text.append(content)
    
    with open("res.txt", 'w', encoding="UTF-8") as wfile:
        wfile.write(str(all_text))


def remove_forbidden(file, fbd_file):
    
    with open(fbd_file, 'r', encoding="UTF-8") as rfile:
        forbidden_words = [line.strip() for line in rfile.readlines()]

    with open(file, 'r', encoding="UTF-8") as wfile:
        curr_data = wfile.read()

    
    for forbidden_word in forbidden_words:
        curr_data = curr_data.replace(forbidden_word, '*')

    with open(file, 'w', encoding="UTF-8") as wfile:
        wfile.write(curr_data)
t1 = threading.Thread(target=search_files, args=(PATH, word))

remove_forbidden('res.txt', 'dir\\forbidden.txt')
# t1.start()
# t1.join()



