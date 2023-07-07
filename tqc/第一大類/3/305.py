# 設計說明：
# 請撰寫一程式，讓使用者輸入一個正整數，將此數值以反轉的順序輸出。
# n=input() #代表輸入的是文字
# print(n[2::-1])

n=eval(input())
while n >0 :
    print(n%10,end="")
    n=n//10 #整數除法
