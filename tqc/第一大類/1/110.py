# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
# 提示1：建議使用import math模組的math.pow及math.tan
import math
n=eval(input())
s=eval(input())
Area=(n*s**2)/(4*math.tan(math.pi/n))
print(f"Area={Area:.4f}")
print("Area=%.4f" %Area)