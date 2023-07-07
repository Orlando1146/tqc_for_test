# 請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義（State）。
# 假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
# BMI值	代表意義
# BMI < 18.5	under weight
# 18.5 <= BMI < 25	normal
# 25.0 <= BMI < 30	over weight
# 30 <= BMI	fat
# 提示： BMI=體重(kg/身高**2(m）
#  ，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。
while True:
    k=eval(input())
    if k == -9999:
        break
    h=eval(input())
    BMI=k/(h/100)**2

    if BMI <18.5:
        print(f"BMI: {BMI:.2f} \nState: under weight")

    if 18.5 <= BMI < 25:
        print(f"BMI: {BMI:.2f} \nState: normal")

    if 25.0 <= BMI < 30	:
        primt(f"BMI: {BMI:.2f} \nState: over weight")

    if 30 <= BMI	:
        print(f"BMI: {BMI:.2f} \nState: fat")

