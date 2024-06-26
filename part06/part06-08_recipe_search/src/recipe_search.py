# Write your solution here
def read_file(file):
    with open(file) as cooking_book:
        matrix=[]
        recipe = []
        for line in cooking_book:
            line = line.lower()
            recipe.append(line.strip())
            if line == '\n':
                matrix.append(recipe)
                recipe = []
    matrix.append(recipe)
    return matrix



def search_by_name(file, name):
    matrix = read_file(file)
    found_recipes = []
    for i in matrix:
        if name in i[0]:
            found_recipes.append(i[0].capitalize())
    return found_recipes



def search_by_time(file: str, time: int):
    matrix = read_file(file)
    found_recipes = []
    for i in matrix:
        if time >= int(i[1]):
            found_recipes.append(f"{i[0].capitalize()}, preparation time {i[1]} min")
    return found_recipes




def search_by_ingredient(filename: str, ingredient: str):
    matrix = read_file(filename)
    found_recipes = []
    for i in matrix:
        if ingredient in i[2:]:
            found_recipes.append(f"{i[0].capitalize()}, preparation time {i[1]} min")
    return found_recipes

#print(search_by_name("recipes1.txt", "cake"))
#print(search_by_time("recipes1.txt", 20))
#print(search_by_ingredient("recipes1.txt", "eggs"))