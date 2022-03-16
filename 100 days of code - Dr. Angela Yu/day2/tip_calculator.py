print("Welcome to the tip calculator!")

totalBill = float(input("What was the total bill? $"))

tipPercent = float(input("What percentage tipo would you like to give? "))/100

billPercent = totalBill * tipPercent

finalBill = totalBill * tipPercent

people = int(input("How many people to split the bill? "))

valueEachPerson = round(finalBill/people,2)

print(f"Each person should pay: $ {valueEachPerson}")
