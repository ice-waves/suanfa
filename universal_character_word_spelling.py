from typing import List

"""
有一个字符串数组words和一字符串chars.假如可以用chars中的字母拼写出words中的某个“单词”(字符串)，
那么我们就认为你掌握了这个单词。

words的字符仅由 a-z 英文小写字母组成。
例如: abc

chars 由 a-z 英文小写字母和“?“组成，其中英文间号”?"表示万能字符，能够在拼写时当做任意一个英文字母，
例如: "?"可以当做"a"等字母

注意:每次拼写时，chars中的每个字母和万能字符都只能使用一次。
输出词汇表words中你掌握的所有单词的个数。 没有掌握任何单词，则输出0。

输入描述.

第1行输入数组words的个数，记为N.
从第2行开始到第N+1行依次输入数组words的每个字符串元素
第N+2行输入字符串chars。


输出描述:

输出一个整数，表示词汇表words中你掌握的单词人数


注意:
1 <= words.length <= 100
1 <= wordslil.length, chars.length <= 100
所有字符串中都仅包含小写英文字母、英文问号

"""



def CharWordsSpelling(n: int, wordsArr: List[str], chars: str) -> int:
	num = 0
	charsMap = {}
	for i in chars:
		if i not in charsMap:
			charsMap[i] = 1
		else:
			charsMap[i] += 1


	for word in wordsArr:
		tempCharMap = charsMap.copy()
		addFlag = True
		for j in word:
			if tempCharMap.get(j):
				if tempCharMap[j] > 0:
					tempCharMap[j] -= 1
				elif tempCharMap[j] == 0:
					if tempCharMap.get('?'):
						if tempCharMap['?'] > 0:
							tempCharMap['?'] -= 1
						elif tempCharMap['?'] <= 0:
							addFlag = False
							break
					else:
						addFlag = False
						break
				else:
					addFlag = False
					break
			elif tempCharMap.get('?'):
				if tempCharMap['?'] > 0:
					tempCharMap['?'] -= 1
				elif tempCharMap['?'] <= 0:
					addFlag = False
					break
			else:
				addFlag = False
				break


		if addFlag:
			num += 1
				
		
	return num


		

if __name__ == '__main__':
	n = 4
	wordsArr = ["cat", "bt", "hat", "tree"]
	chars = "atach??"
	result =  CharWordsSpelling(n, wordsArr, chars)

	print(result)


