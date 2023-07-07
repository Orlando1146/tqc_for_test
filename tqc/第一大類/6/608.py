# 設計說明：
# 請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
# 輸入輸出：
# 輸入說明
# 九個整數
# 輸出說明
# 矩陣最大值及其索引
# 矩陣最小值及其索引
n1=s1=n2=s2=0
max=-9999999999
min=99999999999
for n in range(3):
    for s in range(3):
        num=eval(input())
        if num > max:
            max=num ;n1=n ;s1=s #要用;不是用,
        if num < min:
            min = num; n2=n ; s2=s
print(f"Index of the largest number {max} is: ({n1}, {s1})")
print(f"Index of the smallest number {min} is: ({n2}, {s2})")

# l=[]
# for i in range(9):
#     n=eval(input())
#     l.append(n)
# print(f"Index of the largest number {max(l)} is: ({l.index(max(l))//3}, {l.index(max(l))%3})")
# print(f"Index of the largest number {max(l)} is: ({l.index(min(l))//3}, {l.index(min(l))%3})")
