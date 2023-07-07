# 請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值。
# 方法１
n=[]
for temp in range(10):
    n2=eval(input())
    n.append(n2)
print(min(n))
# 方法２
n=eval(input())
for temp in range(9):
    n2=eval(input())
    if n2< n:
        n=n2
print(n)