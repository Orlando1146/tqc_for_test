# 請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。
# 輸入輸出：
# 輸入說明
#
# 兩個整數a、b，及一個算術運算子 (+、-、*、/、//、%）
a=eval(input())
b=eval(input())
op=input() #不能加eval
if op == "+" :
    print(a+b)
if op == "-" :
    print(a-b)
if op == "*" :
    print(a*b)
if op == "/" :
    print(a / b)
if op == "//" :
    print(a // b)
if op == "%" :
    print(a % b)
