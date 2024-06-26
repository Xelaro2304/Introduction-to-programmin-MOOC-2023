# Write your solution here
temperature = int(input('Please type in a temperature'))
celsius = (temperature - 32) * 5/9
print(f'{temperature} degrees Fahrenheit equals {celsius} degrees Celsius')
if celsius < 0:
    print("Brr! It's cold in here!")
