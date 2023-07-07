# 10 費氏數列
# 說明:
# 請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，
# 並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
# 費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
x=eval(input())
for i in range(x):
    print(fib(i),end=" ")



