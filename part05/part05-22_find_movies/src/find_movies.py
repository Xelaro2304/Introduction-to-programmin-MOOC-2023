# Write your solution here
def find_movies(database: list, search_term: str):
    found = []
    for i in database:
        key = str(i["name"])
        if search_term in key.lower():
            found.append(i)
    return found
