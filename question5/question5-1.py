import math

def getMaxCoin(coinPrice:int,changePrice:int, maxCoinsSum:int):
    maxCoin =  math.floor(changePrice/coinPrice) if math.floor(changePrice/coinPrice)>=maxCoinsSum else maxCoinsSum
    return maxCoin

def exchangePatternCount(exchangeMoney, coins:list, maxCoinsSum:int):
    maxCoins = [getMaxCoin(coin,exchangeMoney,maxCoinsSum) for coin in coins]
times=-1
count=0
sum = 0
def getCount(maxCoins,coins,exchangeMoney):
    if times==0:
        return count
    
    if times>0:

    


print(exchangePatternCount(1000,[10,50,100,500],15))

# def getCount(maxCoins,coins,exchangeMoney):
#     if times<len(maxCoins):
#         return count
#     for i in range(len(maxCoins)):
#         sum+=maxCoins[i]*coins[i]
        
#         if sum==exchangeMoney:
#             count+=1

