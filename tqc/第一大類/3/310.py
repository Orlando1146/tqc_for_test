n=eval(input())
sum=0
for a in range(2,n+1):
    sum+= 1/((a-1)**0.5+a**0.5)
print(f"{sum:.4f}")
