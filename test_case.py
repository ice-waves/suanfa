import unittest
import universal_character_word_spelling as ucws
import find_location as fl
import generate_huffman_tree as ght
import min_difference as md
import buy_gems as bg

class TestCase(unittest.TestCase):
	"""docstring for TestExampleSpell"""
	def test_CharWordsSpelling(self):
			n = 4
			wordsArr = ["cat", "bt", "hat", "tree"]
			chars = "atach??"
			self.assertEqual(ucws.CharWordsSpelling(n, wordsArr, chars), 3)

	def test_FindLocation(self):
			order = "93,95,97,100,102,123,155"
			result = fl.findLocation(order, 101)
			self.assertEqual(result, 5)

	def testGenHuffmanTree(self):
		charWeights = [5, 15, 40, 30, 10]
		result = ght.GenHuffmanTree(charWeights)
		expect = [40, 100, 30, 60, 15, 30, 5, 15, 10]
		self.assertEqual(result, expect)

	def testMinDifference(self):
		scores = [5, 1, 8, 3, 4, 6, 7, 10, 9, 2]
		result = md.minDifference(scores)
		expect = 1
		self.assertEqual(result, expect)
	
	def testBuyGems(self):
		cases = [
			{'gems': [8, 4, 6, 3, 1, 6, 7], 'money': 10, 'expect': 3},
			{'gems': [], 'money': 1, 'expect': 0},
			{'gems': [6, 1, 3, 1, 8, 9, 3, 2, 4], 'money': 15, 'expect': 4},
   			{'gems': [1, 1, 1, 1, 1, 1, 1, 1, 1], 'money': 10, 'expect': 9},
		]
  
		for every in cases:
			result = bg.buyGems(len(every['gems']), every['gems'], every['money'])
			self.assertEqual(result, every['expect'])

if __name__ == '__main__':
	unittest.main()