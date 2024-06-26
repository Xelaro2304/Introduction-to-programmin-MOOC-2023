# Write your solution here
def filter_incorrect():
    lottery_line = {}
    numbers = '1234567890'
    with open('lottery_numbers.csv') as new_file:
        for line in new_file:
            line = line.split(';')
            line[1] = line[1].strip()
            list_of_numbers = line [1].split(',')
            lottery_line[line[0]] = list_of_numbers
    #lottery_line['week 52'] = [['29'],['26'],['11'],['21'],['20'],['29'],['5'],]
    with open('correct_numbers.csv', 'a') as correct_file, open('correct_numbers.csv', 'w') as create_correct_file:
        for key, value in lottery_line.items():
            check = False
            check_key_num = 4-len(key)
            for i in range (-1,check_key_num,-1):
                if key[i] not in numbers:
                    check = True
            if check:
                continue
            for number in value:
                for integer in range (len(number)):
                    try:
                        if number[integer] not in numbers or int(number) > 39 or int(number) < 1 or len(value) != 7 or value.count(number) > 1:
                            check = True
                    except:
                        check = True
                        break
                    if check:
                        break
            if check:
                continue
            rejoin_number = ','.join(value)
            try:
                correct_file.append(f'{key};{rejoin_number}\n')
            except:
                create_correct_file.write(f'{key};{rejoin_number}\n')

#filter_incorrect()