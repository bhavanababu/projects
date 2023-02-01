num=123
res=0
while(num!=0):
    ld=num%10
    res=(res*10)+ld
    num=num//10
print(res)