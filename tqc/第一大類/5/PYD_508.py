# 請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。
# 輸入輸出：
# 輸入說明
# 兩個正整數（以半形逗號分隔）
# x,y
# 輸出說明
# 最大公因數
def compute(x,y):
    if y==0:
        return x
    else:
        return compute(y,x%y)

x,y=eval(input())
print(compute(x,y))

# def compute(x,y):
#     n=0
#     if x<y:
#         for i in range(1,x+1):
#             if x%i==0 and y%i==0 :
#                 n=i
#     if y<x:
#         for i in range(1,y+1):
#             if y%i==0 and y%i==0 :
#                 n=i
#     print(n)
# x,y=eval(input())
#
# compute(x,y)
