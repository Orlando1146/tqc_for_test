# 請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。
# 3. 輸入輸出：
# 輸入說明
# 一個正整數
# 輸出說明
# 以 * 畫出等腰三角形
# （每列最後一個 * 的右方無空白）

#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************
n=eval(input())
for r in range(1,n+1):
    for spa in range(n-r):
        print(" ",end="")
    for star in range(r*2-1):
        print("*",end="")
    print()

# n=eval(input())
# sum=1
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end="")
#     for y in range(sum):
#         print("*",end="")
#     sum+=2
#     print()

