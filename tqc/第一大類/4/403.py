# 請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。
# 輸入輸出：
# 輸入說明
#
# 兩個正整數a、b（a<=b）
# 輸出說明
#
# 格式化輸出兩個正整數之間4或9之倍數（包含a和b）
# 倍數個數
# 倍數總合
n1=eval(input())
n2=eval(input())
sum=0
con=0
for tem in range(n1,n2+1):
    if tem%4==0 or  tem%9==0:
        sum+=tem
        con+=1
        print(f"{tem:<4}",end="")
        if con%10==0:
            print()
print()
print(con)
print(sum)
