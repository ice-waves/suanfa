import unittest
import universal_character_word_spelling as ucws
import find_location as fl
import generate_huffman_tree as ght


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

if __name__ == '__main__':
	unittest.main()