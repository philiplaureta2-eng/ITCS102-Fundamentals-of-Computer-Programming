


age = int(input("Enter your age "))
is_employed = bool(input("Are you employed? (Yes/No) "))
credit_score = eval(input("What is your credit score? "))
annual_income = eval(input("What is your annual income? "))
has_collateral = bool(input("Do you have any collateral? (Yes/No) "))

base_rate = 0.00

if age <= 21 and not is_employed == False :
    print("Rejected: Fails baseline criteria")

if age >= 21 and is_employed == True :
    if credit_score >= 750 : 
        print("Your credit score is excellent")
        base_rate = 5.0
        if annual_income >= 100000 :
            base_rate = 4.5
        else :
            base_rate = 5.0
            print("Your base rate is ", base_rate)
    elif credit_score <= 600 and credit_score <= 750 :
        print("Your credit score is fair")
        if has_collateral == True :
            base_rate = 7.0 
        elif annual_income <= 40000 :
            base_rate = 9.5
        elif annual_income <= 40000 and has_collateral == True :
            base_rate = 8.0
        else : 
            base_rate = 5.0
    elif credit_score <= 600 : 
        print("Rejected: Credit score too Low.")
    else :
        print("Rejected: Fails baseline criteria")


print("===============================================")
print("Age                  : ", age)
print("Employed?            : ", is_employed)
print("Credit Score         : ", credit_score)
print("Annual Income        : ", annual_income)
print("Has Collateral?      : ", has_collateral)
print("Your base rate is ", base_rate)
print("===============================================")






