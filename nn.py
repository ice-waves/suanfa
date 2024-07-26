# 节点类
class Node(object):
    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None

    def __lt__(self, other):
        self._value < other._value

# 哈夫曼树类
class HuffmanTree(object):
    midOrderResult = []

    # 根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def __init__(self, char_weights):
        priority_queue = [Node(x) for x in char_weights]  

        
        # self.a = [Node(part) for part in char_weights]  # 根据输入的字符及其频数生成叶子节点
        while len(priority_queue) != 1:
            priority_queue.sort()
            left = priority_queue.pop(0)
            right = priority_queue.pop(0)
            c = Node(value=(left._value + right._value))
            c._left = left
            c._right = right
            priority_queue.append(c)

        self.root = priority_queue[0]

    def midOrder(self, node: Node):
        if node is None:
            return
        self.midOrder(node._left)
        self.midOrderResult.append(node._value)
        print(self.midOrderResult)
        self.midOrder(node._right)




if __name__ == '__main__':
    tree = HuffmanTree([5, 15, 40, 30, 10])
    tree.midOrder(tree.root)
