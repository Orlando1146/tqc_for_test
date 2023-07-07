# 設計說明：
# 請撰寫一程式，依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。接著回答：
# set2是否為set1的子集合（subset）？set3是否為set1的超集合（superset）？
# 輸入輸出：
# 輸入說明
# 依序分別輸入五個、三個、九個整數
# 輸出說明
# 顯示回覆：
# set2是否為set1的子集合（subset）？
# set3是否為set1的超集合（superset）？
s1=set()
s2=set()
s3=set()
print("Input to set1:")
for i in range(5):
    s1.add(input())

print("Input to set2:")
for i in range(3):
    s2.add(input())

print("Input to set3:")
for i in range(9):
    s3.add(input())

print(f"set2 is subset of set1:{s2.issubset(s1)}")
print("set3 is superset of set1:",s3.issuperset(s1))