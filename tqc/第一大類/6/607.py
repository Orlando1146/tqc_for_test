# 設計說明：
# 請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# 提示：平均分數輸出到小數點後第二位。
# 輸入輸出：
# 輸入說明
#
# 三位學生各五筆成績
# 輸出說明
#
# 格式化輸出每位學生的總分及平均分數

l=[[],[],[]]
ord=["1st","2nd","3rd"]
for j in range(3):
    print(f"The {ord[j]} student:")
    for i in range(5):
        n=eval(input())
        l[j].append(n)
for i in range(3):
    print(f"Student {i+1}\n#Sum {sum(l[i])}\n#Average {sum(l[i])/5:.2f}")
