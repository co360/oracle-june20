class employee:

    # data/properties/attributes

    def __init__(self, empname, empage, empcompany, empcountry):
        self.name = empname
        self.age = empage
        self.salary = 0
        self.company = empcompany
        self.country = empcountry
        self.tax = 0

    # functions/mothods

    def printstatus(self):
        print("SELF:", self)
        print(self.name, self.company, self.country)
        print('------------------------------------')
        print(self.salary, self.tax)
        print('\n')

    def setsalary(self, amount):
        self.salary = amount

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * self.salary

    def gettax(self):
        return self.tax


# -------------------------------------------------------------- #

emp1 = employee('Anil', 35, 'oracle', 'India')
emp2 = employee('Raj', 36, 'genpact', 'India')

emp1.printstatus()
emp2.printstatus()

emp1.setsalary(100000)
emp2.setsalary(200000)

emp1.printstatus()
emp2.printstatus()

emp1.calctax()
emp2.calctax()

emp1.printstatus()
emp2.printstatus()
