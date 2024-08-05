from typing import List
"""
在一个大型体育场内举办了一场大型活动，由于疫情防控的需要，要术每位观众的必项同陽至少一个空位才允许落座。
现在给出一排观众座位分布图，座位中存在已落座的观众，请计算出，在不移动现有观众座位的情况下，最安还能坐下多少名观众。
输入描达：
一个数组，用来标识共一排座位中，每个座位是否己经坐人。口表示该座位没有坐人，1表示该座位已经坐人。
输出描述：
墊效，在不移动现有观众座位的情況下，環交还能生下交少名观众。
"""

def seatNum(seatTag: List) -> int:
    seatTagLen = len(seatTag)
    
    # 边界值
    if seatTagLen == 0:
      return 0
    elif seatTagLen == 1:
        if seatTag[0] == 0:
          return 1
        else:
            return 0
    
    seatTagNew = seatTag.copy()
    
    for i in range(seatTagLen):
        if i == 0:
            if seatTagNew[i] == 0:
                if seatTagNew[i+1] == 1:
                    continue
                else:
                    seatTagNew[i] = 1
        else:
            if seatTagNew[i-1] == 1:
               continue
            else:
                if i+1 <= seatTagLen-1:
                    if seatTagNew[i+1] == 1:
                        continue
                    else:
                        seatTagNew[i] = 1
                else:
                    seatTagNew[i] = 1
    avaiableNum = 0
    
    for x in range(seatTagLen):
        if seatTag[x] != seatTagNew[x]:
            avaiableNum += 1
    
    return avaiableNum