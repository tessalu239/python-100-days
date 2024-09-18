print("Welcome to the tip calculator!")
bill=input("What was the total bill? $")
tip_percentage=int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people=int(input("How many people to split the bill? "))
tip=float(bill)*(tip_percentage/100)/num_people
bill_each=float(bill)/num_people
print(f"Each person should pay: ${round(bill_each+tip,2)}")