# Write your solution here
def results ():
    exam=[]
    exercises=[]
    while True:
        grades = input("Exam points and exercises completed: ")
        if grades == '':
            return exam, exercises
        grades = grades.split()
        exam.append(grades[0])
        exercises.append(grades[1])


def final_points(points_exam, points_exercises):
    total_points = []
    for i in range (0, len(points_exam)):
        total_points.append(int(points_exam[i]) + (int(points_exercises[i])//10))
    return total_points

def grade_distribution(final_points, exam_points):
    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    passing = 0
    for i in range (0, len(final_points)):
        if final_points[i] <= 14 or int(exam_points[i]) < 10:
            zero += '*'
        elif 15 <= final_points[i] <= 17:
            one += '*'
            passing += 1
        elif 18 <= final_points[i] <= 20:
            two += '*'
            passing += 1
        elif 21 <= final_points[i] <= 23:
            three += '*'
            passing += 1
        elif 24 <= final_points[i] <= 27:
            four += '*'
            passing += 1
        elif 28 <= final_points[i] <= 30:
            five += '*'
            passing += 1
    
    passing = (passing/(len(final_points)))*100
    return zero, one, two, three, four, five, passing



def statistics(grade_points):
    sum = 0
    for i in (grade_points):
        sum += i
    average = sum/(len(grade_points))
    return average
    


def screen(mean, passed, distribution):
    print("Statistics:")
    print(f'Points average: {mean:.1f}')
    print(f'Pass percentage: {passed:.1f}')
    print("Grade distribution:")
    print(f"  5: {distribution[5]}")
    print(f"  4: {distribution[4]}")
    print(f"  3: {distribution[3]}")
    print(f"  2: {distribution[2]}")
    print(f"  1: {distribution[1]}")
    print(f"  0: {distribution[0]}")




def main():
    exam_exercise_points = results()
    grade = final_points(exam_exercise_points[0], exam_exercise_points[1])
    distribution = grade_distribution(grade, exam_exercise_points[0])
    stat = statistics(grade)
    result = screen(stat, distribution [-1], distribution)

main ()