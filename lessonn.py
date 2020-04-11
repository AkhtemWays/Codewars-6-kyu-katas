import datetime
class Employee:
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    @classmethod
    def change_raise_amt(cls, amt):
        cls.raise_amt = amt
        return cls.raise_amt
    @classmethod
    def Alter_constr(cls, data):
        first, last, pay = data.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    def __add__(self, other):
        print(self.fullname(), other.fullname())
        return self.pay + other.pay
    def __sub__(self, other):
        print(self.fullname(), other.fullname())
        return self.pay - other.pay
    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first, self.last, self.pay)
    def __str__(self):
        return 'name is {}, surname is {} and salary is {}'.format(
            self.first, self.last, self.pay
        )
    def __mul__(self, other):
        return self.pay * other.pay


class Developer(Employee):
    raise_amt = 1.09
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.__prog_lang = prog_lang
    def PrLang(self):
        return self.__prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None: self.__employees = []
        else: self.__employees = employees
    def PrintEmps(self):
        for emp in self.__employees:
            print('-->', emp.fullname())
    def Add_emp(self, emp):
        if emp not in self.__employees:
            self.__employees.append(emp)
    def Remove_emp(self, emp):
        if emp in self.__employees:
            self.__employees.remove(emp)
    def get_data(self):
        return self.__employees





emp_1 = Employee('Corey', 'Askren', 58000)
emp_2 = Employee('Ben', 'Kerrel', 65000)
emp_3 = Employee('Rachel', 'Griffin', 75000)


date = datetime.date(2020, 4, 10)
dev_1 = Developer('Lincoln', 'Badger', 99000, 'Python')
dev_2 = Developer('Bernard', 'Show', 102000, 'C++')
mgr_1 = Manager('Tahir', 'Kurbanov', 130000, [dev_1])
print(mgr_1._Manager__employees)




