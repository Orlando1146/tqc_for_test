 # 請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，印出其所對應的GPA。
# 假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
# 分　數	GPA
# 90 ~ 100	A
# 80 ~ 89	B
# 70 ~ 79	C
# 60 ~ 69	D
# 0 ~ 59	E
while True:
    while True:
        n = eval(input())
        if n == 9999:
            break
        elif n >=90:
            print("A")

        elif n >= 80:
            print("b")

        elif n >= 70:
            print("c")

        elif n >= 60:
            print("d")

        elif n <= 59:
            print("e")

