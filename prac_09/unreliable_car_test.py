from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Old Bomb", 100, 30)

total_attempts = 10
for i in range(total_attempts):
    distance = unreliable_car.drive(10)
    print(f"Attempt {i+1}: Drove {distance} km, Fuel left: {unreliable_car.fuel}")