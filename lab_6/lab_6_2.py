class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    def get_info(self):
        print(f"Это транспортное средство марки {self.mark}, модели {self.model}")

bike = Vehicle("KSBOOR", "OL342")
bike.get_info()

class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__( mark, model)
        self.fuel_type = fuel_type
    def get_info(self):
        print(f"Это машина марки {self.mark}, модели {self.model}. Тип топлива - {self.fuel_type}")

carrr = Car("KSBOOR", "OL342", "27A")
carrr.get_info()

