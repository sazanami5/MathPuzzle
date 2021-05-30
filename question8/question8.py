'''
前後左右のみ動くことのできる掃除ロボット
同じ場所を掃除しないように動く時、12回移動する移動経路は何パターンあるか
線対称、点対称のパターンは別のものとしてカウントする。
'''

N = 12

def move(moveLog: list)->int:
    #最初の位置を含んでN+1個調べれば終了
    if len(moveLog) == N + 1:
        return 1
        
    cnt = 0
    #前後左右に移動
    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nextPos =[ moveLog[-1][0] + d[0] ,moveLog[-1][1] + d[1]]
        #探索済みでなければ移動させる
        if  not(nextPos in moveLog):
            cnt = cnt+ move(moveLog + [nextPos])
            
    return cnt

print(move([[0, 0]]))
