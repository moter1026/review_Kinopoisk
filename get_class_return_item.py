import os
import csv
import pandas as pd


def get_class_return_item(class_name):
    if (os.path.exists("return_path.csv")):
        lines_of_class = 0
        names_of_files = []
        with open("return_path.csv", "r", encoding="utf-8") as readFile:
            read = csv.DictReader(readFile)
            for i, row in enumerate(read):
                names_of_files.append(row["Возвращённый путь до файла"])
                if class_name == row["Класс"]:
                    lines_of_class = lines_of_class + 1


        path = None
        file_class = 0
        with open("description_three_random.csv", "r", encoding='utf-8') as csvFile:
            read = csv.DictReader(csvFile)
            count = 0
            name_exists = False
            for i, row in enumerate(read, start=0):
                if row["метка класса"] == class_name:
                    if count == lines_of_class or name_exists == True:
                        # Проверка на выдачу до этого данного пути файла
                        if row["абсолютный путь к файлу"] in names_of_files:
                            name_exists = True
                            continue
                        path = row["абсолютный путь к файлу"]
                        file_class = row["метка класса"]
                    count = count + 1

        if path != None:     
            with open("return_path.csv", "a", encoding='utf-8') as TextFile:
                writer = csv.writer(TextFile, delimiter=",")
                writer.writerow([path, file_class])
        

        return path

    else:
        with open("return_path.csv", "w+", encoding='utf-8') as TextFile:
            writer = csv.writer(TextFile, delimiter=",")
            writer.writerow(["Возвращённый путь до файла", "Класс"])
        get_class_return_item(class_name)

print(get_class_return_item("good"))