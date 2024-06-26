# Write your solution here
import datetime
def is_it_valid(pic: str):
    control = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    try:
        if pic[6] == '+':
            birthyear = '18'
        elif pic[6] == '-':
            birthyear = '19'
        elif pic[6] == 'A':
            birthyear = '20'
        else:
            return False
        check_birth = datetime.datetime(int(birthyear + pic[4:6]), int(pic[2:4]), int(pic[0:2]))
        index = int(pic[0:6] + pic[7:10]) % 31

    except:
        return False
    if 31 < int(pic[0:2]) or 1 > int(pic[0:2]) or 12 < int(pic[2:4]) or 1 > int(pic[2:4]) or pic[-1] != control[index] or len(pic) != 11:
        return False
    return True


#is_it_valid('080842-720N')
    