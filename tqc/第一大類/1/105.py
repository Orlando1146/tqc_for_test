# 105 矩形面積計算
# 說明:
# 請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。
# 輸出浮點數到小數點後第二位。
# 輸入
h=float(input())
w=float(input())
Perimeter=2*w + 2*h
Area=h * w
print(f"Height = {h}")
print(f"Width = {w}")
print(f"Perimeter = {Perimeter:.2f}")
print(f"Area ＝ {Area:.2f}")
