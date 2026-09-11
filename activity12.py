name = input("Enter your name --->")

age = int(input("Enter your age --->"))

if age >= 0 and age <= 5 :
    print("The age is considered as Infant")

elif age >= 5 and age <= 12 :
    print("The age is considered as Kid")

elif age >= 13 and age <= 15 :
    print("The age is considered as Pre-Teen")

elif age >= 16 and age <= 19 :
    print("The age is considered as Teenager")

elif age >= 20 and age <= 29 :
    print("The age is considered as Early Adulthood")

elif age >= 30 and age <= 58 :
    print("The age is considered as Adult")

elif age >= 59 and age <= 150 :
    print("The age is considered as Senior Citizen")

else :
    print("Age is Invalid")

    