# 506 一元二次方程式
# 說明:
# 請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式 ax2+bx+c=0的三個係數a、b、c）
# 作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has noroot.】
#
# 輸出有順序性
def compute(a, b, c):
    if (b ** 2) - (4 * a * c) >= 0: #b平方-4 * a * c 先判斷是不是有解
        ans1 = (-b+(b**2-4*(a*c))**0.5)/(2*a)
        ans2 = (-b-(b**2-4*(a*c))**0.5)/(2*a)
        return ans1, ans2
    else:
        return 0
a1=eval(input())
b1=eval(input())
c1=eval(input())
if compute(a1,b1,c1)!= 0:
    x,y=compute(a1,b1,c1)
    print(f"{x}, {y}")

else:
    print("Your equation has noroot.")
