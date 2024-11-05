
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post


employee = Employee("Rahul", "886012", 50000, "Manager")
employee.display()


