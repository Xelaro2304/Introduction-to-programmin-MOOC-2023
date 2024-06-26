# Write your solution here
def add_student(student_db, student):
    if student not in student_db:
        student_db[student] = "no completed courses"

 

def print_student(student_db, student):
    if student in student_db:
        if student_db[student] != "no completed courses" and student_db[student] != []:
            average_grade=0
            courses = student_db[student]
            print(f'{student}:')
            print(f" {len(courses)} completed courses:")
            for i in range (0, len(courses)):
                print (f'  {courses[i][0]} {courses[i][1]}')
                average_grade+=courses[i][1]
            print(f" average grade {average_grade/len(courses)}")
        else:
            print(f'{student}:')
            print(' no completed courses')
    else:
        print(f"{student}: no such person in the database")

 

 


def add_course(student_db: dict, student: str, courses: tuple):
    new_course = True
    if student_db[student] != "no completed courses":
        saved_courses = student_db[student]
        for i in range (0, len(saved_courses)):
            if saved_courses[i][0] == courses[0]:
                grade = saved_courses[i][1]
                new_course = False
                if grade<courses[1]:
                    student_db[student][i] = courses
            if new_course == True and courses[1] != 0 and i == (len(saved_courses)-1):
                (student_db[student]).append(courses)    
    if student_db[student] == "no completed courses":
        student_db[student] = []
        if courses[1] != 0:
            (student_db[student]).append(courses)




def summary(student_db):
    number_students = len(student_db)
    highest=0
    most_completed= 0
    grade=0
    for key, value in student_db.items():
        for i in value:
            grade+=i[1]
            if i == (value[-1]):
                avrg_grade = grade/len(value)
                if avrg_grade > highest:
                    highest = avrg_grade
                    highest_student = key
        if len(value) > most_completed:
            most_completed = len(value)
            most_completed_student=key
    print(f'students {number_students}')
    print(f'most courses completed {most_completed} {most_completed_student}')
    print(f'best average grade {highest} {highest_student}')

