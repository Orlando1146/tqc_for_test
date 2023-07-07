# 設計說明：
# 請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。
# 輸入輸出：
# 輸入說明
# 一個字串（格式為ddd-dd-dddd，d表示數字）
# 輸出說明
# 判斷是否符合SSN格式
s=input().split("-")
for i in range(len(s)):
    if s[i].isdigit()==False:
        print("Invalid SSN")
        break
else:
    print("Valid SSN")