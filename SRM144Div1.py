class BinaryCode:
	def f(self,msg,p):
		for i in xrange(1,len(msg)+1):
			c = 0
			if i==1:
				c = ord(msg[i-1]) -ord('0')- (ord(p[i-1]) -ord('0'))
			else:
				c = ord(msg[i-1]) -ord('0')- (ord(p[i-1]) -ord('0')) - (ord(p[i-2]) -ord('0'))
			if i == len(msg):
				if c!=0: return "NONE"
			elif c>=2 or c<0:
				return "NONE"
			c = chr(ord('0')+c)
			p += c
		
		return p[:-1]
		
	def decode(self,msg):
		p1='0'
		p1=self.f(msg,p1)
		p2='1'
		p2=self.f(msg,p2)
		return (p1,p2)
