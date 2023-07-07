# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。
# 提示：假設樣本中只有一個眾數。
# 輸入輸出：
# 輸入說明
# 十個整數
# 輸出說明
# 眾數
# 眾數出現的次數
L=[]
sum=0
num=0
for i in range(10):
  L.append(eval(input()))
for j in range(10):
  if L.count(L[j])>sum:
    sum=L.count(L[j])
    num=L[j]
print(num)
print(sum)
