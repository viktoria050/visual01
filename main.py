class Employee:
    def __init__(self, name, salary):
        self.name = name  
        self.salary = salary  

    def describe(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department  

    def describe(self):
        print(f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}")



class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language  

    def describe(self):
        print(f"Developer: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}")



manager1 = Manager("Alice", 5000, "Sales")
manager2 = Manager("Bob", 6000, "IT")

developer1 = Developer("Charlie", 4000, "Python")
developer2 = Developer("Diana", 4500, "JavaScript")

manager1.describe()  
manager2.describe()  

developer1.describe() 
developer2.describe()  