from typing import List
import heapq
"""
给定长度为的无序的数字数组，每个数字代表二又树的叶子节点的权值，数字数组的值均大于等于1。
请完成一个函数，根据输入的数字数组生成哈夫曼树，并将哈夫曼树按照中序遍历输出。
为了保证输出的二又树中序遍历结果统一，增加以下限制:
二又树节点中，左节点权值小于等于右节点权值，根节点权值为左右节点权值之和当左右节点权值相同时，
左子树高度高度小于等于右子树。


注意:所有用例保证有效，并能生成哈夫曼树。

提醒:哈夫曼树又称最优二又树，是一种带权路径长度最短的二又树。
所谓树的带权路径长度，就是树中所有的叶结点的权值乘上其到根结点的路径长度 
(若根结点为0层，叶结点到根结点的路径长度为叶结点的层数)。

例如:
由叶子节点5 15 40 30 10生成的最优二又树如下图所示，

该树的最短带权路径长度为40*1+30*2+15*3+5*4+10*4=205.

"""

class Node:
	"""docstring for Node"""
	def __init__(self, value: int, nodeLeft=None, nodeRight=None):
		self.value = value
		self.nodeLeft = nodeLeft
		self.nodeRight = nodeRight

	# 定义比较方法，以便在堆中使用  
	def __lt__(self, other):  
		return self.value < other.value  

class HuffmanTree:

	preOrderResult = []
	midOrderResult = []

	# def __init__(self, charWeights):
		# self.nodes = [ Node(x) for x in charWeights ]

		# while len(self.nodes) != 1:
		# 	self.nodes.sort(key=lambda node: node.value, reverse=True)
		# 	for i in self.nodes:
		# 		print(i.value)
		# 	print("===============")
		# 	c = Node(value=self.nodes[-1].value + self.nodes[-2].value)
		# 	c.nodeLeft = self.nodes.pop(-1)
		# 	c.nodeRight = self.nodes.pop(-1)
		# 	self.nodes.append(c)
		
		# self.root = self.nodes[0]

	def __init__(self, charWeights): 
		priority_queue = [Node(x) for x in charWeights] 
		heapq.heapify(priority_queue)
  
		# 当堆中元素大于1时，不断合并  
		while len(priority_queue) > 1:  
			left = heapq.heappop(priority_queue)  
			right = heapq.heappop(priority_queue)  
	
			# 创建一个新的内部节点，频率为左右子节点频率之和  
			merged = Node(left.value + right.value)  
			merged.nodeLeft = left  
			merged.nodeRight = right  
	
			# 将合并后的节点加入堆中  
			heapq.heappush(priority_queue, merged)  
	
    # 最后堆中剩下的节点即为根节点  
		self.root = priority_queue[0]  


	def preOrder(self, node: Node):
		if node is None:
			return
		
		self.preOrderResult.append(node.value)
		self.preOrder(node.nodeLeft)
		self.preOrder(node.nodeRight)

	def midOrder(self, node: Node):
		if node is None:
			return
		self.midOrder(node.nodeLeft)
		self.midOrderResult.append(node.value)
		print(self.midOrderResult)
		self.midOrder(node.nodeRight)


def GenHuffmanTree(charWeights: List)-> List:
	huffmanTree = HuffmanTree(charWeights)
	huffmanTree.midOrder(huffmanTree.root)
	return huffmanTree.midOrderResult


midOrderResult = []

def Order(node: Node):
	if node is None:
		return
	Order(node.nodeLeft)
	midOrderResult.append(node.value)
	print(midOrderResult)
	Order(node.nodeRight)


if __name__ == '__main__':
	root = Node(1)  
	root.nodeLeft = Node(2)  
	root.nodeRight = Node(3)  
	root.nodeLeft.nodeLeft = Node(4)  
	root.nodeLeft.nodeRight = Node(5)
	Order(root)