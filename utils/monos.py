from .cipher import Cipher

class Caesar(Cipher):

	def __init__(self,key=3): #ceaser 3 mucx :))
		self.key = key % 26

	def encipher(self,string):
		ret = ''
		for c in string:
			if c.isalpha(): # Alphabet controlls
				ret += self.conv2a( self.conv2i(c) + self.key )
			else:
				ret += c
		return ret

	def decipher(self,string):     
		ret = ''
		for c in string:
			if c.isalpha(): # Alphabet controlls
				ret += self.conv2a( self.conv2i(c) - self.key )
			else:
				ret += c
		return ret

class Additive(Cipher):

    def __init__(self,a=15):
        self.a = a

    def encipher(self,string):        
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.conv2i(c) + self.a)
            else: ret += c
        return ret

    def decipher(self,string):       
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.conv2i(c) - self.a)
            else: ret += c
        return ret

class Multiplicative(Cipher):

    def __init__(self,a=7):
        self.a = a
        self.inva = -1
        for i in range(1,26,2):
            if (self.a*i) % 26 == 1: self.inva = i
        #assert 0 <= self.inva <= 25, 'invalid key: a='+str(a)+', no inverse exists (mod 26)'

    def encipher(self,string):        
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.a*self.conv2i(c))
            else: ret += c
        return ret

    def decipher(self,string):       
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.inva*self.conv2i(c))
            else: ret += c
        return ret

class Affine(Cipher):

    def __init__(self,a=5,b=9):
        self.a = a
        self.b = b
        self.inva = -1
        for i in range(1,26,2):
            if (self.a*i) % 26 == 1: self.inva = i
        #assert 0 <= self.inva <= 25, 'invalid key: a='+str(a)+', no inverse exists (mod 26)'

    def encipher(self,string):        
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.a*self.conv2i(c) + self.b)
            else: ret += c
        return ret

    def decipher(self,string):       
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.conv2a(self.inva*(self.conv2i(c) - self.b))
            else: ret += c
        return ret

class Substitution(Cipher):

    def __init__(self,key='AJPCZWRLFBDKOTYUQGENHXMIVS'):
        assert len(key) == 26
        self.key = [k.upper() for k in key]
        self.invkey = ''

    def encipher(self,string):
        ret = ''
        for c in string.upper():
            if c.isalpha(): ret += self.key[self.conv2i(c)]
            else: ret += c
        return ret

    def decipher(self,string):
        if self.invkey == '':
            for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
                self.invkey += self.conv2a(self.key.index(i))
        ret = ''
        for c in string.upper():
            if c.isalpha(): ret += self.invkey[self.conv2i(c)]
            else: ret += c
        return ret