print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# calculates bill with tip
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
# rounds off bill per person to 2 decimal points
final_bill = round(bill_per_person, 2)
print(f"Each person will pay ${final_bill}")