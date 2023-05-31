import mysql.connector;
class emp_DB:
	def __init__(self):
		self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="emp",auth_plugin="mysql_native_password")
		self.cur=self.con.cursor()

	def read(self,name,age,address,empcode):
		ins="INSERT INTO emp3(name,age,address,empcode) VALUES (%s,%s,%s,%s)"
		val=(name,age,address,empcode)
		self.cur.execute(ins,val)
		self.con.commit()
	def display(self):
		sel="SELECT * FROM emp3"
		self.cur.execute(sel)
		rows=self.cur.fetchall()
		for i in rows:
			print(i)
	def update(self,name1,name2):
		upd="UPDATE emp3 SET name=%s WHERE name=%s"
		val=(name2,name1)
		self.cur.execute(upd,val)
		self.con.commit()
	def delete(self,name):
		de="DELETE FROM emp3 WHERE name=%s"
		val=(name,)
		self.cur.execute(de,val)
		self.con.commit()

obj=emp_DB()
while True:
	print("1.insert\n 2.display\n 3.update\n 4.delete\n")
	ch=int(input("enter your choice"))
	if ch==1:
		name=input("enter the name")
		age=int(input("enter the age"))
		address=input("enter the address")
		empcode=int(input("enter the empcode"))
		obj.read(name,age,address,empcode)
	elif ch==2:
		obj.display()
	elif ch==3:
		name1=input("enter the name to update")
		name2=input("enter the name")
		obj.update(name1,name2)
	elif ch==4:
		name=input("enter name to be deleted:")
		obj.delete(name)
	else:
		exit()
	

