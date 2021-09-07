def create_students_list(n):
    students = []
    for i in range(n):
        aux = []
        name = str(input())
        grade = float(input())

        aux.append(grade)
        aux.append(name)

        students.append(aux)

    return students

def create_lowest_grade_list(students):
    x = sorted(students)
    slg = []

    try:
        for i in range(len(x)):
            if x[i][0] != x[i + 1][0]:
                target = x[i + 1]
                break
    except: pass

    for i in range(len(x)):
       if target[0] == x[i][0]:
           slg.append(x[i])

    return slg

n = int(input())

students = create_students_list(n)
slg = create_lowest_grade_list(students)

for i in range(len(slg)):
    print(slg[i][1])
