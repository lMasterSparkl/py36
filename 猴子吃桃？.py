'''猴子吃桃问题 每天吃一半加一个第五天只剩下一个求第一天摘了个多少桃子'''
n=1
for i in range(5,0,-1):
    n=(n+1)<<1 #<<1什么意思？
print(n)
