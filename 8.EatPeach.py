#EatPeach
#猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，
#还不过瘾，又多吃了一个；第二天早上又吃了剩下的一半，又
#多吃了一个。以后每天早上都吃前一天剩下的一半加一个。到
#第5天早上想吃时，只剩下一个桃子了，请问第一天摘了几个？

n = 1
for i in range(5,0,-1):
    n = (n+1)<<1
print(n)
