import csv
import os

print("Expense Tracker")

filename = "expenses.csv"
choice = ""

while choice != "0":
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What did you buy? ").strip()

        try:
            amount = float(input("Amount in GBP: "))

            if description == "":
                print("Description cannot be empty.")

            elif amount <= 0:
                print("Amount must be greater than zero.")

            else:
                with open(filename, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([description, round(amount, 2)])

                print("Expense saved!")

        except ValueError:
            print("Enter a valid number, for example 12.50.")

    elif choice == "2":
        if os.path.exists(filename):
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(row[0], "-", "£" + row[1])

        else:
            print("No expenses saved yet.")

    elif choice == "3":
        total = 0

        if os.path.exists(filename):
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    total += float(row[1])

        print("Total expenses: £" + format(total, ".2f"))

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Invalid option.")
