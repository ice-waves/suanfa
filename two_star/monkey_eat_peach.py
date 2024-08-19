"""
孙悟空爱吃媱桃，有一天趁着蟠桃园守 卫不在来偷吃。已知蜢桃园有N颗桃树，每颗树上都有桃子，守卫将在H小时后回来。
孙悟空可以決定他吃蟠桃的速度K（个/小时），每个小时选一颗桃树，并以树上吃掉K个，如果树上的桃子少于K个，则全部吃掉，并且这一小时剩余的时间里不再吃桃。
孙悟空喜欢慢慢吃，但又想在守卫回来前吃完桃子。
请返回孙悟空可以在H小时内吃掉所有桃子的最小速度K（K为整数）。如果以任何速度都吃不完所有桃子，则返回0。
"""

"""
思路：二分查找
"""

def canEatAllPeaches(peaches, H):
    if len(peaches) > H:
        return 0
    
    def canEat(k):
        hours = 0
        for peach in peaches:
            hours += peach // k + (peach % k > 0)  # 进一取整数
            if hours > H:
                return False
        return True
    
    left, right = 1, max(peaches)
    
    while left < right:
        mid = left + (right - left) // 2
        if canEat(mid):
            right = mid
        else:
            left = mid + 1
    
    if canEat(left):
        return left

    return 0
    