from typing import List, Tuple

"""
下图中，每个方块代表一个像表，每个像表用其行号和列号表示。
为简化处理，多段线的走向只能是水平、竖直、斜向45度。
上图中的多段线可以用下面的坐标串表示：(2,8), (3.7),(3,6), (3,5). (4,4), (5, 3). (6,2), (7, 3), (8,4). (7,5)
但可以发现，这种表示不是最简的，其实只需要存储6个蓝色的关键点即可，它们是线段的起点、拐点、终点，而剩下4个点是元余的。
现在，请根据输入的包含有元余数据的多段线坐标列表，输出其最简化的结果。

2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5
1、所有数字以空格分隔，每两个数字一组，第一个数字是行号，第二个数字是列号;
2、行号和列号范围为[0,64)，用例输入保证不会越界，考生不必检查；
3、输入数据至少包含两个坐标点。
"""

def dataCompression(points: List[int]) -> List[int]:
    pointsList = list(zip(*[iter(points)] * 2))
    result = simplifyPolyline(pointsList)
    mergeResult = [item for tup in result for item in tup]
    return mergeResult
    
def isRedundant(p1, p2, p3: Tuple[int]) -> bool:
    if p1[0] == p2[0] == p3[0]:
        return True

    if p1[1] == p2[1] == p3[1]:
        return True
    
    if (p2[0] - p1[0] == p3[0] - p2[0]) and (p2[1] - p1[1] == p3[1] - p2[1]):
        return True
    return False

def simplifyPolyline(points):
    if len(points) < 3:
        return points
    simplified = [points[0]]
    for i in range(1, len(points)-1):
        if not isRedundant(points[i-1], points[i], points[i+1]):
            simplified.append(points[i])
    
    simplified.append(points[-1])
    return simplified

if __name__ == '__main__':
    result = dataCompression([2, 8, 3, 7,3, 6, 3, 5, 4, 4, 5, 3, 6, 2, 7, 3, 8, 4, 7, 5])
    print(result)