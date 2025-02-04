number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid input of items！")
    number_of_items = int(input("Enter the number of items: "))

total_price = 0

for i in range(number_of_items):
    price = float(input(f"Price of item {i + 1}: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"The total price for {number_of_items} items is ${total_price:.2f}")