# 設計說明：
# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
# 提示：J、Q、K以及A分別代表11、12、13以及1。
# 輸入輸出：
# 輸入說明
# 5張牌數
# 輸出說明
# 5張牌的數值總和
l=[]
for i in range(5):
    n = input()
    if n =="j":
        n=11
    if n=="Ｑ":
        n=12
    if n=="K":
        n=13
    if n=="A":
        n=1
    l.append(int(n))

print(sum(l))
