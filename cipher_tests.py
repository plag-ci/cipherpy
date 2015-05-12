import os
import main
import unittest
import tempfile
from utils.monos import *
from utils.poly import *


#### MONO TEST CASES ####

class CeasarTestCase(unittest.TestCase):

	def test_decipher(self):
		text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		declist = ['11111xyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw',
					'vwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu',
					'stuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr',
					'pqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno',
					'lmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					'bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza']
		for i,key in enumerate((3,5,8,11,15,0,25)):
			dec = Caesar(key).decipher(text)
			self.assertEqual(dec.upper(), declist[i].upper())

	def test_encipher(self):
		text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		enclist = ['bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza',
					'cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab',
					'efghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd',
					'hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
					'jklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					'zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy']
		for i,key in enumerate((1,2,4,7,9,0,25)):
			enc = Caesar(key).encipher(text)
			self.assertEqual(enc.upper(), enclist[i].upper())

class AffineTestCase(unittest.TestCase):

	def test_decipher(self):
		text = 'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs'
		declist = ['yfmtahovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkr',
					'onmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqp',
					'jarizqhypgxofwnevmdulctkbsjarizqhypgxofwnevmdulctkbs',
					'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs',
					'tmfyrkdwpibungzslexqjcvohatmfyrkdwpibungzslexqjcvoha',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']
		for i,key in enumerate(((7,3),(3,25),(9,12),(1,0),(19,18),(23,15))):
			a,b = key
			dec = Affine(a,b).decipher(text)
			self.assertEqual(dec.upper(), declist[i].upper())        

	def test_encipher(self):
		text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		enclist = ['hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
					'dgjmpsvybehknqtwzcfiloruxadgjmpsvybehknqtwzcfiloruxa',
					'afkpuzejotydinsxchmrwbglqvafkpuzejotydinsxchmrwbglqv',
					'ovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkryfmtah',
					'sbktcludmvenwfoxgpyhqzirajsbktcludmvenwfoxgpyhqziraj',
					'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs']
		for i,key in enumerate(((1,7),(3,3),(5,0),(7,14),(9,18),(23,15))):
			a,b = key
			enc = Affine(a,b).encipher(text)
			self.assertEqual(enc.upper(), enclist[i].upper())

#### POLY TEST CASES ####

class AutokeyTestCase(unittest.TestCase):
	
	def test_encipher(self):
		keys = ('GERMAN', 'CIPHERS')
		plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
		ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
					  'cjrkiwyhjlnprtvxzbdfhjlnprtvxzbdfhjlnprtvxzbdfhjlnpr')
		for i,key in enumerate(keys):
			enc = Autokey(key).encipher(plaintext[i])
			self.assertEqual(enc.upper(), ciphertext[i].upper())

	def test_decipher(self):
		keys = ('GERMAN','CIPHERS')
		plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
		ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
					  'cjrkiwyhjlnprtvxzbdfhjlnprtvxzbdfhjlnprtvxzbdfhjlnpr')
		for i,key in enumerate(keys):
			dec = Autokey(key).decipher(ciphertext[i])
			self.assertEqual(dec.upper(), plaintext[i].upper())

class VigenereTestCase(unittest.TestCase):

	def test_encipher(self):
		keys = ('GERMAN','CIPHERS')
		plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
		ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
					'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')
		for i,key in enumerate(keys):
			enc = Vigenere(key).encipher(plaintext[i])
			self.assertEqual(enc.upper(), ciphertext[i].upper())

	def test_decipher(self):
		keys = ('GERMAN','CIPHERS')
		plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
					'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
		ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
					'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')
		for i,key in enumerate(keys):
			dec = Vigenere(key).decipher(ciphertext[i])
			self.assertEqual(dec.upper(), plaintext[i].upper())


if __name__ == '__main__':
	unittest.main()