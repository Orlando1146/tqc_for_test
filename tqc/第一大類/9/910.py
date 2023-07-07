# 請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，
# 第二列之後是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。
# 輸入輸出：
# 輸入說明
# 讀取read.dat
# 輸出說明
# 讀取檔案內容，並格式化輸出男生人數和女生人數
l=[]
with open("read910.dat","r",encoding="utf-8") as f:
    for i in f:
        # for w in i.split():
        l.append(i.split()[2])
        print(i)
    f.seek(0)

    print(f"Number of males: {l.count('0')}")
    print(f"Number of females: {l.count('1')}")
    # print(l)
