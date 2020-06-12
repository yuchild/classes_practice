class Employee:
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age
        self.email = first + '.' + last + '@fivemenow.com'