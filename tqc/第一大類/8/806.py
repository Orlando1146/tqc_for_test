# 請撰寫一程式，讓使用者輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，
# 此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。
# 輸入輸出：
# 輸入說明
# 一個字串和一個字元
# 輸出說明
# 字串中指定字元出現的次數
s=input()
c=input()

def compute(a,b):
    return s.count(c)
print(f"{c} occurs {compute(s,c)} time(s)")