# 設計說明：
# 請撰寫一程式，要求使用者輸入五個人的名字並加入到read.txt的尾端。之後再顯示此檔案的內容。
# 輸入輸出：
# 輸入說明
# 輸入五個人的名字
# 輸出說明
# 讀取及寫入檔案後，輸出此檔案內容
with open("read.txt", "a+", encoding="utf-8") as f:
    for i in range(5):
        f.write("\n"+input())   #注意記得＋
    print("Append completed")
    print("Content of \"read.txt\": ")
    f.seek(0)
    print(f.read())