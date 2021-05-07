
import datetime
now=datetime.datetime.now()
op = ["+","/","-","*",""]

for num in range(1000,10000):
    numString=str(num)
    for x in op:
        for y in op:
            for z in op:
                string = str(numString[3]) + str(x)+ str(numString[2])+ str(y)+ str(numString[1])+ str(z)+ str(numString[0])
                if len(string) < 5:
                    continue
                try:
                    if num == eval(string):
                        print(num)
                except Exception:
                    continue
now=datetime.datetime.now()-now
print("検索時間："+str(now.seconds)+"."+str(now.microseconds)+"秒")


