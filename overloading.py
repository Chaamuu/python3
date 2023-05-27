#create a class with a method name as hello overloading
class person:
	def hello(self,name=None,age=None):
		if name!=None and age!=None:
			print("hello",name,age)
		elif name!=None:
			print("hello",name)
		else:
			print("hello")
d1=person()
d1.hello()
d1.hello('andrean')
d1.hello('andrean','29') 
