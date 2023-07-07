# 設計說明：
# 請撰寫一程式，輸入一顏色詞典color_dict（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再根據key值的字母由小到大排序並輸出。
# 輸入輸出：
# 輸入說明
# 輸入一個詞典，直至end結束輸入
# 輸出說明
# 根據key值字母由小到大排序輸出
d={}
while True :
    k=input("Key: ")
    if k=="end":
        break
    v=input("Value: ")
    d[k]=v
s1=sorted(d)
for i in s1:
    print(f"{i}: {d[i]}")