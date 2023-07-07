# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳
# a
# b
#  的值。
class PYD5:
    def __init__(self, tester_name):
        self.tester = tester_name

    def power(self, a, b):
        return a**b

    def multiple(self, x, y):
        return x * y

    def is_prime(self, x):
        ans = True
        if x < 2:
            ans = False
        for i in range(2, x - 1):
            if x % i == 0:
                ans = False
                break
            else:
                ans = True
        return ans

    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def quadratic_equation(self, a, b, c):
        if (b ** 2) - (4 * a * c) >= 0:  # b平方-4 * a * c 先判斷是不是有解
            ans1 = (-b + (b ** 2 - 4 * (a * c)) ** 0.5) / (2 * a)
            ans2 = (-b - (b ** 2 - 4 * (a * c)) ** 0.5) / (2 * a)
            return ans1, ans2
        else:
            return 0

    def compute(self,A,B,C):
        return (A,B,C)

    def sum(self,a, b):
        sum = 0
        for i in range(a, b + 1):
            sum += i
        return sum  # 跑到return迴圈就結束 所以不能放在 for in裏面



