# A getter method to get its value.
# A setter method to set its value.
# A deleter method to delete it.
class Person:
    def __init__(self, name, age, friends):
        self._name = name
        self._age = age
        self._friends = friends

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, age: int):
        # date validation
        if 0 <= age <= 150:
            self._age = age
        else:
            raise ValueError( "Age is not valid")
    def del_age(self):
        self._age = None
    def del_friends(self):
        return self._friends

    #     To define property while it is still empty
    def del_friends(self):
        self._friends = []

pers1 = Person('Paulius', 12, ['John', 'Mery'])
pers2 = Person('John', 22, ['Paulius'])

print(pers1.get_name(), pers1.get_age(), pers1.get_friends())
pers1.del_age()
pers1.del_friends()
print(pers1.get_name(), pers1.get_age(), pers1.get_friends())

#let use @property decoration and see how it construct
class Person:
    def __init__(self, name, age, friends):
        self._name = name
        self._age = age
        self._friends = friends

@property
        def name(self):
        return self._name

@property
    def age(self):
        return self._age
    def set_age(self, age: int):
        # date validation
        if 0 <= age <= 150:
            self._age = age
        else:
            raise ValueError( "Age is not valid")
    def del_age(self):
        self._age = None
@property
    def friends(self):
        return self._friends

    #     To define property while it is still empty
    def del_friends(self):
        self._friends = []

pers1 = Person('Paulius', 12, ['John', 'Mery'])
pers2 = Person('John', 22, ['Paulius'])

print(pers1.name, pers1.age, pers1.friends)
pers1.del_age()
pers1.del_friends()
print(pers1.name, pers1.age, pers1.friends)


# Add setter
class Person:
    def __init__(self, name, age, friends):

    # Direct setting
    # self._name = name
    # self._age = age
    # self._friends = friends

    # Property setting (using data validation potentially!)
    self.name = name
    self.age = age
    self.friends = friends

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a: int):

# Data validation
     if 0 <= a <= 150:
        self._age = a
     else:
        raise ValueError("Age is not valid!")

    def del_age(self):
        self._age = None

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend_list: list):

    # Data validation
    for friend in friend_list:
        if not isinstance(friend, str):
            raise ValueError(f"{friend} is not string!")

    if len(friend) == 0:
        raise ValueError("There is a friend with no name!")

    self._friends = friend_list.copy()

    def del_friends(self):
        self._friends = []


pers1 = Person("Paulius", 12, ["john", "mary"])
pers2 = Person("John", 22, ["paulius"])

# pers1.age = -2

print(pers1.name, pers1.age, pers1.friends)
pers1.del_age()
pers1.del_friends()
print(pers1.name, pers1.age, pers1.friends)

# add deletter

class Person:
    def __init__(self, name, age, friends):

    # Direct setting
    # self._name = name
    # self._age = age
    # self._friends = friends

    # Property setting (using data validation potentially!)
    self.name = name
    self.age = age
    self.friends = friends

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n
    @name.deleter
    def name(self,):
        del.self._name



    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a: int):

    # Data validation
      if 0 <= a <= 150:
        self._age = a
      else:
        raise ValueError("Age is not valid!")
    @age.deleter
    def del_age(self):
        self._age = None

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend_list: list):

    # Data validation
    for friend in friend_list:
        if not isinstance(friend, str):
            raise ValueError(f"{friend} is not string!")

    if len(friend) == 0:
        raise ValueError("There is a friend with no name!")
        self._friends = friend_list.copy()


     @friends.deleter
    def del_friends(self):
        self._friends = []


pers1 = Person("Paulius", 12, ["john", "mary"])
pers2 = Person("John", 22, ["paulius"])

# pers1.age = -2

print(pers1.name, pers1.age, pers1.friends)
del pers1.name  #output  None means  call delete method #output
del pers1.friends
print(pers1.name, pers1.age, pers1.friends)


# Another way is @property decoration to control access to class attributes using encapsulation

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

rect1 = Rectangle(3.0, 4.0)
print(rect1.width, rect1.height, rect1.area)   # if we call area as a method i.e we add () after area
                                                 # it will show error bcoz we already have @property decoration









class Person:
    def __init__(self, name, age, friends):

# Direct setting
    # self._name = name
    # self._age = age
    # self._friends = friends

    # Property setting (using data validation potentially!)
    self.name = name
    self.age = age
    self.friends = friends

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a: int):

    # Data validation
    if 0 <= a <= 150:
        self._age = a
    else:
        raise ValueError("Age is not valid!")

    def del_age(self):
        self._age = None

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend_list: list):

     # Data validation
    for friend in friend_list:
        if not isinstance(friend, str):
            raise ValueError(f"{friend} is not string!")

    if len(friend) == 0:
        raise ValueError("There is a friend with no name!")

    self._friends = friend_list.copy()

    def del_friends(self):
        self._friends = []


pers1 = Person("Paulius", 12, ["john", "mary"])
pers2 = Person("John", 22, ["paulius"])

# pers1.age = -2

print(pers1.name, pers1.age, pers1.friends)
pers1.del_age()
pers1.del_friends()
print(pers1.name, pers1.age, pers1.friends)


''''''