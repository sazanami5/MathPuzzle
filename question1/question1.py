# Q1
# 10進数、２進数、８進数のいずれで表現しても回文数となる数のうち、10進数の10以上で最小の値を求めてください


#文字列を逆順にする
def reverseString(string):
    reversedString = ''.join(list(reversed(str(string))))
    return reversedString

#2進数は偶数だと一桁目が0になるため、奇数のみサーチ
i =11
while True :
    if (str(i) == reverseString(i) and str(bin(i)[2:]) == reverseString(bin(i)[2:]) and str(oct(i)[2:]) == reverseString(oct(i)[2:])):
        print(i)
        break
    i += 2