# 請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。
# 輸入輸出：
# 輸入說明
#
# 兩個2*2矩陣，皆輸入整數
# 輸出說明
#
# 矩陣1的內容
# 矩陣2的內容
# 矩陣1及矩陣2相加的結果
l=[[[],[]],[[],[]]]
for i in range(2):
    print(f"Enter matrix {i+1}:")
    for k in range(2):
        for j in range(2):
            print(f"[{k+1}, {j+1}]:"  ,end=" ")
            l[i][j].append(eval(input()))

for i in range(2):
    print(f"Matrix {i+1}:")
    for j in range(2):
        for k in range(2):
            print(l[i][j][k] ,end=" ")
        print()
print(f"Sum of 2 matrices:")

for i in range(2):
    for j in range(2):
        print(f"{l[0][i][j]+l[1][i][j]}",end=" ")
    print()