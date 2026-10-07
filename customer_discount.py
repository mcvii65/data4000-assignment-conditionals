purchase_amount = float(input("Enter purchase amount: $"))
membership_status = input("Are you a member? (yes or no): ").strip().lower()

# Members receive a discount based on the $100 purchase threshold.
if membership_status == "yes":
    if purchase_amount >= 100:
        discount_percent = 15
    else:
        discount_percent = 5
# Nonmembers receive 10% off at $150 or more, and no discount otherwise.
elif purchase_amount >= 150:
    discount_percent = 10
else:
    discount_percent = 0

# Subtract the discount from the original purchase amount.
final_price = purchase_amount * (1 - discount_percent / 100)

print(f"Discount applied: {discount_percent}%")
print(f"Final price: ${final_price:.2f}")