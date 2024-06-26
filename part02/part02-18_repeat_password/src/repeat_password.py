# Write your solution here
password = input("Password:")
while True:
    rpassword = input("Repeat password:")
    if rpassword == password:
        print('User account created!')
        break
    else:
        print('They do not match!')