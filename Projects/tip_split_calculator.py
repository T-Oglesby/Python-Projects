print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 15, 18, or 20? "))
split = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

per_person = bill_with_tip / split
final_amount = "{:.2f}".format(per_person)

print(f"Each person should pay: ${final_amount}")