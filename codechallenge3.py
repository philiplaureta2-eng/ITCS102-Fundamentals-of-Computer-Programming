
Name = str(input("Enter the sender name ---> "))
Item = str(input("Enter the type of item ---> "))
isFragile = bool(input("Is the item Fragile? (Yes/No) ---> "))
Weight = float(input("Enter the weight of an item (kg) ---> "))
Distance = float(input("Enter the distance of an item (km) ---> "))
isExpress = bool(input("Is the item express? (Yes/No) ---> "))
isInternational = bool(input("Is the item international? (Yes/No) ---> "))


base_cost = (Weight * 2.50) + (Distance * 0.15)

if Weight <= 2.0 and Distance <= 100.0 and isExpress and isInternational:
    Total = 0.00

elif isInternational and isExpress:
    Total = (base_cost * 1.40) + 50

elif isExpress or (isInternational and Weight > 20.0) :
    Total = base_cost + 30

elif All :
    Total = base_cost

print(">>>>>>>>>>>>>>>> Shipping Information <<<<<<<<<<<<<<<<")
print()
print("Sender Name                : ", Name)
print("Type of Item               : ", Item)
print("Is the item Fragile?       : ", isFragile)
print("Weight of the item         : ", Weight, "kg")
print("Distance of the item       : ", Distance, "km")
print("Is the item Express?       : ", isExpress)
print("Is the item International? : ", isInternational)
print()
print("Total Shipping Cost        : $", Total)
print()
print(">>>>>>>>>>> Thank you for using our service! <<<<<<<<<<")