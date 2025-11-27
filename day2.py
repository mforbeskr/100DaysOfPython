height = 1.65 
weight = 84


# Write your code here.
# Calculate the bmi using weight and height.
bmi = 84/1.65**2

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 4))

print("=== Welcome to your tip calculator ===")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15"))
people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
total_per_person = bill_with_tip / people

final_amount = round(total_per_person, 2)

print(f"Each person should pay: ${final_amount}")
