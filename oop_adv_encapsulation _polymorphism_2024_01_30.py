
'''Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and Space Shuttle classes.
Create a simple calculator with:
Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).
Through the main class you should be able to calculate the mission cost which includes:
fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) ,
average personals expenditures ( ppl x base_salary ).
Prepare the final report in the file document and
on screen with a method get_full_report with all gathered and calculated data.'''


class BaseSpacecraft:
    def __init__(self, age, cost, year_built, weight, capacity):
        # information about the Spacecraft via functionality and attributes
        # using get method
        self.age = age
        self.cost = cost
        self.year_built = year_built
        self.weight = weight
        self.capacity = capacity


    def get_age(self):
        return self.age

    def get_cost(self):
        return self.cost
    def get_year_built(self):
        return self.year_built
    def get_weight(self):
        return self.weight
    def get_capacity(self):
        return self.capacity

spacecraft = BaseSpacecraft(age=25, cost=300000000, year_built=1999, weight=8000, capacity=220)
class SpaceShuttle(BaseSpacecraft):
    def __init__(self, age, cost, year_built, weight, capacity, burn_rate):
        super().__init__(age, cost, year_built, weight, capacity)
        self.burn_rate = burn_rate
    def get_burn_rate(self):
        return self.burn_rate

    class MissionCalculator:

        orbit_price = 2500
        base_salary = 10000
        fuel_cost = 5
        # average personals expenditures == people x base_salary
        def __init__(self, spacecraft, orbit_price,base_salary, fuel_cost, orbit_height, personnel_expenditure, people_cost, total_cost):
            self.spacecraft = spacecraft
            self.orbit_price = orbit_price
            self.base_salary = base_salary
            self.fuel_cost = fuel_cost
            self.orbit_height = orbit_height
            self.personnel_count = personnel_expenditure
            self.people_cost = people_cost
            self.total_cost = total_cost


    def calculate_fuel_cost(self):
        burn_rate_variable = self.orbit_price / self.orbit_height
        fuel_cost = self.fuel_cost * self.spacecraft.get_burn_rate() * burn_rate_variable
        return fuel_cost

     def calculate_personnel_cost(self):
     return self.base_salary * self.personnel_expenditure

    def calculate_mission_cost(self):
        fuel_cost = self.calculate_fuel_cost()
        people_cost = self.calculate_personnel_cost()
        total_cost = fuel_cost + people_cost
        return total_cost


shuttle = SpaceShuttle(age=25, cost=300000000, year_built=1999, weight=8000, burn_rate=0.08)
calculator = MissionCalculator(spacecraft=shuttle, orbit_height=320, personnel_expenditure=200)

print("Space Shuttle Info:")
print("Age:", shuttle.get_age())
print("Cost:", shuttle.get_cost())
print("Year Built:", shuttle.get_year_built())
print("Weight:", shuttle.get_weight())
print("Fuel Capacity:", shuttle.get_fuel_capacity())
print("Mission Cost:")
print("Fuel Cost:", calculator.calculate_fuel_cost())
print("Personnel Cost:", calculator.calculate_personnel_cost())
print("Total Mission Cost:", calculator.calculate_mission_cost())


def get_full_report(self):
    report = f"Mission Report:\n\n" \
             f"Spacecraft Information:\n" \
             f"  Age: {self.spacecraft.get_age()} years\n" \
             f"  Cost: ${self.spacecraft.get_cost()}\n" \
             f"  Year Built: {self.spacecraft.get_year_built()}\n" \
             f"  Weight: {self.spacecraft.get_weight()} kg\n" \
             f"  Burn Rate: {self.spacecraft.get_burn_rate()} kg/mile\n\n" \
             f"Mission Expenses:\n" \
             f"  Fuel Cost: ${self.calculate_fuel_cost():.2f}\n" \
             f"  Personnel Cost: ${self.calculate_personnel_cost():.2f}\n\n" \
             f"Total Mission Cost: ${self.calculate_mission_cost():.2f}"
    return report

print(calculator.get_full_report())

with open("mission_report.txt", "w") as file:
    file.write(calculator.get_full_report())

print("\nReport has been saved to 'mission_report.txt'.")



'''Cafeteria project : Create an live menu and payment system (a.k.a console program) :
First the program should ask if table was reserved/ not (Providing your full name) .
And then if not would assign you a table (there is a specific number single, double or family tables) .
 After table is assigned to you, system should show how many free tables are and how which are reserved/occupied. 
 The system must be able to show name/surname of the person of the reserved 
 table (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)
After assigning table, system should show different menu options for breakfast, lunch , dinner , 
drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan 
must be included too in the special menu. All menu items should have weight, preparation time in minutes, 
calories, and price.I have to have an option to change the order before the payment section. 
Thus I can delete, add more, update amount of the same order.
I should be able to choose whatever I want from all menus in one ordering. 
After I finish, I need to see what I chosen, the full payable amount and approx waiting 
time for the food to be served
Add an option to add tips (% from the full cost) to the final bill.
After the payment , system should generate the receipt (logging).'''














