import csv


def get_top_performers(file_path, number_of_top_students=5):
    text = []
    top_students = []

    with open(file_path,'r') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")

        for string in file_reader:
            text.append(string)

    sorted_text = sorted(text, reverse=True, key=lambda x: x[2])
    for i in range(number_of_top_students+1):
        if i == 0:
            continue
        top_students.append(sorted_text[i][0])
    return top_students



def sort_by_age(file_path):

    with open(file_path, 'r') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")

        for string in file_reader:
                text.append(string)

    sorted_text = sorted(text, reverse=True, key=lambda x: x[1])

    with open("data/sort_students.csv", "w", newline='') as r_file:

        writer = csv.writer(r_file, delimiter=';')

        for i in noveishii_spisok:
            writer.writerow(i)

        with open("data/sort_students.csv", "w") as f:
            writer = csv.writer(f)
            for elem in sorted_st:
                writer.writerow(elem)
