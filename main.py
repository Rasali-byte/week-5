from fleet import CargoTruck, PassengerCar, Vehicle, generate_fleet_manifest


def run_validation_checks() -> None:
    print("--- 1. Abstract Class Check ---")
    try:
        invalid_vehicle = Vehicle("V-000", "Generic Base", 50.0)  # type: ignore[abstract]
        print(invalid_vehicle)
    except TypeError as exc:
        print(f"Expected TypeError caught: {exc}")

    print("\n--- 2. Daily Rate Validation Check ---")
    for bad_rate in (0.0, -25.0):
        try:
            PassengerCar("PC-999", "Test Sedan", bad_rate, 5)
        except ValueError as exc:
            print(f"Rate {bad_rate} rejected with ValueError: {exc}")

    sample_car = PassengerCar("PC-101", "Toyota Corolla", 45.0, 5)
    try:
        sample_car.set_daily_rate(0.0)
    except ValueError as exc:
        print(f"Setter rejected 0.0 with ValueError: {exc}")

    sample_car.set_daily_rate(52.0)
    print(f"Updated rate via setter: ${sample_car.get_daily_rate():.2f}/day")


def main() -> None:
    run_validation_checks()

    fleet = [
        CargoTruck("CT-201", "Volvo FH16", 140.0, 18.5),
        PassengerCar("PC-102", "Honda Civic", 42.0, 5),
        CargoTruck("CT-202", "Freightliner Cascadia", 115.0, 12.0),
        PassengerCar("PC-103", "Ford Transit Passenger", 68.0, 12),
    ]

    print("\n--- 3. Polymorphic Fleet Manifest ---")
    rental_days = 4
    manifest = generate_fleet_manifest(fleet, rental_days)
    print(manifest)


if __name__ == "__main__":
    main()