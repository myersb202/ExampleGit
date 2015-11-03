class Animal:
	def __init__(self,name):
		self.name = name
		self.tricks=[]
	def prin(self):
		print self.name
		#print self.name
	def addTrick(self,trick):
		self.tricks.append(trick)

anim1=Animal("Doggie")
anim2=Animal("Kitty")

anim1.prin()
anim2.prin()
anim1.addTrick("play dead")
anim2.addTrick("lay down")
print anim1.tricks
print anim2.tricks
print anim1.name
print anim2.name

