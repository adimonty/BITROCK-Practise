from abc import ABC, abstractmethod

# Abstract delivery strategy
class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, goods, addresses):
        pass

# Concrete delivery strategies
class PlaneDelivery(DeliveryStrategy):
    def deliver(self, goods, addresses):
        print(f"Using a plane to deliver {goods} to {addresses}")

class TruckDelivery(DeliveryStrategy):
    def deliver(self, goods, addresses):
        print(f"Using a truck to deliver {goods} to {addresses}")

class ShipDelivery(DeliveryStrategy):
    def deliver(self, goods, addresses):
        print(f"Using a ship to deliver {goods} to {addresses}")

class VanDelivery(DeliveryStrategy):
    def deliver(self, goods, addresses):
        print(f"Using a van to deliver {goods} to {addresses}")

class DroneDelivery(DeliveryStrategy):
    def deliver(self, goods, addresses):
        print(f"Using a drone to deliver {goods} to {addresses}")

# Context class (Amazon's shipping system)
class AmazonShipping:
    def __init__(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy

    def set_delivery_strategy(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy

    def deliver_goods(self, goods, addresses):
        self.delivery_strategy.deliver(goods, addresses)

# Usage
if __name__ == "__main__":
    # Create different delivery strategies
    plane_delivery = PlaneDelivery()
    truck_delivery = TruckDelivery()
    ship_delivery = ShipDelivery()
    van_delivery = VanDelivery()
    drone_delivery = DroneDelivery()

    # Initialize Amazon's shipping system with a delivery strategy
    amazon_shipping = AmazonShipping(plane_delivery)

    # Deliver goods to addresses using the current strategy
    amazon_shipping.deliver_goods("electronics", ["Address1", "Address2"])

    # Change the delivery strategy
    amazon_shipping.set_delivery_strategy(truck_delivery)

    # Deliver goods to addresses using the new strategy
    amazon_shipping.deliver_goods("books", ["Address3", "Address4"])
