# 設計說明：
# 請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
# 　a. 必須至少八個字元。
# 　b. 只包含英文字母和數字。
# 　c. 至少要有一個大寫英文字母。
# 　d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。
# 輸入輸出：
# 輸入說明
#
# 一個字串
# 輸出說明
# 判斷是否符合密碼規則
s=input()
if len(s)<=7 or not s.isalnum() or s.islower() :
    print("InValid password")
else:
    print("Valid password")