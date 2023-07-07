# 509 最簡分數
# 說明:
# 請撰寫一程式，讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數的和為p/q，
# 接著將p和q傳遞給名為compute()函式，此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）。再將p和q各除以其最大公因數，
# 最後輸出的結果必須以最簡分數表示。
def compute(x,y):
    if y==0:
        return x
    else:
        return compute(y,x%y)
x,y=eval(input())
m,n=eval(input())
p=(x*n)+(y*m)
q=(y*n)
a=compute(p,q)

print(f"{x}/{y} + {m}/{n} = {int(p / a)}/{int(q / a)}")



