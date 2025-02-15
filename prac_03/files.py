name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name_from_file = file.read().strip()

print(f"Hi {name_from_file}!")

with open("numbers.txt", "w") as file:
    file.write("17\n42\n400")

with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())

result = num1 + num2
print(f"The sum of the first two numbers is: {result}")

with open("numbers.txt", "r") as file:
    total_sum = 0
    for line in file:
        total_sum += int(line.strip())

print(f"The total sum of all numbers is: {total_sum}")
