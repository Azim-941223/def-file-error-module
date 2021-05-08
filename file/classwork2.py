# 2
f = open ('user.txt', 'w')
login = input("Enter login: ")
password = input("Enter password: ")
f.write(f"{login}, {password}")
f.close
