# 請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值
n=[]
while True:#無限迴圈
    temp = eval(input())
    if temp == 9999:
        break
    n.append(temp)
print(min(n))