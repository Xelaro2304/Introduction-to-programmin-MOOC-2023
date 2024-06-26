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


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

student_information = students(student_info)
exercise_information = exercise(exercise_data)



for i in student_information:
    number = 0
    for j in exercise_information:
        if i[0] in j:
            for k in range (1, len(j)):
                number += int(j[k])
            print(f'{i[1]} {i[2]} {number}')
