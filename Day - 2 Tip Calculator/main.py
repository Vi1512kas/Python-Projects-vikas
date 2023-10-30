# TIP CALCULATOR
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
individual_bill = total_bill + (tip*total_bill)/100
individual_bill /= people
print(f"Each person should pay: ${individual_bill}")
