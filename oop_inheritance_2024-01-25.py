# class Vehicle:
#     def __init__(self, brand, model, capacity,year):
#         self.brand = brand
#         self.model = model
#         self.capacity = capacity
#         self.year = year
#         self.speed = 0
#         self.engine = False
#     def calculate_charge(self):
#         self.fare = self.capacity * 100
#
#     def start(self):
#         '''vehincle consumption'''
#         if not self.engine:
#             print(f"{self.brand} {self.model} is working.")
#             self.engine = True
#         else:
#             print(f"{self.brand} {self.model}  is already working")
#
#     def stop(self):
#         """Stop the vehicle."""
#         if self.engine:
#             print(f"{self.brand} {self.model} is stopping.")
#             self.engine = False
#         else:
#             print(f"{self.brand} {self.model} is already stopped.")
#
#     def speedup(self, kmh):
#         """speedup' the vehicle."""
#         if self.engine:
#             self.speed += kmh
#         print(f'The current speed of the vehincle {self.speed}.')
#     def brea(self):
#         """Apply brakes to the vehicle."""
#         if self.engine:
#             self.speed = 0
#         print(f' Press break to the vehincle {self.speed}.')
#
# class Bus(Vehicle):
#     def __init__(self, brand, model, capacity, year):
#         super().__init__(brand, model, capacity, year)
#         self.capacity = capacity
#     def calculate_charge(self):
#       self.fare = super().calculate_charge() * 1.1
#
#     def calculate_total_fare(self):
#         initial_fare  = self.calculate_charge()
#         if self.calculate_charge.lower() == "Bus":
#             maintenance_charge = 0.1 * initial_fare
#             total_fare = initial_fare + maintenance_charge
#         else:
#             total_fare = initial_fare
#         return total_fare
#











'''EX 4
Lets say we have classes: A, B and C:
Modify the program to add a method say_hello to class A that prints "Hello from class A".
Modify the program to add a method say_hello to class B that prints "Hello from class B".
Modify the program to add a method say_hello to class C that prints "Hello from class C".
Create an object of class C and call the say_hello method on it. What is the output?
Modify the program so that class B's say_hello method calls the say_hello method of class A using the super() function.
Create an object of class C and call the say_hello method on it again. What is the output now?'''


class Animal:
    def __init__(self, name, habitat, species):
        self.name = name
        self.habitat = habitat
        self.species = species

    def Heterotrophy(self):
        #The Ability to Ingest Food
        pass
    def noise(self):
        pass
    def sound(self):
        pass

    def motility(self):
        pass

class Mammal(Animal):
    def __init__(self, name,species, habitat, diff_color, blooded_warm=True):
        super().__init__(name, species, habitat)
        self.diff_color = diff_color
        self.blooded_warm = blooded_warm

    def birth(self):
        pass
class Primate(Mammal):
    def __init__(self, name, species, habitat, fur_color, diet, opposable_thumbs=True):
        super().__init__(name, species, habitat, fur_color)
        self.diet = diet
        self.opposable_thumbs = opposable_thumbs   #All primates have opposable thumbs
    def playing(self):
        pass

    def swing(self):
        pass

class Chimpanzee(Primate):
    def __init__(self, name, habitat, diff_color="Brown and black", diet="Omnivore"):
        super().__init__(name, "Chimpanzee", habitat, diff_color, diet)

    def swing(self):
        return f"{self.name} they do swinging from tree to tree!"













