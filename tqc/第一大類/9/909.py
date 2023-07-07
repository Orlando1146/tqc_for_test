# 設計說明：
# 請撰寫一程式，將使用者輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。再將檔案加以讀取並顯示檔案內容。
# 輸入輸出：
# 輸入說明
#
# 五個人的姓名和電話號碼，以空白分隔
# 輸出說明
#
# 讀取及寫入檔案後，再輸出讀入的檔案名稱及內容
with open("data.tat", "w+", encoding="utf-8") as f:
    for i in range(5):
        f.write(input()+"\n")
    f.seek(0)
    print('The content of "data.dat":')
    for i in  f:
        print(i)