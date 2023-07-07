from employ import Employ
from employ import Intern
from employ import ForeignEmploy
# from employ import employ_list

import employ as ep

employ_list = ep.employ_list()

def find_salary_under_30k(emp_list):
    l = []
    for i in emp_list:
        if i.salary() <30000 :
            l.append(i)
    return l


a=find_salary_under_30k(employ_list)

for i in a :
    print(f"{i.salary():.2f}, {i.name}")

