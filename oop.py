class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")




phone = Smartphone("Samsung", "S24Ultra", 256)

phone.info()


phone.call("07040218796")



class Gamingphone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)
        self.__gpu_power = gpu_power

    def play_game(self, game):
        print(f"Playing {game} with GPU power {self.__gpu_power}..")


gaming = Gamingphone("Asus", "ROG 6", 512, "High-End GPU")

gaming.info()
gaming.play_game("Call Of Duty")




# The Polymorphism
class Vehicle:
    def move(self):
        print("The Vehicle is Moving")


class Car(Vehicle):
    def move(self):
        print("Driving.......")



class Plane(Vehicle):
    def move(self):
        print("Flying.......")
        

class Boat(Vehicle):
    def move(self):
        print("Flying.......")


Vehicle = [Car(),Plane(),Boat()]

for v in Vehicle:
    v.move()