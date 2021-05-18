

#再帰での書き方がわかりません助けてください
# Question
# N円札を[coin,..]で両替する時何通りあるか。コインの合計の枚数の最大値はN
import math

def getMaxCoin(coinPrice:int,changePrice:int, maxCoinsSum:int):
    maxCoin =  math.floor(changePrice/coinPrice) if math.floor(changePrice/coinPrice)<=maxCoinsSum else maxCoinsSum
    return maxCoin


count = 0
times = 0
def exchangePatternCount(exchangeMoney, coins:list, maxCoinsSum:int):
    maxCoins = [getMaxCoin(coin,exchangeMoney,maxCoinsSum) for coin in coins]
    coin = coins.pop(0)
    times+=1
    if len(coins)==0:
        count +=1 
        return count
    else:
        for i in range(maxCoins[times]+1):
            times+=1
            exchangePatternCount(exchangeMoney-coin*i,coins,maxCoinsSum)


exchangePatternCount(1000, [500,100,50,10], 15)
