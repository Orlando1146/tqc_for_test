# 設計說明：
# 請撰寫一程式，要求使用者輸入檔名read.txt，顯示該檔案的行數、單字數
# （簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。
# 輸入輸出：
# 輸入說明
#
# 讀取read.txt
# 輸出說明
#
# 行數
# 單字數
# 字元數（不含空白）
lines= words= chars =0
with open("read.txt", "r", encoding="utf-8") as file:
    for i in file:
        lines += 1
        words += len(i.split())
        chars += sum(len(i) for i in i.split())
    print(f"{lines} (s)\n{words} (s)")
    # print(f"{words} (s)")
    print(f"{chars} (s)")

    # lin = 0
    # wor = []
    # cha = []
    # for i in f:
    #     lin += 1
    #     for j in i.split():
    #         wor.append(j)
    #         for k in j:
    #             cha.append(k)
    # print(lin)
    # print(len(wor))
    # print(len(cha))
