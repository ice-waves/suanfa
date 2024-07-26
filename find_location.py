"""
小朋友出操，按学号从小到大排成一列;
小明来迟了，请你给小明出个主意，让他尽快找到他应该排的位置。
算法复杂度要求不高于NLog (n) ，
学号为整数类型，队列规模<=10000;

输入描述
第一行:输入已排成队列的小朋友的学号 (正整数)，以””隔开:90: 93 95 97 100 102 123 155
第二行:小明学号，如110:
输出描述:
输出个数字，代表队列位置(从1开始)


题目类型：二分查找
"""

def findLocation(source: str, target: int) -> int:
	soruceIntArr = [int(item) for item in source.split(',')]

	start, end, targetIndex = 0, len(soruceIntArr)-1, 0

	middle = int(start + (end - start) / 2)

	while start <= end:
		middle = int(start + (end - start) / 2)
		if soruceIntArr[middle] < target:
			start = middle+1
		elif soruceIntArr[middle] > target:
			end = middle-1
		else:
			pass

	targetIndex = start + 1 # 索引加一
	return targetIndex

if __name__ == '__main__':
	order = "93,95,97,100,102,123,155"
	result = findLocation(order, 101)
	print(result)

