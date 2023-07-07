# 請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。
# 請依序分行顯示(1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。
# 提示：科目須參考範例輸出樣本，依字母由小至大進行排序。
# 輸入輸出：
# 輸入說明
# 輸入X組和Y組各自的科目至集合，直至end結束輸入
# 輸出說明
# X組和Y組的所有科目
# X組和Y組的共同科目
# Y組有但X組沒有的科目
# X組和Y組彼此沒有的科目（不包含相同科目）
x=set()
y=set()
print("Enter group X's subjects:")
while True:
    s=input()
    if s == "end":
        break
    x.add(s)
print("Enter group Y's subjects:")
while True:
    s2=input()
    if s2 == "end":
        break
    y.add(s2)

print(sorted(x|y))
print(sorted(x&y))
print(sorted(y-x))
print(sorted(x^y))
