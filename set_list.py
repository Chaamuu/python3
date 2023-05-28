while True:
	print("set and list operation")
	print("1.set\n 2.list\n 3.exit")
	print("==========")
	ch=int(input("enter your choice"))
	if ch==1:
		s1=set(input("enter the ele"))
		while True:
			print("1.length\n 2.add\n 3.pop\n 4.equivalence\n 5.subset\n 6.superset\n 7.union\n 8.intersection\n 9.set difference\n 10.symmetric difference\n 11.exit()")
			sch=int(input("enter your choice"))
			if sch==1:
				print(len(s1))
			elif sch==2:
				ele=int(input("enter the element"))
				s1.add(ele)
				print(s1)
			elif sch==3:
				print("poped element is",s1.pop())
			elif sch==4:
				s2=set(input("enter the set element"))
				if s1==s2:
					print(s1,"is equal to",s2)
				else:
					print(s1,"is not equal to ",s2)
			elif sch==5:
				s2=set(input("enter the set element"))
				if s1<=s2:
					print(s1,"is subset of",s2)
				else:
					print(s1,"is not subset of",s2)
			elif sch==6:
				s2=set(input("enter the set element"))
				if s1>=s2:
					print(s1,"is superset of",s2)
				else:
					print(s1,"is not superset of",s2)
			elif sch==7:
				s2=set(input("enter set element"))
				print(s1,"U",s2,"=","is",s1|s2)
			elif sch==8:
				s2=set(input("enter the set element"))
				print(s1,"intersection",s2,"=",s1&s2)
			elif sch==9:
				s2=set(input("enter element"))
				print(s1,'-',s2, "is",s1-s2)
				print(s2,'-',s2,"is",s2-s1)
			elif sch==10:
				s2=set(input("enetr the element"))
				print("symmetric difference of" ,s1,"and",s2,"is",s1^s2)
			elif sch==11:
				exit()
	elif ch==2:
		n=int(input("enter the length"))
		list=[]
		for i in range(n):
			ele=input("enter the element")
			list.append(ele)
			print(list)
		while True:
			print("1.append\n 2.insert\n 3.pop\n 4.remove\n 5.length\n 6.reverse\n 7.max\n 8.min\n 9.delete\n 10.clear\n 11.exit")
			c=int(input("enter your choice"))
			if c==1:
				x=input("enter the element to be appended")
				list.append(x)
				print(list)
			elif c==2:
				m=int(input("enter the index"))
				n=input("enter the element to be inserted")
				list.insert(m,n)
				print(list)
			elif c==3:
				print("poped element",list.pop())
				print(list)
			elif c==4:
				l=input("enter the element")
				list.remove(l)
				print(list)
			elif c==5:
				print("length",len(list))
			elif c==6:
				print("reverse list",list[::-1])
			elif c==7:
				print("maximum in list",max(list))
			elif c==8:
				print("minimum in list", min(list))
			elif c==9:
				print("after deleting")
			elif c==10:
				list.clear()
				print(list)
			else:
				exit()



