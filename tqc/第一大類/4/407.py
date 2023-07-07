# 1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則如下：
# 每四年一閏，每百年不閏，但每四百年也一閏。
# (2) 假設此不定數迴圈輸入-9999則會結束此迴圈。
# 輸入輸出：
# 輸入說明
# 一個正整數，直至-9999結束輸入
# 輸出說明
# 判斷是否為閏年或平年
while True:
    year=eval(input())
    if year== -9999:
        break
    if year%4 == 0 and year%100!=0 or year%400 == 0:
        print(f"{year} is a leap year")
    elif year%4!=0 or year%100==0:
        print(f"{year} is not a leap year")

