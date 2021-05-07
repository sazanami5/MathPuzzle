import math
# print("長さを入力")
#length= int(input())
# print("人数を入力")
#people= int(input())
length= 100
people= 2

times=0
cutTimes=length-1

while (True):
    if people<= 1*2**times:
        break
    cutTimes -= 1*2**times
    times+=1
print("回数は：{}回" .format(times+math.ceil(cutTimes/people)))


# level=1
# while(True):
#     if 1*2**(level-1)<=people:#人数の方が多い
#         cutTimes -= 1*2**(level-1)
#         times += 1
#     elif 1*2**(level-1)>people:#人数の方が少ない
#         cutTimes -= 1*2**(level-1)
#         times += math.ceil(1*2**(level-1)/people)
#     if cutTimes<=0:
#         print(times)
#         break
#     level+=1

