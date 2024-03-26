from dataclasses import dataclass
from typing import List

''' EX4
You are tasked with designing an advanced Employee Management System using Python data classes,
functional programming operations, and various methods for analysis and manipulation of employee data.

Employee Class:
Create a data class named Employee to represent an employee. The class should have attributes for employee_id,
name, age, salary, and department.
Department Class: Create a data class named Department to represent a department.
The class should have attributes for department_id, name, and employe (List[Employee]).
Add a method named average_salary that calculates and returns the average salary of employees in the department.
EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple
departments and employees. The class should have an attribute for departments (List[Department]).

Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees
within that age range.
Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
Add a method named filter_employees_by_department that takes a department name and returns a list of employees in
that department.
Functional Operations:

Utilize functional programming operations such as map, filter, and sorted where appropriate in the
implementation of the methods. Demonstrate the use of these operations to enhance the readability and efficiency
 of your code.
Test Cases:
Create a sample dataset with multiple employees and departments to thoroughly test your system.
Use the implemented methods to perform various analyses, such as calculating average salaries,
sorting employees, and filtering employees by criteria.'''
@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    salary: int
    department: "Department"

    # def __lt__(self, other):
    # #     return self.salary < other.salary
    # in method return sorted(employees_by_salary)

@dataclass
class Department:
    department_id: int
    name: str
    employees: list[Employee]

    def average_salary(self):
        total_salaries = sum([employee.salary for employee in self.employees])
        if len(self.employees) == 0:
            return 0
        return total_salaries / len(self.employees)
@dataclass
class EmployeeManagement:
    departments: list[Department]
    def total_salary(self):
        total_salaries_departments = 0
        for department in self.departments:
            total_salaries = sum([employee.salary for employee in department.employees])
            total_salaries_departments = total_salaries_departments + total_salaries
        return total_salaries_departments
    def get_employees_in_age_range(self, min_age, max_age):
        age_range_employees = []
        for department in self.departments:
            for employee in department.employees:
                if min_age <= employee.age <= max_age:
                    age_range_employees.append(employee)
        return age_range_employees
    def sort_employees_by_salary(self):
        employees_by_salary = []
        for department in self.departments:
            # employees_by_salary += department.employees    # += means extend the list
            employees_by_salary.extend(department.employees)
        return sorted(employees_by_salary, key=lambda x: x.salary, reverse=True)
    def filter_employees_by_department(self, department_name: str):
        for department in self.departments:
            if department.name == department_name:
                return department.employees

"""
EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple departments and employees. 
The class should have an attribute for departments (List[Department]).

Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees 
within that age range.
Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
Add a method named filter_employees_by_department that takes a department name and returns a list of employees in that 
department.

"""
emp1 = Employee(1, "Tom", 25, 1500, None)
emp2 = Employee(2, "Tim", 27, 1855, None)
emp3 = Employee(3, "John", 66, 2000, None)
emp4 = Employee(4, "Sam", 55, 2500, None)

dep1 = Department(11, "IT", [emp1, emp2])
dep2 = Department(12, "Finance", [emp3, emp4])

empmng = EmployeeManagement([dep1, dep2])
print(empmng.get_employees_in_age_range(15, 28))
print(empmng.sort_employees_by_salary())
print(empmng.filter_employees_by_department("IT"))

print(dep1.average_salary())
print(empmng.total_salary())


'''EX 5 Create a flight ticketing mini system:
-The CLI should ask you to choose departure place and destination (minimum 5 cities) 
(Use dictionary to create a distance between the cities matrix map ).

-Then it should show options for at least 3 flight options with different 
different aircraft (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300). 
Every aircraft has different seat configuration (economy, business, first with different seat amount, 
seat pitch and average price)

-When you select the ticket (the provided option) the final cost should be calculated depending on aircraft type, 
departure time, and fuel consumption. (We can agree that flights that are departure earlier, 
has less seats and older, cost more). Use data classes and simple classes to achieve the result.'''

