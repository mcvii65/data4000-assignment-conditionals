credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: ").replace(",", ""))

# Check for Low Risk first, then Medium Risk; all remaining cases are High Risk.
if credit_score >= 720 and annual_income >= 60000:
    risk_category = "Low Risk"
elif credit_score >= 650 and annual_income >= 40000:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

print(f"Loan Risk Category: {risk_category}")