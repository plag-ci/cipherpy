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

class Hill(Cipher):
    def __init__(self, key):
        self.key = key
    def encipher(self, message, encryption=True):
        matrix = self.key
        message = message.upper()
        if not invertible(matrix):
            return "Non invertible matrix"
        if len(message) % 2 != 0:
            message = message + 'X'
        couple = [list(message[i*2:(i*2)+2]) for i in range(0, len(message)/2)]
        result = [i[:] for i in couple]
        if not encryption:
            matrix = inverse_matrix(matrix)
        for i, c in enumerate(couple):
            if c[0].isalpha() and c[1].isalpha():
                result[i][0] = chr(((ord(c[0])-65) * matrix[0][0] + \
                                        (ord(c[1])-65) * matrix[0][1]) % 26 + 65)
                result[i][1] = chr(((ord(c[0])-65) * matrix[1][0] + \
                                        (ord(c[1])-65) * matrix[1][1]) % 26 + 65)
        return "".join(["".join(i) for i in result])

    def decipher(self, cypher):
        matrix = self.key
        return self.encipher(cypher, False)


def gcd_v1(x,y):
    assert x or y, "both arguments equals to zero " + `x, y`
    while y:
        (x, y) = (y, x%y)
    return abs(x)

def invertible(matrix):
    determinant = matrix[0][0] * matrix[1][1] - \
                    matrix[1][0] * matrix[0][1]
    return gcd_v1(determinant, 26) == 1

def inverse_matrix(matrix):
    if not invertible(matrix):
        return "Non invertible matrix"
    result = [i[:] for i in matrix]
    result[0][0] = matrix[1][1]
    result[1][1] = matrix[0][0]
    result[1][0] = (-matrix[1][0]) % 26
    result[0][1] = (-matrix[0][1]) % 26
    
    return result