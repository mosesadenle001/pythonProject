'''EX1 You have been asked to create a simple inventory management system for a small retail store.
You need to define a Product class using the dataclass module that represents a product in the store.
Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock.
You also need to implement a method calculate_total_cost that calculates the total cost of a given number of items
of the product,taking into account any discounts that may apply.'''
from dataclasses import dataclass
@dataclass
class Product:
    product_id: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_total_cost(self, number_of_items: int) -> float:
        total_cost = number_of_items * self.price
        # let apply discounts when quantity purchased is greater than or equal 20
        if number_of_items >= 20:
            discount_allow = total_cost * 0.3  # 30% discount
            #
            total_cost -= discount_allow        #total cost discount has to be removed from TC
        return total_cost

# Example usage:
product1 = Product(1, "Car", "Latest hybrid car", 50000.00, 50)
product2 = Product(2, "Apartment", "smart model home", 100800.00, 40)

# Calculate total cost for purchasing 21 laptops
total_cost_car = product1.calculate_total_cost(21)

# Calculate total cost for purchasing 20 smartphones
total_cost_apartment = product2.calculate_total_cost(12)

print("Total cost for 21 car after discount:", total_cost_car)
print("Total cost for 20 apartment after discount:", total_cost_apartment)



'''MORE Exercises: Space Station Personnel Management
Objective:
Apply concepts of immutable dataclasses, inheritance, and default values using the field(default_factory) 
method in the context of a space station personnel management system.
Instructions:
-Base Class - CrewMember:
Create a base class named CrewMember with an immutable dataclass.		
The dataclass should have felds for name (string), age (integer), and position (string).
-Derived Class - Astronaut:
Create a derived class named Astronaut that inherits from the CrewMember class.
Add an additional field to the Astronaut class: missions_completed (integer).
Utilize the field(default_factory) method to set a default value of 0 for missions_completed.
-Derived Class - Engineer:
Create another derived class named Engineer that also inherits from the CrewMember class.
Add a field for specialization (string).
Set a default value of "Generalist" for the specialization field using the field(default_factory) method.
-Create Instances:		
Instantiate a CrewMember object with the name "Commander Smith", age 45, and position "Commander".
Instantiate an Astronaut object with the name "Dr. Williams", age 40, position "Astrophysicist", 
and missions completed.		
Instantiate an Engineer object with the name "Engineer Johnson", age 35, and position "Mechanical Engineer".
Demonstrate Immutability:
Attempt to modify a field in one of the instances (e.g., change the name of the Astronaut).		
Observe and explain the error that occurs due to the immutability of the dataclasses. '''

from dataclasses import dataclass, field

@dataclass
class CrewMember:
    name: str
    age: int
    position: str

@dataclass
class Astronaut(CrewMember):
    missions_completed: int = field(default_factory=lambda: 0)

@dataclass
class Engineer(CrewMember):
    specialization: str = field(default_factory=lambda: "Generalist")

crew_member = CrewMember("Commander Smith", 45, "Commander")
astronaut = Astronaut("Dr. Williams", 40, "Astrophysicist")
engineer = Engineer("Engineer Johnson", 35, "Mechanical Engineer")

