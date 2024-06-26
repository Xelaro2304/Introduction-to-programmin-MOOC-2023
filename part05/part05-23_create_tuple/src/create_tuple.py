# Write your solution here
def create_tuple(x: int, y: int, z: int):
    reference = [x,y,z]
    sorted_list = sorted(reference)
    addition = 0
    for i in reference:
        addition += i
    instruction = (sorted_list[0], sorted_list[-1], addition)
    return instruction