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
        mul = math.pow(1.03, self.seniority())
        return self.starting_salary * mul


class Intern(Employ):
    def __init__(self, e_id, name, enter_year, starting_salary, duration):
        super().__init__(e_id, name, enter_year, starting_salary)
        self.duration = duration #month

    def salary(self):
        return self.starting_salary


class ForeignEmploy(Employ):
    def __init__(self, e_id, name, enter_year, starting_salary, country):
        super().__init__(e_id, name, enter_year, starting_salary)
        self.country = country

    def salary_usd(self):
        return self.salary()/30


def employ_list():
    emp1 = Intern("00101234", "Mary", "2023", 22000, 3)
    emp2 = Employ("10002345", "John", "2000", 22000)
    emp3 = Employ("10005555", "Aaron", "2019", 22000)
    emp4 = Intern("00101238", "Mark", "2022", 22000, 15)
    emp5 = Intern("00101243", "Hank", "2023", 22000, 3)
    emp6 = ForeignEmploy("20101209", "Laurentiu", "2022", 28000, "Belgium")
    emp7 = Employ("10005822", "Willie", "2020", 22000)
    emp8 = Employ("10000025", "Maggie", "1990", 22000)
    emp9 = ForeignEmploy("20101209", "Megha", "2021", 28000, "India")
    emp10 = ForeignEmploy("20101209", "Singh", "2021", 28000, "Belgium")
    return [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]

