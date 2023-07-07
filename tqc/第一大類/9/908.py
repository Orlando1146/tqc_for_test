# 請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。
# 輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）
# 輸入輸出：
# 輸入說明
#
# 讀取read.txt的內容，以及檔案中某單字出現的次數
# 輸出說明
#
# 輸出符合次數的單字，並依單字的第一個字母大小排序
filename = input()
n = eval(input())
d = {}
with open(filename, "r") as f:     #要記得檔案位置是自己輸入的時候不要加“”
    for line in f:
        for w in line.split():
            if w in d:
                d[w] += 1
            else:
                d[w]  = 1
    w = sorted(d)
    for word in w:
        if d[word] == n:
            print(word)
