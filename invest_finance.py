from typing import List
"""
在一款處拟游戏中生活，你必须进行没资以增强在處拟游戏中的资产以免被淘汰出局。
现有一家Bank，已提供有若千理财产品m，风险及投资回报不同，你有N（元）进行投资，脂接受的总风险值为×。
你要在可接受范里内选择最优的投资方式获得最大回报。
说明：
在应拟游戏中，每项投资风险值相加为总风,险值；
在處拟游戏中，最多只能投资2个理财产品；
在虚拟游戏中，最小单位为整数，不能拆分为小数；
投资额*回报率=投资回报

输入描述
第一行：产品数(取值范围(1,201)，总投资额(整数，取值范围(1.10000))，可接受的总风,险(整数，取自范国(1.200))
第二行：产品投资回报率序列，输入为整效，取住范国11.60]
第三行：产品风险伯产列，输入为整数，取伯范国(1.100]
第四行：最大投资额度序列，输入为盛效，取白范国(1.10000]
"""

def investFinance(
    productsNum: int, 
    totalInvestmentAmount: int,
    totalRisk: int,
    productsRate: List[int],
    productsRisk: List[int],
    productsMaxInvest: List[int],
) -> List[int]:
    if productsNum == 0:
        return []
    elif productsNum == 1:
        if productsRisk[0] > totalRisk:
            return []
        else:
            return productsMaxInvest
    
    tempTotalRisk = 0
    totalReturnInvestment = 0  
    productsInvestResult = [0 for _ in range(productsNum)] 
    
    productsInvestMap = {}
     
    for i in range(productsNum):
        # 只取一个产品
        tempTotalRisk = productsRisk[i]
        if tempTotalRisk > totalRisk:
          continue
        
        totalReturnInvestment = productsRate[i]*productsMaxInvest[i]
        productsInvestResult[i] = productsMaxInvest[i]
        productsInvestMap[totalReturnInvestment] = productsInvestResult.copy()
        productsInvestResult = [0 for _ in range(productsNum)]
        for j in range(i+1, productsNum):
            # 选取两个产品
            tempTotalRisk = productsRisk[i] + productsRisk[j]
            if tempTotalRisk > totalRisk:
                continue
            
            totalReturnInvestment = productsRate[i]*productsMaxInvest[i] + productsRate[j]*productsMaxInvest[j]
            productsInvestResult[i] = productsMaxInvest[i]
            productsInvestResult[j] = productsMaxInvest[j]
            productsInvestMap[totalReturnInvestment] = productsInvestResult.copy()
            productsInvestResult = [0 for _ in range(productsNum)]
        
    
    
    maxResultKey = max(productsInvestMap.keys())
    
    return productsInvestMap[maxResultKey]