# 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），然後以三角形的方式依序輸出此數的相乘結果。
# 提示：輸出欄寬為4，且需靠右對齊

tri = eval(input())
for temp in range(1, tri+1):
    for ans in range(1, temp+1):
        # fin = temp*ans
        print(f"{temp*ans:>4}", end="")
    print()
