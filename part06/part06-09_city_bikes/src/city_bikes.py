# tee ratkaisu tänne
# Write your solution here
import math


def get_station_data(filename: str):
    map_dictionary = {}
    with open(filename) as file:
        for line in file:
            if "FID" in line:
                continue
            line = line.split(';')
            longitude = line[0]
            latitude = line [1]
            map_dictionary[line[3]] = (float(longitude), float(latitude))
        return map_dictionary

def distance(stations: dict, station1: str, station2: str):

    coordinates1 = stations[station1]
    coordinates2 = stations[station2]
    x = (coordinates1[0]-coordinates2[0]) * 55.26
    y = (coordinates1[1]-coordinates2[1]) * 111.2
    lineal_distance = math.sqrt(x**2 + y**2)
    return lineal_distance



def greatest_distance(stations: dict):
    longest="","",0
    previous=[]
    for key, value in stations.items():
        for next_key, next_value in stations.items():
            if next_value == value:
                continue
            if next_key in previous:
                continue
            x = (value[0]-next_value[0]) * 55.26
            y = (value[1]-next_value[1]) * 111.2
            lineal_distance = math.sqrt(x**2 + y**2)
            if lineal_distance > longest[2]:
                longest = (key, next_key, lineal_distance)
        previous.append(key)
    return longest
