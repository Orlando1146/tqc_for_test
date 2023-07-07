# 設計說明：
# 請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。
# 提示：輸出浮點數到小數點後第二位。
# 輸入輸出：
# 輸入說明
#
# 讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）
# 輸出說明
#
# 輸出檔案中的內容
# 平均身高
# 平均體重
# 最高者
# 最重者
l=[]
na=[]
h=[]
w=[]
with open("read2.txt", "r",encoding="utf-8") as f:
     for s in f:
         print(s)
         l.append(s.split())
     n=len(l)

     for i in range(n):
         na.append([i][0])  #n=[l[i][0] for i in range(n)]
         h.append(eval(l[i][1])) #h=[eval(l[i][0]) for i in range(n)]
         w.append(eval(l[i][2]))
print(f"Average height: {sum(h)/n:.2f}")
print(f"Average weight: {sum(w)/n:.2f}")
print(f"The tallest is {na[h.index(max(h))]} with {max(h):.2f}cm")
print(f"The heaviest is {na[w.index(max(w))]} with {max(w):.2f}kg")
