num=[1,5,16,18,15]
# lst=[n+1 if n>15 else n-1for n in num ]
# print(lst)

for n in num:
    if n>15:
        n=n+1
    elif n<15:
        n=n-1
print(num)