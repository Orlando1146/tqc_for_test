# 請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
# 將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。
# 輸入輸出：
# 輸入說明
# 輸入兩個詞典，直至end結束輸入
# 輸出說明
# 合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值
d1={}
d2={}
print(f"Create dict1")
while True:
    k=input("Key: ")
    if k == "end":
        break
    v=input("Value: ")
    d1[k]=v

print(f"Create dict2")
while True:
    k=input("Key: ")
    if k == "end":
        break
    v=input("Value: ")
    d2[k]=v

d1.update(d2)  #D1會變成兩個合併後的字典
d3=sorted(d1)
for i in d3:    #要迭代的是list
    print(f"{i}: {d1[i]}")

