"""1.Create a class Employee with attributes emp_id, name, and salary. Create a derived class
Manager that inherits from Employee and contains an additional attribute department. Display all
employee and manager details and calculate the manager&#39;s annual salary."""

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m = Manager(101, "Rahul", 50000, "IT")
m.display_manager()

"""2. Create a base class Vehicle with attributes brand and model. Create a derived class Car with
additional attributes fuel_type and price. Define methods to display vehicle details and calculate
the discounted price of the car."""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self):
        discount = self.price * 0.10
        return self.price - discount


c = Car("Toyota", "Innova", "Petrol", 2000000)
c.display_car()
print("Discounted Price:", c.discounted_price())

"""3. Create two classes Academic and Sports. The Academic class should store marks obtained by a
student, while the Sports class should store sports points. Create a class Student that inherits from
both classes and calculates the student&#39;s overall performance."""

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        overall = self.marks + self.points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", overall)


s = Student(85, 15)
s.performance()

"""4. Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name
and age in the first class and employee ID, designation, and salary in the second class. Create an
Employee class that inherits from both classes and displays complete employee information."""

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = Employee("Priya", 25, 102, "Developer", 60000)
e.display()

"""5. Create a class Person containing name and age. Derive a class Student from Person with roll
number and course. Further derive a class ResearchStudent from Student with research topic and
guide name. Display all details."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)


r = ResearchStudent(
    "Amit", 24, 101, "BTech CSE",
    "Artificial Intelligence", "Dr. Sharma"
)

r.display()

"""6. Create a base class BankAccount with account number and balance. Derive SavingsAccount from
it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define
methods to calculate interest and display account details."""

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        interest = self.calculate_interest()

        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", interest)
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(12345, 100000, 6, "Free ATM and Lounge Access")
p.display()

"""7. Create a base class Shape containing a method to display the name of the shape. Create three
derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to
calculate the area."""

class Shape:
    def display(self, name):
        print("Shape:", name)


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, width):
        return length * width


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


c = Circle()
c.display("Circle")
print("Area:", c.area(5))

r = Rectangle()
r.display("Rectangle")
print("Area:", r.area(10, 5))

t = Triangle()
t.display("Triangle")
print("Area:", t.area(10, 6))

"""8. Create a base class Employee containing employee ID, name, and basic salary. Create derived
classes Manager, Developer, and Tester. Each derived class should calculate salary differently
based on its respective allowances."""

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.10


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())

"""9. Create a class Person. Derive Student and Faculty from Person. Create another class
TeachingAssistant that inherits from both Student and Faculty. Display the details and
demonstrate the use of multiple and hierarchical inheritance together."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Sneha", 22, 101, "Python")
ta.display()

"""10. Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that
inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes
and methods to demonstrate a combination of inheritance types."""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Sports Car:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Electric Bike:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


sc = SportsCar("BMW", "M4", 250)
sc.display()

eb = ElectricBike("Ola", "S1", 4)
eb.display()