# 1000, 500, 200, 100, 50, 20, 10, 5, 1

money = eval(input("Enter Money to Deposit ---> ")) # int(), eval(), type()
print(type(money))

print("\n ======================== PH BANK DENOMINATION ======================== ")
print(" Money to Deposit ------->   ", money, "php")

thousand = money // 1000
thousand_change = money % 1000

fiveh = thousand_change // 500
fiveh_change = thousand_change % 500

twoh = fiveh_change // 200
twoh_change = fiveh_change % 200

oneh = twoh_change // 100
oneh_change = twoh_change % 100

fifty = oneh_change // 50
fifty_change = oneh_change % 50

twenty = fifty_change // 20
twenty_change = fifty_change % 20

ten = twenty_change // 10
ten_change = twenty_change % 10

five = ten_change // 5
five_change = ten_change % 5

one = five_change // 1
one_change = five_change % 1

print("\n\t1000 -", thousand)
print("\t500 -", fiveh)
print("\t200 -", twoh)
print("\t100 -", oneh)
print("\t50 -", fifty)
print("\t20 -", twenty)
print("\t10 -", ten)
print("\t5 -", five)
print("\t1 -", one)

print("\n ======================== PH BANK END OF LINE ======================== ")