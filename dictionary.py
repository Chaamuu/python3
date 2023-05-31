d=dict()
class employee:
	def input(self):
		self.name=input("enter emp name\n")
		self.address=input("enter the address\n")
		self.pan=input("enter the pan\n")
		self.basic=int(input("enter the basic salary\n"))
		self.deduct=int(input("enter the deduction\n"))
		self.tds=int(input("enter tds\n"))
		self.hra=1.25*self.basic
		self.da=0.25*self.basic
		self.gross_sal=self.basic+self.hra+self.da
		self.net_pay=self.gross_sal-self.deduct
		self.update()
	def update(self):
		d.update({self.name:{
			"name":self.name,
			"address":self.address,
			"pan":self.pan,
			"basic":self.basic,
			"deduct":self.deduct,
			"tda":self.tda,
			"hra":self.hra,
			"da":self.da,
			"gross_sal":self.gross_sal,
			"net_pay":self.net_pay,
		}})
	def search(self,name):
		flag=0
		for key in d:
			if key==name:
				print("emploee found")
				for i in d[key]:
					print(i,d[key][i])
					flag=1
		if flag==0:
			print("no record found")

	def printemp(self):
		for key in d:
			print(key,d[key])

class employee(employee):
	em=employee()
	while True:
		ch=int(input("\n 1.to add employee \n 2-print all employees \n 3-find an employee by name\n 0-exit \n"))
		if ch==1:
			em.input()
		elif ch==2:
			em.printemp()
		elif ch==3:
			name=input("enter the name of employee to be search")
			em.search(name)
		elif ch==0:			break
