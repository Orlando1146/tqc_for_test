# 1) 請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數n（n<10），顯示n*n乘法表。
# (2) 每項運算式需進行格式化排列整齊，每個運算子及運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。
n= eval(input())
for a in range(1,n+1):
   for b in range(1,n+1):
       print(f"{b:<2}* {a:<2}= {a*b:<4}",end="")
   print()
# n= eval(input())
# for a in range(1,n+1):
#    for b in range(1,n+1):
#        print(f"{b:<2}* {a:<2}= {a*b:<4}",end=" ")
#    print()