# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    total = 0
    for i in my_matrix:
        total += i.count(element)
    return total