import csv

with open("students.csv", encoding = "utf8") as file:
    reader = csv.reader(file, delimiter=",")
    data = list(reader)[1:]
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while (float(data[j]['score']) if data[j]['score'] != 'None' else 0) < (float(key[j]['score']) if key[j]['score'] != 'None' else 0):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key