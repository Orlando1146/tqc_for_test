# 設計說明：
# 請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
# 提示1：平均溫度輸出到小數點後第二位。
# 提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。
# 輸入輸出：
# 輸入說明
# 四週各三天的溫度
# 輸出說明
# 平均溫度
# 最高溫度
# 最低溫度
l=[]
for i in range(1,5):
    print(f"Week {i}")
    for j in range(1,4):
        print(f"Day {j}:",end="")
        # n=eval(input())
        # l.append(n)
        l.append(eval(input()))
# print(f"Average: {sum(l)/len(l):.2f}")
print(f"Average: {sum(l)/12:.2f}")
print(f"Highest: {max(l)}")
print(f"Lowest: {min(l)}")



