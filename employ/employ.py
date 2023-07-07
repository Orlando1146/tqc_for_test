import datetime
import math

class Employ:
    def __init__(self, e_id, name, enter_year, starting_salary):
        self.e_id = e_id
        self.name = name
        self.enter_year = enter_year
        self.starting_salary = starting_salary

    def seniority(self):
        current_date_time = datetime.datetime.now()
        date = current_date_time.date()
        year = date.strftime("%Y")
        return int(year) - int(self.enter_year)

    def salary(self):
        mul = math.pow(1.05, self.seniority())
        return self.starting_salary * mul


class Intern(Employ):
    def __init__(self, e_id, name, enter_year, starting_salary, duration):
        super().__init__(e_id, name, enter_year, starting_salary)
        self.duration = duration #month

    def salary(self):
        return self.starting_salary


class Foreigner(Employ):
    def __int__(self, e_id, name, enter_year, starting_salary, country):
        super().__init__(e_id, name, enter_year, starting_salary)
        self.country = country

    def salary_usd(self):
        return self.salary()/30


class Temp (Employ):
    def __int__(self, e_id, name, enter_year, starting_salary, hour):
        super().__init__(e_id, name, enter_year, starting_salary)
        self.hour = hour

    def salary(self):
        return self.starting_salary*self.hour


emp1 = Intern("00101234", "Mary", "2023", 25000, 3)
emp2 = Employ("10002345", "John", "2000", 22000)
emp3 = Employ("10005555", "Aaron", "2019", 25000)
emp4 = Intern("00101238", "Mark", "2022", 25000, 15)
emp5 = Intern("00101243", "Hank", "2023", 25000, 3)

# 10002345
# John
# 2000
# 22000
# 10005555
# Aaron
# 2019
# 25000
# end
# 00101234
# Mary
# 2023
# 25000
# 3
# 00101238
# Mark
# 2022
# 25000
# 15
# 00101243
# Hank
# 2023
# 25000
# 3
# end