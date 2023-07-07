# 請撰寫一程式，讓使用者輸入一個整數x，並將x傳遞給名為compute()的函式，此函式將回傳x是否為質數（Prime number）的布林值，接著再將判斷結果輸出。
# 如輸入值為質數顯示【Prime】，否則顯示【Not Prime】。
# 只有1跟自己本身可以整除為質數 1不是質數
def compute(x):
    ans=True
    if x < 2:
        ans = False
    for i in range(2,x-1):
        if x%i==0:
            ans = False
            break
        else:
            ans= True
    return ans
a=eval(input())
if compute(a):
    print("Prime")
else:
    print("Not Prime")
# def compute(x):
#     if x <= 1:
#         return 'Not Prime'
#     for i in range(2, x):
#         if x % i == 0:
#             return 'Not Prime'
#         else:
#             return 'Prime'
#
#
# x = eval(input())
# print(compute(x))