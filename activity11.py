import getpass

username = "Kanin"
password = "buseng"

u = input("Enter your username --->")
p = getpass.getpass("Enter your password --->")

if u == username and p == password :
    print("Access granted")

else :
    print("username or password is incorrect. Access denied")

    

username = "Maling"
password = "cornbeef"

u = getpass.getpass("Enter your username --->")
p = input("Enter your password --->")

if u == username and p == password :
    print("Access granted")

else :
    print("username or password is incorrect. Access denied")



username = "Adobo"
password = "Sinigang"

u = getpass.getpass("Enter your username --->")
p = getpass.getpass("Enter your password --->")

if u == username and p == password :
    print("Access granted")

else :
    print("username or password is incorrect. Access denied")
