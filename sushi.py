from typing import List
"""
寿司店周年庆，正在举办优惠活动回馈新老容户。
寿司转密上总共有n盎寿司，priceso是第盛寿司的价格，
如果客户选择了第盗寿司，寿司店免费脂送容户距高第盛寿司最近的下一盎寿司j，
前提是prices[i] < prices[j]，如果没有满足条件的j。则不赠送寿司。
每个价格的寿司都可无限供应
"""

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = LinkedNode(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            
            last.next = newNode
            newNode.next = self.head




def buySushi(prices: List[int]) -> List[int]:
    result = []
    linkedList = CircularLinkedList()
    for price in prices:
        linkedList.append(price)
    
    for i in range(len(prices)):
        curNode = linkedList.head
        while curNode.data != prices[i]:
            curNode = curNode.next
        
        nextNode = curNode.next
        sushiPrice = prices[i]
        while nextNode.data != prices[i]:
            if nextNode.data < prices[i]:
                sushiPrice = nextNode.data + prices[i]
                break
            nextNode = nextNode.next

        result.append(sushiPrice)
    
    return result
        
    
if __name__ == '__main__':
    buySushi([3, 14, 15, 6, 5])
