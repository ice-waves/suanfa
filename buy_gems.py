from typing import List
"""
橱窗里有一排宝石，不同的宝石对应不同的价格，宝石的价格标记为gems[i],O<=i<n,n=gems.length
主石可同时出售0个或多个，如果同时出售多个，则要求出售的宝石编号连续；

例如容户最大购买宝石个数为m，购买的宝石编号必须为
gems[i],gems[i+1], gems[i+m-1](0<=i<n, m<=n)
假设你当前拥有总面值为value的钱，请问最多能购买到多少个宝石,如无法购买宝石，则返回0.
"""

def buyGems(num: int, gemsPrice: List[int], money: int) -> int:
    buyNum = []
    if num == 0:
        return 0
    
    for i in range(num):
        totalPrice = 0
        index = 0
        for j in range(i, num):
            totalPrice += gemsPrice[j]      
            if totalPrice > money:
                break
            index += 1
        
        buyNum.append(index)
        
    return max(buyNum)
            
            
if __name__ == '__main__':
    buyGems(5, [],2)