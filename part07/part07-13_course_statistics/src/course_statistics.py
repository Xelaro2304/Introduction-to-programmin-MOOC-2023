# Write your solution here
import urllib.request, json

def retrieve_all():
    active_courses = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    for info in courses:
        if info['enabled'] == True:
            full_name = info['fullName']
            course = info['name']
            year = info['year']
            exercises = sum(info['exercises'])
            course_data = full_name, course, year, exercises
            active_courses.append(course_data)
    return active_courses



def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)

    weeks = len(course)
    students = []
    hours = 0
    exercises = 0
    for key, i in course.items():
        students.append(i['students'])
        hours += i['hour_total']
        exercises += i ['exercise_total']
    course_stats = {}
    course_stats['weeks'] = weeks
    course_stats['students'] = max(students)
    course_stats['hours'] = hours
    course_stats['hours_average'] = hours // max(students)
    course_stats['exercises'] = exercises
    course_stats['exercises_average'] = exercises // max(students)
    return course_stats
    




#retrieve_all()
#print(retrieve_course('docker2019'))