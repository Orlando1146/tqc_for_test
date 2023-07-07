# 說明:
# 請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。
#
# 提示：輸出浮點數到小數點後第一位。
# 輸入
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
sum=a+b+c+d+e
Average=sum/5
print(a,b,c,d,e)
print(f"sum={sum:.2f}\nAverage={Average:.2f}")
