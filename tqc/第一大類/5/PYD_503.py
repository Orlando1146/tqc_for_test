# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。

def compute(a,b):
    sum = 0
    for i in range(a,b+1):
        sum+=i
    return sum    #跑到return迴圈就結束 所以不能放在 for in裏面
a=eval(input())
b=eval(input())
print(compute(a,b))


