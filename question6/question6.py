count = 0
for i in range(10001):
    Num = i*3 + 1
    while(True):
        if Num%2==0:
            Num = Num/2
        if Num==1:
            break
        if Num==i:
            count += 1
            break

        if Num%2 != 0:
            Num=Num*3+1
        if Num==1:
            break
        if Num==i:
            count += 1
            break

print(count)
