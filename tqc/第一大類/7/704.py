# 設計說明：
# 請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），
# 最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。
# 輸入輸出：
# 輸入說明
#
# 輸入n個整數至集合，直至-9999結束輸入
# 輸出說明
#
# 集合的長度
# 集合中的最大值
# 集合中的最小值
# 集合內的整數總和
s=set()
while True:
    n=eval(input())
    if n==-9999:
        break
    s.add(n)
print(f"Length: {len(s)}")
print(f"Max: {max(s)}")
print(f"Min: {min(s)}")
print(f"Sum: {sum(s)}")