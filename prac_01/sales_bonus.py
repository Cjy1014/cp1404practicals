"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,ooo, the user gets a 10% bonus.
If sale are $1,000 or over, the bonus 15%.
"""

sales = float(input("Enter the sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15

    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter the sales: $"))

print("Thank you")