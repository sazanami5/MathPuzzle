
count=0
for tenY in range(101):
    for fiftyY in range(21):
        for hyakuY in range(11):
            for gohyakuY in range(3):
                if tenY*10 + fiftyY*50  + hyakuY*100 + gohyakuY*500 ==1000 and tenY+fiftyY+hyakuY+gohyakuY<=15:
                    count += 1
                    #print("硬貨の枚数は10円：{} 50円：{} 100円：{} 500円：{}".format(tenY,fiftyY,hyakuY,gohyakuY))

print(str(count)+"通り")