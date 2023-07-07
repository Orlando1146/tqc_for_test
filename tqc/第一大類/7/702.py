# 設計說明：
# 請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
# 輸入輸出：
# 輸入說明
#
# 兩個數組，直至-9999結束輸入
# 輸出說明
#
# 排序前的數組
# 排序後的串列
l=[]
for i in range(1,3):
    print(f"Creat tuple{i}")
    while True:
        n=eval(input())
        if n == -9999:
            break
        else:
            l.append(n)
t=tuple(l)
l.sort()
print(f"Combined tuple before sorting: {t}")
print(f"list after sorting: {l}")