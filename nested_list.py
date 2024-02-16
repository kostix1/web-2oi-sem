def nested_list(N):

    students = []

    for _ in range(N):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])
    students.sort(key=lambda x: x[1], reverse=True)
    second_highest_score = students[1][1]


    second_highest_students = [student[0] for student in students if student[1] == second_highest_score]

    second_highest_students.sort()
    for name in second_highest_students:
        print(name)
