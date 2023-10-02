class Car:

  def __init__(self):
    self.accessories = []

  def add_accessory(self, accessory):
    self.accessories.append(accessory)

class CarBuilder:
  
  def __init__(self):
    self.car = Car()

  def add_standard_accessories(self):
    self.car.add_accessory("ABS")
    self.car.add_accessory("8 Airbags")
    self.car.add_accessory("Manual Air Conditioning")
    self.car.add_accessory("Electric Windows")
    self.car.add_accessory("Traction Control")
    self.car.add_accessory("Automatic Headlights")

  def add_metallic_paint(self):
    self.car.add_accessory("Metallic Paint")
  
  def add_alloy_wheels(self):
    self.car.add_accessory("Alloy Wheels")

  def add_auto_climate_control(self):
    self.car.add_accessory("Auto Climate Control")
    
  def add_multimedia_system(self):
    self.car.add_accessory("Multimedia System")

  def add_satellite_nav(self):
    self.car.add_accessory("Satellite Navigation")

  def get_car(self):
    return self.car

# Build a car
builder = CarBuilder()
builder.add_standard_accessories() 
builder.add_metallic_paint()
builder.add_alloy_wheels()

car = builder.get_car()
print(car.accessories)