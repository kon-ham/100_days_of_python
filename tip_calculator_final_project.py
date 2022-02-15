total_bill = input("Ayyy, Tip Calculator speaking.\nFirst off, what is the total bill?\n")

number_of_people_splitting_bill = input("$%s. Got it. How many people are splitting the bill?\n" % (total_bill))

tip_percentage = input("%s people splitting a $%s receipt. Got it. What is your desired tip percentage?\n" % (number_of_people_splitting_bill, total_bill))

cost_per_person_including_tip = float(total_bill) / float(number_of_people_splitting_bill) * (1.0 + float(tip_percentage) / 100)

result = round(cost_per_person_including_tip, 2)

print("Calculating...\nLooks like each person should pay $%s" % result)