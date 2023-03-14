message = "Welcome to The Tip Calculator"
print(message)
bill = float(input("Enter The Amount of Bill \n $"))
tipPercent = float(input("How much percent do want to give tip 10%, 15% Or 20%"))
numOfPeople = float(input("How many people will split the bill"))
def getTip(bill, tip, split):
    tipInPrice = float((tip*bill)/100)
    totalPice = tipInPrice + bill
    return totalPice/split
print(f"each Person hast to pay ${getTip(bill, tipPercent, numOfPeople)}")