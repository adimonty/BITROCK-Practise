from abc import ABC, abstractmethod

# Abstract Ship class
class Ship(ABC):
    def __init__(self, name):
        self.name = name
        self.number_of_crew = 0
        self.number_of_passengers = 0
        self.max_speed = 0

    @abstractmethod
    def set_number_of_crew(self, crew):
        pass

    @abstractmethod
    def set_number_of_passengers(self, passengers):
        pass

    @abstractmethod
    def set_max_speed(self, max_speed):
        pass

# Concrete sailing ship class
class SailingShip(Ship):
    def set_number_of_crew(self, crew):
        self.number_of_crew = crew

    def set_number_of_passengers(self, passengers):
        self.number_of_passengers = passengers

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

# Concrete motor ship class
class MotorShip(Ship):
    def set_number_of_crew(self, crew):
        self.number_of_crew = crew

    def set_number_of_passengers(self, passengers):
        self.number_of_passengers = passengers

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

# Concrete outboard ship class
class OutboardShip(Ship):
    def set_number_of_crew(self, crew):
        self.number_of_crew = crew

    def set_number_of_passengers(self, passengers):
        self.number_of_passengers = passengers

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

# Factory Method to create ships
class ShipFactory:
    @staticmethod
    def create_ship(ship_type, name):
        if ship_type == "sailing":
            return SailingShip(name)
        elif ship_type == "motor":
            return MotorShip(name)
        elif ship_type == "outboard":
            return OutboardShip(name)
        else:
            raise ValueError("Invalid ship type")

# Usage
if __name__ == "__main__":
    factory = ShipFactory()

    sailing_ship = factory.create_ship("sailing", "Sailboat")
    sailing_ship.set_number_of_crew(10)
    sailing_ship.set_number_of_passengers(20)
    sailing_ship.set_max_speed(15)

    motor_ship = factory.create_ship("motor", "Motor Yacht")
    motor_ship.set_number_of_crew(5)
    motor_ship.set_number_of_passengers(10)
    motor_ship.set_max_speed(30)

    outboard_ship = factory.create_ship("outboard", "Outboard Boat")
    outboard_ship.set_number_of_crew(2)
    outboard_ship.set_number_of_passengers(4)
    outboard_ship.set_max_speed(25)

    # Print ship details
    print(f"{sailing_ship.name}: Crew={sailing_ship.number_of_crew}, Passengers={sailing_ship.number_of_passengers}, Max Speed={sailing_ship.max_speed}")
    print(f"{motor_ship.name}: Crew={motor_ship.number_of_crew}, Passengers={motor_ship.number_of_passengers}, Max Speed={motor_ship.max_speed}")
    print(f"{outboard_ship.name}: Crew={outboard_ship.number_of_crew}, Passengers={outboard_ship.number_of_passengers}, Max Speed={outboard_ship.max_speed}")
