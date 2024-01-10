# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран.

import os
import shutil

def copy_directory_structure(source_path, destination_path):
    try:
        
        items = os.listdir(source_path)

        
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        
        for item in items:
            
            source_item_path = os.path.join(source_path, item)
            destination_item_path = os.path.join(destination_path, item)

            
            if os.path.isdir(source_item_path):
                copy_directory_structure(source_item_path, destination_item_path)
            
            elif os.path.isfile(source_item_path):
                shutil.copy2(source_item_path, destination_item_path)

        print(f"Directory structure from '{source_path}' copied to '{destination_path}' successfully.")

    except Exception as e:
        print(f"Error: {e}")


source_directory = input("enter source directory path: ")
destination_directory = input("enter destination directory path: ")


copy_directory_structure(source_directory, destination_directory)
