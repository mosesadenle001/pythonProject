# # class Employee:
# #     def __init__(self, name, salary):
# #         self.__name = name
# #         self._salary = salary
# #
# #     def get_yearly_salary(self):
# #         return self._get_salary() * 12
# #
# #     def _get_salary(self):
# #         return self._salary
# #
# #     def get_name(self):
# #         return self.__name
# #
# #
# #
# #
# #
# # employee = Employee("John", 4561)
# #
# # print(employee._salary)
# #
# # print(employee.get_yearly_salary())
# #
# # print(employee._get_salary())
# #
# # # print(employee.__name)
# #
# # print(employee.get_name())
# #
# #
# # engineer = Engineer("John", 52, 20, 5000, "Senior developer")
# #
# # engineer.show()
# #
# # engineer.print_data()
# #
# # designer = Designer("Tom", 54, 10, 4000, "UI designer", "skiing")
# #
# # designer.show()
# #
# # designer.show_hobbies()
# #
# #
# # def print_data(self):
# #     print(self.level)
# #
# #
# # class Designer(Employee, Person):
# #     def __init__(self, name, age, experience, salary, position, hobbies):
# #         Employee.__init__(self, name, age, experience, salary)
# #         Person.__init__(self, hobbies)
# #         self.position = position
# #
# #     def show(self):
# #         super().show()
# #         print(self.position)
#
#
# '''Four pillars of OOP'''
#
# class Parent:
#     def __init__(self):
#         # protected member
#         self._mobile_number = 5555551234
#
# class Parent:
#     def __init__(self):
#         self._mobile_number = "555456456"
#
#     @property  # (getter)
#     def mobile_number(self):
#         return self._mobile_number
#
#     @mobile_number.setter
#     def mobile_number(self, mobile_number):
#         if mobile_number.startswith("+"):
#             self._mobile_number = mobile_number
#         else:
#             self._mobile_number = f"+{mobile_number}"
#
#
# class Child(Parent):
#     def show_mobile_number(self):
#         print(self._mobile_number)
#
# child = Child()
# child.show_mobile_number()
#
# obj = Parent()
#
# print(obj._mobile_number)
#
# print(obj.mobile_number)
#
# obj.mobile_number = "77788999"
#
# print(obj.mobile_number)
#
#
# class Rectangle:
#     def __init__(self, length, breadth, colour):
#         self.length = length
#         self.breadth = breadth
#         self._colour = colour
#
#     def area(self):
#         return self.length * self.breadth
#
#     def show_colour(self):
#         print(self._colour)
#
# class Square(Rectangle):
#     def __init__(self, size, colour):
#         super().__init__(size, size, colour)
#
#
#
# rectangle = Rectangle(5, 6, "blue")
#
# square = Square(5, "red")
#
# print(square.area())
# print(rectangle.area())
#

'''EX1 Create a few examples of yourself where you show four pillars of OOP in action.'''

#Inheritance
#
# class Animals:
#     def __init__(self, names, mammals, birds, fish):
#         self._names = names
#         self._mammals = mammals
#         self._birds = birds
#         self._fish = fish
#
#     def speak(self):
#         pass
#
#     def swim(self):
#         pass
#
# class mammals(Animals):
#     def speak(self):
#         return "Woof"
#
# class birds(Animals):
#     def swim(self):
#         return "Swits"
#
# class fish(Animals):
#     def speak(self):
#        return "Hibs"
#
# print(mammals.names, "Talks:", mammals.speak())
# print(birds.name, "Talks:", birds.speak())
# print(fish.names, "Talk:", fish.swim())





'''EX2 Write a class called CoffeeShop, which has three instance variables:
name : a string (basically, of the shop)
menu : a list of items (of dict type), with each item containing the item (name of the item), 
type (whether a food or a drink) and price.
orders : an empty list
and seven methods:
add_order: adds the name of the item to the end of the orders list if it exists on the menu,
 otherwise, return "This item is currently unavailable!"
fulfill_order: if the orders list is not empty, return "The {item} is ready!". 
If the orders list is empty, return "All orders have been fulfilled!"
list_orders: returns the item names of the orders taken, otherwise, an empty list.
due_amount: returns the total amount due for the orders taken.
cheapest_item: returns the name of the cheapest item on the menu.
drinks_only: returns only the item names of type drink from the menu.
food_only: returns only the item names of type food from the menu.'''

class CoffeShop:
    def __init__(self, name: str, menu: dict):
        self.name = name
        self.menu = menu
        self.orders = []

def add_order(self, item):
    item_names = []
    for menu_item in self.menu:
        item_names.append(menu_item['name'])
    if item in item_names:
            self.orders.append(item)
    else:
        return 'This item is currently unavailable!'

def fulfill_order(self):
    if self.orders != []:
        item = self.orders.pop(0)
        return f'The {item} is ready!'
    else:
        return 'All orders have been fulfilled!'
        # {'name': 'burger', 'type': 'food', 'price': 15}

def list_orders(self):
    return self.orders

def due_amount(self):
    amount = 0
    for order in self.orders:
        for item in self.menu:
            if item['name'] == order:
                amount += item['price']
    return amount

def cheapest_item(self):
    cheapest_item = self.menu[0]
    for item in self.menu:
        if item['price'] < cheapest_item['price']:
            cheapest_item = item
    return cheapest_item

def drinks_only(self):
    drinks = []
    for item in self.menu:
        if item['type'] == 'drink':
            drinks.append(item['name'])
    return drinks

def food_only(self):
    food = []
    for item in self.menu:
        if item['type'] == 'food':
            food.append(item['name'])
            return food

menu = [{'name': 'burger', 'type': 'food', 'price': 15}, {'name': 'sandwich', 'type': 'food', 'price': 10},
       {'name': 'coke', 'type': 'drink', 'price': 2}, {'name': 'coffee', 'type': 'drink', 'price': 3}]
cafe = CoffeShop('Mac', menu)

cafe.add_order('coffee')
print(cafe.orders)
print(cafe.due_amount())
cafe.add_order('burger')
cafe.add_order('coke')
print(cafe.orders)
print(cafe.list_orders())
print(cafe.food_only())
print(cafe.drinks_only())
print(cafe.cheapest_item())
print(cafe.fulfill_order())
print(cafe.due_amount())





