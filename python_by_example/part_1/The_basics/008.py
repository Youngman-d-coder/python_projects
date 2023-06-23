total_bill = int(input("Enter the total bill:  "))
diners = int(input("How many people are splitting the bill:  "))
new_bill = total_bill / diners

print(f"Each person must pay {new_bill}")
