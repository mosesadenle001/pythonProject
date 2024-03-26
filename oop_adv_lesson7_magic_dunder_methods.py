class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        """String representation of an object. Evaluated on print(object)"""
        return f"Person's name is {self.name}, their age is {self.age}"
    def __repr__(self):
        """Unambiguous string representation of an object. Evaluated on repr(object)"""
        return f"Person('{self.name}', {self.age})"
    def __eq__(self, other: 'Person'):
        """Equal. Compare self to other object. Evaluated on =="""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    def __ne__(self, other: 'Person'):
        """Not equal. Compare self to other object. Evaluated on !="""
        if isinstance(other, Person):
            return self.name != other.name or self.age != other.age
        else:
            return True

pers = Person("john", 33)
print(pers)
person_represantation = repr(pers)  # "Person('john', 33)"
print(person_represantation)
pers2 = eval(person_represantation)
print(pers2)
pers2 = Person("mary", 25)
pers3 = Person("john", 33)
print(pers)



#2rd class KARINA
a = str(5)

# if a > b :

print("hi" > "hello")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __eq__(self, other):
        if isinstance(other, Car):
            if self.make == other.make and self.model == other.model and self.year == other.year:
                return True
        return False

car1 = Car("Toyota", "Prius", 2010)
car2 = Car("Toyota", "Prius", 2010)
car3 = Car("Nissan", "Leaf", 2020)

if car1 == car3:
    print("They are the same car")
else:
    print("Those are different cars")

"Hello" + "World"
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        raise TypeError(f"unsupported operand type(s) for +: 'Vector' and '{type(other).__name__}'")
    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

vector1 = Vector(5, 4)
vector2 = Vector(3, -6)

print(vector1)

print(vector2 + vector1)
print(vector1 + 5)
print(5 + vector1)
class Train:
    def __init__(self, wagons):
        self.wagons = wagons
    def __len__(self):
        return self.wagons

train = Train(5)

print(len(train))






'''EX1 Create a class called Product that takes a name and price as 
parameters and has __str__ and __repr__ methods defined.
The __str__ method should return a string in the format "Product: name, Price: price"
The __repr__ method should return a string in the format "Product('name', price)"'''
class Product:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price
    def __str__(self):
        '''The __str__ method should return a string'''
        return f"Product: {self.name}, Price: {self.price} Euro"

    def __repr__(self):
        '''The __repr__ method should return a string'''
        return f"Product('{self.name}', {self.price} Euro)"
product = Product('Apartment', 100000,)
print(str(product))
print(repr(product))

'''EX2 Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.
The __bool__ method should return True if the queue has any items and False if it is empty.
The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
The __len__ method should return the number of items in the queue.'''

class MyQueue:
    def __init__(self):
        self.items = 0
    def __bool__(self):
        return bool(self.items)
    def __repr__(self):
        return f'MyQueue({self.items})'
    def __len__(self):
        return len(self.items)

Queue = MyQueue()
print(bool(Queue))
Queue.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bool(Queue))
print(repr(Queue))
print(len(Queue))

'''EX3 Create a class called Book that takes title, author, and ISBN as parameters. 
The class should have __bool__, __repr__, __len__, __str__, __eq__, __add__, and __getitem__ methods defined.
The __bool__ method should return True if the book has a title, False otherwise.
The __repr__ method should return a string in the format "Book(title, author, ISBN)" 
where title, author and ISBN are the respective attributes of the class
The __len__ method should return the number of pages of the book
The __str__ method should return a string in the format "title by author (ISBN)"
The __eq__ method should compare two books and return True if both ISBN are the same and False otherwise.
The __add__ method should add two books and return a new book object that contains the contents of both 
books concatenated and the title of the new book should be the title of the first book
The __getitem__ method should return the title of the book if the index passed is 0, 
and the author of the book if the index passed is 1.'''
#
# class Book:
#     def __init__(self, title, author, ISBN, pages=0):
#         self.title = title
#         self.author = author
#         self.ISBN = ISBN
#         self.pages = pages

class Book:
    def __init__(self, title: str, author: str, ISBN: int, pages_number: int):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.pages_number = pages_number

    def __bool__(self):
        return len(self.title) != 0

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.ISBN})'

    def __len__(self):
        return self.pages_number

    def __str__(self):
        return f'{self.title} by {self.author} ({self.ISBN})'

    def __eq__(self, other: 'Book') -> bool:
        if isinstance(other, Book):
            return self.ISBN == other.ISBN
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            if other.author == self.author:
                author = self.author
            else:
                author = self.author + ', ' + other.author
            return Book(self.title, author, self.ISBN, other.pages_number + self.pages_number)
        raise TypeError()

    def __getitem__(self, ind: int):
        if ind == 0:
            return self.title
        elif ind == 1:
            return self.author
        raise IndexError('The index doesn\'t exist')


book1 = Book('Alice in Wonderland', 'Lewis Caroll', 90871456869, 313)
book2 = Book('Harry Potter', 'J.K. Rowling', 9780545582889, 500)

# Test __bool__ method
print(bool(book1))
print(bool(Book('', '', 0, 0)))

# Test __repr__ method
print(repr(book1))

# Test __len__ method
print(len(book1))

# Test __str__ method
print(str(book1))

# Test __eq__ method
print(book1 == book2)

# Test __add__ method
book3 = book1 + book2
print(book3)
print(len(book3))

# Test __getitem__ method
print(book1[0])
print(book1[1])



'''Create three different task with real world scenario what would include all magic methods 
we covered today and plus 3 others from the provided list.'''
# Answer     Online Bookstore Inventory Management System:
#         Scenario: You're developing an inventory management system for an online bookstore.
#         Magic Methods Used:
#             __repr__: Display book details in a user-friendly format.
#             __len__: Get the number of books in the inventory.
#             __str__: Display book details for customers.
#             __eq__: Compare books based on ISBN.
#             __add__: Combine two book inventories.
#             __getitem__: Access book title or author based on index.
#             __setattr__: Modify book details, such as price or availability.
#             __getattr__: Retrieve book details, such as price or availability.
#             __iter__: Iterate over the inventory.
#         Example Task: Implement methods to add, remove, and update book details in the inventory.
#         Allow customers to search for books by title or author and display available quantities.
#
#     Social Media Platform User Management System:
#         Scenario: You're building a user management system for a social media platform.
#         Magic Methods Used:
#             __repr__: Display user profile details.
#             __len__: Get the total number of users.
#             __str__: Display user details in a user-friendly format.
#             __eq__: Compare users based on username or email.
#             __add__: Combine user databases.
#             __getitem__: Access user profile details.
#             __setattr__: Update user profile information.
#             __getattr__: Retrieve user profile information.
#             __iter__: Iterate over the user database.
#         Example Task: Implement methods to add, delete, and update user profiles.
#         Allow users to search for other users by username or email and display their profiles.
#
#     E-commerce Website Shopping Cart System:
#         Scenario: You're developing a shopping cart system for an e-commerce website.
#         Magic Methods Used:
#             __repr__: Display product details.
#             __len__: Get the total number of items in the cart.
#             __str__: Display cart contents for users.
#             __eq__: Compare products based on product code.
#             __add__: Combine two shopping carts.
#             __getitem__: Access product details.
#             __setattr__: Update product quantities or prices.
#             __getattr__: Retrieve product information.
#             __iter__: Iterate over the items in the cart.
#         Example Task: Implement methods to add, remove, and update products in the shopping cart.
#         Allow users to view their cart, adjust quantities, and proceed to checkout.
