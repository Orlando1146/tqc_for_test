# 設計說明：
# 請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
# 再輸入一鍵值並檢視此鍵值是否存在於該詞典中。
# 輸入輸出：
# 輸入說明
#
# 先輸入一個詞典，直至end結束輸入，再輸入一個鍵值進行搜尋是否存在
# 輸出說明
#
# 鍵值是否存在詞典中
d={}
while True:
    k=input("Key: ")
    if k == "end":
        break
    v=input("Value: ")
    d[k]=v
sk=input("Search key: ")
print( sk in d)  #查找sk所代表的值 是否有在Ｓ字典裡(in 這用法但只會尋找key欄位 value不會去找)
