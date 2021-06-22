"""
Tip Calculator
--------------
Calculates tip amount for a bill. Allows for splitting the bill.

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""


# Unnecessary title
print("Tip Calculator\n")

# Gather input
bill_total = float(input("Bill total: "))
num_shares = float(input("How many shares? (default = 1): ") or "1")
tip_percent = float(input("What percentage to tip? (default = 15%): ") or "15")

# Perform calculations
bill_share = bill_total / num_shares
tip_amount = bill_share * (tip_percent / 100)
total_share = bill_share + tip_amount

# Display information
print(f"\nThe grand total is {(total_share * num_shares):.2f}")
print(f"Each share is ${bill_share + tip_amount:.2f} (${bill_share:.2f} + ${tip_amount:.2f} tip).")
