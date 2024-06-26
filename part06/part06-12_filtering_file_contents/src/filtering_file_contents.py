# Write your solution here
def filter_solutions():
    solutions = []
    correct_exercises = []
    incorrect_exercises = []
    checked_exercises= {"correct": '', "incorrect": ''}
    with open("solutions.csv") as file:
        for line in file:
            line = line.strip()
            line = line.split(';')
            solutions.append(line)
    for i in solutions:
        if "+" in i[1]:
            operator = i[1].index('+')
            one = int(i[1][:operator])
            two = int(i[1][operator + 1:])
            correct_result = one+two
        else:
            operator = i[1].index('-')
            one = int(i[1][:operator])
            two = int(i[1][operator + 1:])
            correct_result = one-two
        if correct_result == int(i[2]):
            exercise = ""
            for j in i:
                if j == i[-1]:
                    exercise += j
                else:
                    exercise += f"{j};"
            correct_exercises.append(exercise)
            checked_exercises["correct"] = correct_exercises
        else:
            exercise = ""
            for j in i:
                if j == i[-1]:
                    exercise += j
                else:
                    exercise += f"{j};"
            incorrect_exercises.append(exercise)
            checked_exercises["incorrect"] = incorrect_exercises

    with open("correct.csv", "w") as correct:
        for key, value in checked_exercises.items():
            if key == "correct":
                for k in value:
                    correct.write(f'{k}\n')
            else: 
                continue
    with open("incorrect.csv", "w") as incorrect:
        for key, value in checked_exercises.items():
            if key == "incorrect":
                for l in value:
                    incorrect.write(f'{l}\n')
            else: 
                continue

