# Write your solution here
def oldest_person(people: list):
    oldest_age = 10000
    oldest= ""
    for i in people:
        if i[-1] < oldest_age:
            oldest_age = i[-1]
            oldest = i[0]
    return oldest