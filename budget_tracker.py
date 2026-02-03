print("Welcome to your budget tracker!")

start_balance = float(input("Enter your starting balance: £"))
print(f"Starting Balance: £{start_balance:.2f}")

while True:
   expense_income = input("Is this your expense or income (q to quit): ")
   if expense_income.lower() == "q":
       print("Goodbye!")
       break
   money = float(input("Enter an amount: £"))

   if expense_income.lower()== "expense":
       start_balance -= money
   elif expense_income.lower() == "income":
       start_balance += money
   else:
       print("Invalid entry. Please type 'expense' or 'income'. ")

print(f"Updated Balance: £{start_balance:.2f}")
