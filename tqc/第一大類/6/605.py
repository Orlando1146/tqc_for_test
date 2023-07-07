# 設計說明：
# 請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。
# 提示：平均值輸出到小數點後第二位。
# 輸入輸出：
# 輸入說明
# 十個數字
# 輸出說明
# 總和
# 平均
# l=[]
# for i in range(10):
#     l.append(eval(input()))
#     sum+=l[i]
# a=max(l)
# b=min(l)
# sum=sum-a-b
# print(sum)
# print(f"{sum/8:.2f}")

# 方法二
l=[]
for i in range(10):
    l.append(eval(input()))
l.sort()
ans=sum(l)-l[0]-l[9]
print(f"{ans}\n{ans/8:.2f}" )