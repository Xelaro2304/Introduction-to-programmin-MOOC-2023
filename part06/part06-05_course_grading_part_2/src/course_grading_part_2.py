# write your solution here
def students(students_data):
    students_names=[]
    with open(students_data) as student_file:
        for line in student_file:
            line = line.replace("\n", "")
            student_list = line.split(';')
            if student_list[0] == "id":
                continue
            students_names.append(student_list)
        return students_names
    





def exercise(exercise_info):
    exercise_number=[]
    with open(exercise_info) as exercise_file:
        for line in exercise_file:
            line = line.replace("\n", "")
            exercise_list = line.split(';')
            if exercise_list[0] == "id":
                continue
            exercise_number.append(exercise_list)
        return exercise_number
    




def exam(exam_info):
    exam_number=[]
    with open(exam_info) as exam_file:
        for line in exam_file:
            line = line.replace("\n", "")
            exam_list = line.split(';')
            if exam_list[0] == "id":
                continue
            exam_number.append(exam_list)
        return exam_number
    



student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exercises completed: ")


student_information = students(student_info)
exercise_information = exercise(exercise_data)
exam_information = exam(exam_data)





for i in student_information:
    exercise_grade = 0
    exam_grade = 0
    points = 0
    for j in exercise_information:
        if i[0] in j:
            for k in range (1, len(j)):
                exercise_grade += int(j[k])
                exercise_points = str((exercise_grade*100)/40)
                exercise_points = int(exercise_points[0])
    for l in exam_information:
        if i[0] in l:
            for m in range (1, len(l)):
                exam_grade += int(l[m])
    points = exercise_points + exam_grade

    if points < 15:
        grade = 0
    elif 14 < points < 18:
        grade = 1
    elif 17 < points < 21:
        grade = 2
    elif 20 < points < 24:
        grade = 3
    elif 23 < points < 28:
        grade = 4
    elif 27 < points:
        grade = 5
    print(f'{i[1]} {i[2]} {grade}')