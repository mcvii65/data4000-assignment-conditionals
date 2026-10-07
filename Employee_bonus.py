salary_input = input("Enter annual salary (commas allowed): $")
annual_salary = float(salary_input.replace(",", ""))
performance_score = int(input("Enter performance score (0-100): "))

if not 0 <= performance_score <= 100:
    print("Performance score must be between 0 and 100.")
else:
    # Check the highest score ranges first to select the correct bonus rate.
    if performance_score >= 90:
        bonus_percent = 20
    elif performance_score >= 80:
        bonus_percent = 10
    elif performance_score >= 70:
        bonus_percent = 5
    else:
        bonus_percent = 0

    # Calculate the bonus as the selected percentage of annual salary.
    bonus_amount = annual_salary * bonus_percent / 100

    print(f"Performance Bonus: {bonus_percent}%")
    print(f"Bonus Amount: ${bonus_amount:.2f}")