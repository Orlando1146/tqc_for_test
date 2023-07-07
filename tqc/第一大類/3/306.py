# 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。
n=eval(input())
i=1
for tem in range(1, n+1):
    i*=tem
print(i)