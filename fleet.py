from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, daily_rate: float) -> None:
        self.vehicle_id = vehicle_id
        self.model = model
        self.set_daily_rate(daily_rate)

    def get_daily_rate(self) -> float:
        return self.__daily_rate

    def set_daily_rate(self, rate: float) -> None:
        if rate <= 0.0:
            raise ValueError("Daily rate must be greater than 0.0.")
        self.__daily_rate = float(rate)

    def __lt__(self, other: "Vehicle") -> bool:
        return self.get_daily_rate() < other.get_daily_rate()

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        pass


class PassengerCar(Vehicle):
    def __init__(
        self, vehicle_id: str, model: str, daily_rate: float, num_seats: int
    ) -> None:
        super().__init__(vehicle_id, model, daily_rate)
        self.num_seats = int(num_seats)

    def calculate_rental_cost(self, days: int) -> float:
        return (self.get_daily_rate() * days) + (15.0 * self.num_seats)

    def __str__(self) -> str:
        return (
            f"[PassengerCar] ID: {self.vehicle_id} | Model: {self.model} | "
            f"Seats: {self.num_seats} | Rate: ${self.get_daily_rate():.2f}/day"
        )


class CargoTruck(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        model: str,
        daily_rate: float,
        cargo_capacity_tons: float,
    ) -> None:
        super().__init__(vehicle_id, model, daily_rate)
        self.cargo_capacity_tons = float(cargo_capacity_tons)

    def calculate_rental_cost(self, days: int) -> float:
        return (self.get_daily_rate() * days) + (50.0 * self.cargo_capacity_tons)

    def __str__(self) -> str:
        return (
            f"[CargoTruck] ID: {self.vehicle_id} | Model: {self.model} | "
            f"Capacity: {self.cargo_capacity_tons:.1f}t | Rate: ${self.get_daily_rate():.2f}/day"
        )


def generate_fleet_manifest(fleet_list: list[Vehicle], days: int) -> str:
    lines = [f"=== LogiTrans Fleet Manifest ({days} Days) ==="]
    total_cost = 0.0
    for vehicle in sorted(fleet_list):
        cost = vehicle.calculate_rental_cost(days)
        total_cost += cost
        lines.append(f"{str(vehicle)} -> Rental Cost: ${cost:.2f}")
    lines.append(f"Total Fleet Revenue ({days} days): ${total_cost:.2f}")
    return "\n".join(lines)