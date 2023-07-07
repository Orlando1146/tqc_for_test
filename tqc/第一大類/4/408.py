# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。
# 輸入輸出：
# 輸入說明
# 十個整數
# 輸出說明
# 偶數的個數
# 奇數的個數
n1=0
n2=0
for r in range(10):
    num=eval(input())
    if num %2==0 :
        n1+=1
    elif num%2!=0:
        n2+=1
print(f"Even Number : {n1}\nOdd Number : {n2}")
