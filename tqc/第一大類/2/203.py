# 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。
# 輸入輸出：
# 輸入說明
#
# 一個正整數
# 輸出說明
#
# 判斷是否為閏年或平年
y=eval(input())
if (((y%4==0)and(y%100!=0)) or (y%400==0)):
    print(f"{y}is a leap year")
else:
    print(f"{y} is not a leap year")