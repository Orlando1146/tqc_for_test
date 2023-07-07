import employ
l=[]

from employ import Employ
from employ import Intern
while True:
    n1=input()
    if n1== "end":break
    n2=input()
    n3=input()
    n4=eval(input())
    member_employ=Employ(n1,n2,n3,n4)
    # a=member_employ.seniority()
    # b=member_employ.salary()
    # c=member_employ.e_id
    # d=member_employ.name
    # e=member_employ.enter_year
    # f=member_employ.starting_salary
    l.append(member_employ)
# print(member_employ.e_id,end=" ")
# print(member_employ.name,end=" ")
# print(member_employ.enter_year,end=" ")
# print(member_employ.starting_salary,end=" ")
# print(a,end=" " f"{b:.2f}")

# print(dicn)
while True:
    n1=input()
    if n1== "end":break
    n2=input()
    n3=input()
    n4=eval(input())
    n5=eval(input())
    member_employ=Intern(n1,n2,n3,n4,n5)
    # a=member_employ.seniority()
    # b=member_employ.salary()
    # c=member_employ.e_id
    # d=member_employ.name
    # e=member_employ.enter_year
    # f=member_employ.starting_salary
    # g=member_employ.duration
    l.append(member_employ)

# salary=0
# num=0
# for i in range(len(l)):
#     if l[i][3]>salary:
#         salary=l[i][3]
#         num=i
# sal=0
# all=[]
# for i in l:
#     # print(f"{i.name}'s salary is {i.salary()}")
#     if i.salary()>sal:
#         sal=i.salary()
#         all.append(i.e_id)
#         all.append(i.name)
#         all.append(i.enter_year)
#         all.append(i.salary())
# tmp = {"expensive": (l[0].name, l[0].salary())}
# for i in l:
#     if i.salary() > tmp["expensive"][1]:
#         tmp["expensive"] = (i.name, i.salary())
#
# print(f"The most expensive employ is {tmp['expensive'][0]}")
print(l)
