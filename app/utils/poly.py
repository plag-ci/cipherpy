from .cipher import Cipher
import re

class Playfair(Cipher):
	
	def __init__(self,key='monarchybdefgiklpqstuvwxz'):
		self.key = [k.upper() for k in key]

	def encipher_pair(self,a,b):
		if a == b: b = 'X'
		arow,acol = self.key.index(a)/5 , self.key.index(a)%5
		brow,bcol = self.key.index(b)/5 , self.key.index(b)%5
		if arow == brow:
			return (self.key[arow*5+(acol+1)%5] + self.key[brow*5+(bcol+1)%5])
		elif acol == bcol:
			return (self.key[((arow+1)%5)*5+acol] + self.key[((brow+1)%5)*5+bcol])
		else:
			return (self.key[arow*5 + bcol] + self.key[brow*5 + acol])

	def decipher_pair(self,a,b):
		assert a != b, 'two of the same letters occured together, illegal in playfair'
		arow,acol = self.key.index(a)/5 , self.key.index(a)%5
		brow,bcol = self.key.index(b)/5 , self.key.index(b)%5
		if arow == brow:
			return (self.key[arow*5+(acol-1)%5] + self.key[brow*5+(bcol-1)%5])
		elif acol == bcol:
			return (self.key[((arow-1)%5)*5+acol] + self.key[((brow-1)%5)*5+bcol])
		else:
			return self.key[arow*5 + bcol] + self.key[brow*5 + acol]

	def encipher(self,string):   
		string = re.sub(r'[J]','I',string)
		if len(string)%2 == 1: string = string + 'X'
		ret = ''
		for c in xrange(0,len(string),2):
			ret += self.encipher_pair(string[c],string[c+1])
		return ret    

	def decipher(self,string):
		if len(string)%2 == 1: string = string + 'X'
		ret = ''
		for c in xrange(0,len(string),2):
			ret += self.decipher_pair(string[c],string[c+1])
		return ret

class Autokey(Cipher):

	def __init__(self,key='FORTIFICATION'):
		self.key = [k.upper() for k in key]

	def encipher(self,string):
		ret = ''
		for (i,c) in enumerate(string):
			if i<len(self.key): offset = self.conv2i(self.key[i])
			else: offset = self.conv2i(string[i-len(self.key)])     
			ret += self.conv2a(self.conv2i(c)+offset)
		return ret

	def decipher(self,string):
		ret = ''
		for (i,c) in enumerate(string):
			if i<len(self.key): offset = self.conv2i(self.key[i])
			else: offset = self.conv2i(ret[i-len(self.key)])             
			ret += self.conv2a(self.conv2i(c)-offset)
		return ret

class Vigenere(Cipher):

	def __init__(self,key='fortification'):
		self.key = [k.upper() for k in key]

	def encipher(self,string):
		ret = ''
		for (i,c) in enumerate(string):
			i = i%len(self.key)
			ret += self.conv2a(self.conv2i(c) + self.conv2i(self.key[i]))
		return ret

	def decipher(self,string):
		ret = ''
		for (i,c) in enumerate(string):
			i = i%len(self.key)
			ret += self.conv2a(self.conv2i(c) - self.conv2i(self.key[i]))
		return ret