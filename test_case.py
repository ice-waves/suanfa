import unittest
import universal_character_word_spelling as ucws
import find_location as fl
import generate_huffman_tree as ght
import min_difference as md
import buy_gems as bg
import invest_finance as infi
import seat_num as sn
import find_gold as fg
import password_check as pc
import sushi as ss
import data_compression as dc


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

	def testInvestFinance(self):
		cases = [
      		{
       			'productsNum': 5,
          		'totalInvestmentAmount': 100, 
            	'totalRisk': 10, 
             	'productsRate': [10, 20, 30, 40, 50],
				'productsRisk': [3, 4, 5, 6, 10],
				'productsMaxInvest': [20, 30, 20, 40, 30],
				'expect': [0, 30, 0, 40, 0]
			},
			{
       			'productsNum': 2,
          		'totalInvestmentAmount': 100, 
            	'totalRisk': 10, 
             	'productsRate': [10, 20],
				'productsRisk': [5, 6],
				'productsMaxInvest': [40, 30],
				'expect': [0, 30]
			}
		]
		for every in cases:
			result = infi.investFinance(
				every['productsNum'],
				every['totalInvestmentAmount'],
				every['totalRisk'],
				every['productsRate'],
				every['productsRisk'],
				every['productsMaxInvest']
            )
			self.assertEqual(result, every['expect'])
	

	def testSeatNum(self):
		cases = [
      		{'seatTag': [1, 0, 0, 0, 1], 'expect': 1},
			{'seatTag': [0, 1, 0, 1], 'expect': 0},
			{'seatTag': [0, 0, 0, 0, 0, 0], 'expect': 3},
			{'seatTag': [0], 'expect': 1},
			{'seatTag': [1], 'expect': 0}
        ]
		for every in cases:
			result = sn.seatNum(every['seatTag'])
			self.assertEqual(result, every['expect'])
	
	def testFindGold(self):
		cases = [
			{'m': 4, 'n': 5, 'k': 7, 'expect': 20},
			{'m': 40, 'n': 40, 'k': 18, 'expect': 1484}
		]

		for every in cases:
			result = fg.findGold(every['m'], every['n'], every['k'])
			self.assertEqual(result, every['expect'])
	
	def testPasswordCheck(self):
		cases = [
			{'str': 'ABC<c89%000<', 'expect': 'ABc89%00,true'},
			{'str': '<ABC', 'expect': 'ABC,false'},
			{'str': 'AB<<C<', 'expect': ',false'}
		]
		for every in cases:
			result = pc.passwordCheck(every['str'])
			self.assertEqual(result, every['expect'])

	def testSushi(self):
		cases = [
			{'prices': [3, 14, 15, 6, 5], 'expect': [3, 20, 21, 11, 8]},
			{'prices': [3, 15, 6, 14], 'expect': [3, 21, 9, 17]}
		]

		for every in cases:
			result = ss.buySushi(every['prices'])
			self.assertEqual(result, every['expect'])
	
	def testDataCompression(self):
		cases = [
			{'points': [2, 8, 3, 7,3, 6, 3, 5, 4, 4, 5, 3, 6, 2, 7, 3, 8, 4, 7, 5], 'expect': [2, 8, 3, 7, 3, 5, 6, 2, 8, 4, 7, 5]},
			{'points': [3, 0, 2, 0, 4, 0], 'expect': [3, 0, 4, 0]}
  		]

		for every in cases:
			result = dc.dataCompression(every['points'])
			self.assertEqual(result, every['expect'])
 
   
if __name__ == '__main__':
	unittest.main()