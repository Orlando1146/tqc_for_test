price=eval(input())
if price >= 38000:
    print(price*0.7)
elif price >= 28000:
    print(price * 0.8)
elif price >= 18000:
    print(price * 0.9)
else :
    print(price * 0.95)