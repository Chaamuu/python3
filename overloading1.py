class calc:
	def add(self,a=None,b=None):
		if a!=None and b!=None:
			if ((type(a)==int and type(b)==int) or (type(a)==str and type(b)==str)):
				return a+b
			else:
				return "incompatible type"
		else:
			return "2 arguments required"
obj=calc()
print(obj.add(5,6))
print(obj.add("hii","hello"))
print(obj.add("hii",5))
print(obj.add(5))
