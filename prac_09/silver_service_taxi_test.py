from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)

fancy_taxi.drive(18)

fare = fancy_taxi.get_fare()

print(fancy_taxi)
print(f"Fare: ${fare:.2f}")
