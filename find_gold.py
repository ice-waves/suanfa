"""
小地按照地图去寻宝，地图上被划分成 m行和n列的方格，横外坐标范国分别是 [0,n-1]和[0,m-1]。
在横坐标和外坐标的数位之和不大于k的方格中存在黄金（每个方格中仅存在一克黄全），
但横坐行和外坐标之和大于*的方格存在危险不可进入。
小华以入口(0.0)进入，任何时候只能向左，右，上，下四个方向移动一格。
请问小华最多能获得多少克黄金？

坐标取值范里如下：
0<=m<=50
O<=n<=50
k的取值范围如下：
0<=k<=100
输入中包含3个字数，分别是m，n, K
"""

def findGold(m: int, n: int, k: int) -> int:
    goldWeight = 0
    for x in range(m):
        xAdd = sum([int(digit) for digit in str(x)])
        for y in range(n):
            yAdd = sum([int(digit) for digit in str(y)])
            if xAdd + yAdd <= k:
                goldWeight += 1
    return goldWeight
    
if __name__ == '__main__':
  findGold(4, 5, 7)