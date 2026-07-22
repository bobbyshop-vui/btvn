print("=== Bai 1 ===")

class Phone:
    def __init__(self, name, battery_percent):
        if name == "":
            raise ValueError("Ten dien thoai khong duoc de trong")
        if battery_percent < 0 or battery_percent > 100:
            raise ValueError("Pin phai tu 0 den 100")
        self.name = name
        self.battery_percent = battery_percent

    def use(self, percent):
        if percent > self.battery_percent:
            print("Not enough battery!")
        else:
            self.battery_percent = self.battery_percent - percent
            print("Used " + str(percent) + "% battery. Battery left: " + str(self.battery_percent) + "%")

    def charge(self, percent):
        self.battery_percent = self.battery_percent + percent
        if self.battery_percent > 100:
            self.battery_percent = 100
        print("Charged. Current battery: " + str(self.battery_percent) + "%")

p = Phone("iPhone 15", 80)
p.use(30)
p.charge(40)
p.use(100)

print("=== Bai 2 ===")

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Chieu dai va chieu rong phai lon hon 0")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def is_square(self):
        return self.length == self.width

r = Rectangle(6, 4)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
print("Is square:", r.is_square())

print("=== Bai 3 ===")

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Ban kinh phai lon hon 0")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())
print("Circumference:", c.circumference())
c.radius = 10
print("Area after changing radius:", c.area())

print("=== Bai 4 ===")

class BankAccount:
    def __init__(self, owner, balance):
        if owner == "":
            raise ValueError("Ten chu tai khoan khong duoc de trong")
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("So tien nap phai lon hon 0")
        else:
            self.__balance = self.__balance + amount
            print("Deposited " + str(amount) + ". Current balance: " + str(self.__balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("So tien rut phai lon hon 0")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance = self.__balance - amount
            print("Withdrew " + str(amount) + ". Current balance: " + str(self.__balance))

acc = BankAccount("Tran Thi Binh", 1000000)
acc.deposit(500000)
acc.withdraw(300000)
acc.withdraw(5000000)
print("Final balance of " + acc.owner + ": " + str(acc.get_balance()))

print("=== Bai 5 ===")

class Employee:
    def __init__(self, name, base_salary):
        if name == "":
            raise ValueError("Ten khong duoc de trong")
        if base_salary <= 0:
            raise ValueError("Luong co ban phai lon hon 0")
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self, working_days):
        return self.base_salary / 26 * working_days

emp = Employee("Le Van Cuong", 7800000)
salary = emp.calculate_salary(24)
print("Net salary of " + emp.name + " (24 days): " + str(salary))

print("=== Bai 6 ===")

class Contact:
    def __init__(self, name, phone):
        if name == "":
            raise ValueError("Ten khong duoc de trong")
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("So dien thoai phai co dung 10 chu so")
        self.name = name
        self.phone = phone

class ContactManager:
    def __init__(self):
        self.__contacts = []

    def __show_contacts(self):
        if len(self.__contacts) == 0:
            print("Danh ba trong.")
        else:
            for i in range(len(self.__contacts)):
                c = self.__contacts[i]
                print(str(i + 1) + ". " + c.name + " - " + c.phone)

    def __add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        try:
            c = Contact(name, phone)
            self.__contacts.append(c)
            print("Contact added!")
        except ValueError as e:
            print(e)

    def __search_by_name(self):
        name = input("Enter name to search: ")
        found = False
        for c in self.__contacts:
            if c.name.lower() == name.lower():
                print("Found: " + c.name + " - " + c.phone)
                found = True
                break
        if not found:
            print("Not found.")

    def run(self):
        while True:
            print("--- CONTACT MANAGER ---")
            print("1. Show contacts")
            print("2. Add contact")
            print("3. Search by name")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.__show_contacts()
            elif choice == "2":
                self.__add_contact()
            elif choice == "3":
                self.__search_by_name()
            elif choice == "4":
                break
            else:
                print("Lua chon khong hop le.")

cm = ContactManager()
cm.run()

print("=== Bai 7 ===")

class ShoppingCart:
    def __init__(self, customer_name):
        if customer_name == "":
            raise ValueError("Ten khach hang khong duoc de trong")
        self.customer_name = customer_name
        self.__product_names = []
        self.__prices = []

    def add_product(self, name, price):
        if price <= 0:
            print("Gia san pham phai lon hon 0")
        else:
            self.__product_names.append(name)
            self.__prices.append(price)
            print("Added \"" + name + "\" to the cart.")

    def total(self):
        return sum(self.__prices)

    def print_cart(self):
        print("Cart of " + self.customer_name + ":")
        for i in range(len(self.__product_names)):
            print(str(i + 1) + ". " + self.__product_names[i] + " - " + str(self.__prices[i]))
        print("Total: " + str(self.total()))

cart = ShoppingCart("Pham Thu Ha")
cart.add_product("T-shirt", 150000)
cart.add_product("Jeans", 350000)
cart.add_product("Cap", 90000)
cart.print_cart()

print("=== Bai 8 ===")

class Book:
    def __init__(self, title, author):
        if title == "":
            raise ValueError("Tieu de sach khong duoc de trong")
        if author == "":
            raise ValueError("Tac gia khong duoc de trong")
        self.title = title
        self.author = author
        self.__is_borrowed = False

    def borrow(self):
        if self.__is_borrowed:
            print("Book \"" + self.title + "\" is already borrowed!")
        else:
            self.__is_borrowed = True
            print("You have borrowed \"" + self.title + "\".")

    def return_book(self):
        if not self.__is_borrowed:
            print("Book \"" + self.title + "\" is already on the shelf.")
        else:
            self.__is_borrowed = False
            print("You have returned \"" + self.title + "\".")

b = Book("Python Programming", "John")
b.borrow()
b.borrow()
b.return_book()
b.return_book()

print("=== Bai 9 ===")

class TemperatureSensor:
    def __init__(self, location):
        if location == "":
            raise ValueError("Vi tri khong duoc de trong")
        self.location = location
        self.__readings = []

    def record(self, temperature):
        if temperature < -50 or temperature > 100:
            print("Nhiet do khong hop le.")
        else:
            self.__readings.append(temperature)

    def average(self):
        if len(self.__readings) == 0:
            return 0
        return sum(self.__readings) / len(self.__readings)

    def highest(self):
        if len(self.__readings) == 0:
            return None
        return max(self.__readings)

sensor = TemperatureSensor("Server Room")
sensor.record(28.5)
sensor.record(30.2)
sensor.record(27.8)
print("Sensor at " + sensor.location)
print("Average temperature:", sensor.average())
print("Highest temperature:", sensor.highest())

print("=== Bai 10 ===")

class Screening:
    def __init__(self, movie_name, total_seats):
        if movie_name == "":
            raise ValueError("Ten phim khong duoc de trong")
        if total_seats <= 0:
            raise ValueError("Tong so ghe phai lon hon 0")
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.__booked_seats = 0

    def get_available_seats(self):
        return self.total_seats - self.__booked_seats

    def book(self, quantity):
        if quantity <= 0:
            print("So luong ve phai lon hon 0")
        elif quantity > self.get_available_seats():
            print("Not enough seats! Only " + str(self.get_available_seats()) + " left.")
        else:
            self.__booked_seats = self.__booked_seats + quantity
            print("Booked " + str(quantity) + " tickets. " + str(self.get_available_seats()) + " seats left.")

s = Screening("Avengers", 50)
s.book(3)
s.book(48)
s.book(2)
print("Movie \"" + s.movie_name + "\" has " + str(s.get_available_seats()) + " seats left.")
