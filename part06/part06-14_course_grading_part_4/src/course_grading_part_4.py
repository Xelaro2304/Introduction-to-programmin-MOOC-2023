# tee ratkaisu tänne
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
    



def course(course_info):
    course_name_grade = []
    with open(course_info) as course_file:
        for line in course_file:
            line = line.replace("\n", "")
            course_list = line.split(':')
            course_name_grade.append(course_list[1].strip())
    return course_name_grade

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exercises completed: ")
course_data = input("Course information: ")
#student_info = "students1.csv"
#exercise_data = "exercises1.csv"
#exam_data = "exam_points1.csv"
#course_data = "course1.txt"



student_information = students(student_info)
exercise_information = exercise(exercise_data)
exam_information = exam(exam_data)
course_information = course(course_data)



stats = {}
for i in student_information:
    exercise_grade = 0
    exam_grade = 0
    points = 0
    for j in exercise_information:
        if i[0] in j:
            for k in range (1, len(j)):
                exercise_grade += int(j[k])
            if exercise_grade == 40:
                exercise_points = 10
            else:
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
    stats[f'{i[1]} {i[2]}'] = (exercise_grade, exercise_points, exam_grade, points, grade, i[0])



with open("results.txt", "w") as results, open("results.csv", "w") as results_excel:
        
    results.write(f'{course_information[0]}, {course_information[1]} credits\n')
    results.write('='*len(course_information[0]+course_information[1]+' , credits')+'\n')
    results.write('name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n')
    for key, value in stats.items():
        results.write(f'{key:30}{value[0]:<10}{value[1]:<10}{value[2]:<10}{value[3]:<10}{value[4]:<10}\n')
        results_excel.write(f'{value[5]};{key};{value[4]}\n')