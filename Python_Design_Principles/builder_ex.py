class Car:
    def __init__(self):
        self.accessories = []

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def __str__(self):
        return f"Car with Accessories: {', '.join(self.accessories)}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_metallic_paint(self):
        self.car.add_accessory("Metallic Paint")
        return self

    def add_alloy_wheels(self):
        self.car.add_accessory("Alloy Wheels")
        return self

    def add_auto_climate_control(self):
        self.car.add_accessory("Auto Climate Control")
        return self

    def add_multimedia_system(self):
        self.car.add_accessory("Multimedia System")
        return self

    def add_satellite_nav(self):
        self.car.add_accessory("Satellite Navigation")
        return self

    def get_car(self):
        return self.car


# Build a car with different optional configurations
builder = CarBuilder()
full_featured_car = (
    builder
    .add_metallic_paint()
    .add_alloy_wheels()
    .add_auto_climate_control()
    .add_multimedia_system()
    .add_satellite_nav()
    .get_car()
)

# Add standard accessories
full_featured_car.add_accessory("ABS")
full_featured_car.add_accessory("8 Airbags")
full_featured_car.add_accessory("Manual Air Conditioning")
full_featured_car.add_accessory("Electric Windows")
full_featured_car.add_accessory("Traction Control")
full_featured_car.add_accessory("Automatic Headlights")

print(full_featured_car)
