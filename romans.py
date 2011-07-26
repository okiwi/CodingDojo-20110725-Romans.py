import unittest

class TestRomans(unittest.TestCase):

	def test_return_romans_is_good(self):
		self.assertEquals(1, romans("I"))
		self.assertEquals(2, romans("II"))
	
	def test_III_is_three(self):
		self.assertEquals(1 + 2, romans("I" + "II"))

	def test_IV_is_four(self):
		self.assertEquals(-1 + 5, romans("I" + "V"))

	def test_V_is_five(self):
		self.assertEquals(5, romans("V"))

	def test_C_is_hundred(self):
		self.assertEquals(100, romans("C"))

	def test_VI_is_six(self):
		self.assertEquals(5 + 1, romans("V" + "I"))

	def test_X_is_ten(self):
		self.assertEquals(10, romans("X"))

	def test_L_is_fifty(self):
		self.assertEquals(50, romans("L"))
	
	def test_IX_is_nine(self):
		self.assertEquals(9, romans("IX"))

	def test_XIV_is_fourteen(self):
		self.assertEquals(14, romans("XIV"))
	
	def test_XC_is_ninety(self):
		self.assertEquals(90, romans("XC"))

	def test_XL_is_forty(self):
		self.assertEquals(40, romans("XL"))
		self.assertEquals(140, romans("CXL"))			

	def test_wtf_is_nan(self):
		self.assertRaises(NotRomanNumber, lambda: romans(""))

class NotRomanNumber (Exception):
	pass
	

def romans(number):
	if not number:
		raise NotRomanNumber()
		
	look_up = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100
	}

	if len(number) == 1:
		return look_up[number]
	elif romans(number[0]) < romans(number[1]) :
		return romans (number[1:]) - romans(number[0])
	return romans(number[0]) + romans(number[1:])


unittest.main()
