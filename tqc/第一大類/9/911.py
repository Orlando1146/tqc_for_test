# with open("906.txt","r+",encoding="utf-8") as f:
#     print("=== Before the replacement")
#     s1=input()
#     s2=input()
#     a=f.read()
#     print(a)
#     a=a.replace(s1,s2)
#     f.seek(0)
#     print("=== After the replacement")
#     print(a)


# l = []
# name = []
# h = []
# w = []
# with open("read.txt","r",encoding="utf-8") as f:
#
#     for i in f:
#         print(i)
#         l.append(i.split())
#     n=len(l)
#
#     for i in range(n):
#         name.append(l[i][0])
#         h.append(eval(l[i][1]))
#         w.append(eval(l[i][2]))
#     print(f"Average heifht: {sum(h)/n:.2f}")
#     print(f"The tallest is {name[h.index(max(h))]}")


# with open("read.txt","a+",encoding="utf-8") as f :
#     for i in range(5):
#         f.write("\n"+input())
#     f.seek(0)
#     a=f.read()
#     print(a)

with open("902.txt","r",encoding="utf-8") as f:
    l=[]
    for i in f.read().split():
        l.append(eval(i))
    print(sum(l))