# 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開。請將此五個數字加總（Total）並計算平均（Average）。
# 輸入輸出：
# 輸入說
# 一個字串（五個數字，以空白隔開）
# 輸出說明
# 總合
# 平均 (輸出浮點數到小數點後第一位)
s=input()
b=s.split()
#s=input().split()
sum=0
for i in range(len(b)):
    sum+=int(b[i])   #文字記得轉數字才能計算
print(f"Total = {sum}")
print(f"Average = {sum/len(b):.1f}")
