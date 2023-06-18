class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"Car(brand='{self.brand}', model='{self.model}')"

my_car = Car("Toyota", "Corolla")
print("Car Brand: ",my_car.brand)
print("Car Model: ",my_car.model)
print("Car Object: ",my_car)
