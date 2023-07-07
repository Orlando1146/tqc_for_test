# 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。
# 輸入輸出：
# 輸入說明
#
# 一個字串
# 輸出說明
#
# 依序輸出字串中每個字元對應的ASCII碼
# 每個字元ASCII碼的總和
s=input()
sum=0
for i in range(len(s)):
    print(f"ASCII code for '{s[i]}' is {ord(s[i])}")
    sum+=ord(s[i])
print(
    sum
)