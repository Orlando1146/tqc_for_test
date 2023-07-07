# 設計說明：
# 請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。
# 輸入輸出：
# 輸入說明
# 讀取read.txt的內容（內容為數字，以空白分隔）
# 輸出說明
# 總和
with open("read.txt", "r", encoding="utf-8") as f:
#     sum = 0
#     line = f.readline()
#     nums = line.split()
#     for n in range(len(nums)):
#         sum += int(nums[n])
# print(sum)
    num=f.read()
    l=[int(i) for i in num.split()]
    print(sum(l))



