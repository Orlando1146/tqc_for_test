# 設計說明：
# 請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。
# 輸入輸出：
# 輸入說明
# 十個數字
# 輸出說明
# 由大到小排序，顯示最大的3個數字
l=[]
for i in range(10):
    l.append(eval(input()))
    # n=eval(input())
    # l.append(n)
    l.sort()
print(l[9], l[8], l[7])