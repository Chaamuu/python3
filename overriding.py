class employee:
	apply_raise=2.5
	def read(self):
		self.first=input("enter the first name")
		self.last=input("enter the last name")
		self.empid=input("enter the empid")
		self.pay=int(input("enter the salary"))
	def display(self):
		print("first name",self.first)
		print("last name",self.last)
		print("empid=",self.empid)
		print("pay=",self.pay)
	def  pay_raise(self):
		self.pay=int(self.pay)*self.apply_raise

class developer(employee):
	apply_raise=2.5
	def pay_raise(self):
		super().apply_raise
class manager(employee):
	apply_raise=1.5
	def pay_raie(self):
		super().apply_raise

print("enter the developer details")
d1=developer()
d1.read()

print("enetr the manager details")
d2=manager()
d2.read()

d1.pay_raise()
d2.pay_raise()

d1.display()
d2.display()
