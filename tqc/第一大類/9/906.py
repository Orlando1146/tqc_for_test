# 設計說明：
# 請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。
# 輸入輸出：
# 輸入說明
#
# 輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）
# 輸出說明
#
# 輸出檔案中的內容
# 輸出取代指定字串後的檔案內容
fn=input()
s1=input()
s2=input()
with open(fn, "r+", encoding="utf-8") as f:
    st=f.read()
    print("=== Before the replacement")
    print(st)
    print("=== After the replacement")
    st=st.replace(s1,s2)
    print(st)
    f.seek(0)
    f.write(st)