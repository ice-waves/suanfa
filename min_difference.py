from typing import List

def minDifference(scores: List[int]) -> float:
    n = len(scores)
    # 最小话差值
    minDiff = float('inf')

    # 递归函数，用于尝试所有可能的分组  
    def backTrack(index: int, team1_sum: float, team2_sum: float):
        nonlocal minDiff
        # 所有参与者都已分配
        if index == n:
            # 计算当前分配下的实力差绝对值  
            currentDiff = abs(team1_sum - team2_sum)
            minDiff = min(currentDiff, minDiff)
            return

        # 尝试将当前参与者加入第一队
        backTrack(index + 1, team1_sum + scores[index], team2_sum)
        # 尝试将当前参与者加入第二队
        backTrack(index + 1, team1_sum, team2_sum + scores[index])

    
    backTrack(0, 0, 0)
    
    return minDiff


