# 104 圓形面積計算
# 說明:
# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
#
# 需import math模組，並使用math.pi。
#
# 輸出浮點數到小數點後第二位。
import math
r=float(input())
Radius=r
Perimeter=2*math.pi*r
Area=r*r*math.pi
print(f"Radius={Radius:.2f}\nPerimeter={Perimeter:.2f} \n7Area={Area:.2f}")
# print("Radius=""{:.2f}".format(Radius))

