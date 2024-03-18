import csv

with open("students.csv", encoding = "utf8") as file:
    reader = csv.reader(file, delimiter=",")
    data = list(reader)[1:]
    class_members = {}
    class_sum = {}
    for id, name, titleProject_id, clasS, score in data:
        if "Хадаров Владимир" in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
        if score != "None":
            score = int(score)
        else:
            score = 0
        class_members[clasS] = class_members.get(clasS, 0) + 1
        class_sum[clasS] = class_sum.get(clasS, 0) + score
    for student in data:
        if student[-1] == "None":
            student[-1] = round(class_sum[student[-2]] / class_members[student[-2]], 3)

with open("students_new.csv", "w", encoding = "utf8", newline = "") as file:
    new = csv.writer(file)
    new.writerow(["id","Name","titleProject_id","class","score"])
    new.writerows(data)