# 請撰寫一程式，要求使用者輸入檔案名稱read.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。
# 輸入輸出：
# 輸入說明
#
# 輸入read.txt及一個字串
# 輸出說明
#
# 先輸出原檔案內容，再輸入刪除指定字串後的新檔案內容
filename = input()
s = input()
with open(filename, "r+", encoding="utf-8") as f:
    print("=== Before the deletion")
    s1 = f.read()
    print(s1)
    print("=== After the deletion")
    s1 = s1.replace(s, "")   #記得replace要＝
    print(s1)
    f.seek(0)
    f.write(s1)