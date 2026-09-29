"""1. Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes
and override the area() method in each class. Create objects of each class and demonstrate
runtime polymorphism."""

class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def area(self):
        r = 5
        print("Area of Circle:", 3.14 * r * r)


class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Area of Rectangle:", l * b)


class Triangle(Shape):
    def area(self):
        b = 10
        h = 6
        print("Area of Triangle:", 0.5 * b * h)


shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()

"""2. Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and
Tester classes. Override the method in each class to calculate salary according to the employee&#39;s
role.
3. Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override
start() to display the starting behavior of each vehicle.
4. Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion.
Override sound() in each class to display the appropriate sound.
5. Create a base class Notification with a method send(). Derive EmailNotification,
SMSNotification, and PushNotification. Override send() to display the appropriate notification
method.
6. Create a base class Student with a method calculate_grade(). Derive EngineeringStudent,
MedicalStudent, and ManagementStudent. Override the method according to different grading
criteria.
7. Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount,
CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently
for each account type.
8. Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and
HTMLReport. Override generate() in each class. Write a function that accepts any report object
and calls generate().
9. Create a class Distance with feet and inches. Overload the + operator to add two distance objects
and display the result in normalized form.
10. Create a class Student containing the student&#39;s name and total marks. Overload the &gt; and &lt;
operators to compare the marks of two students.