import time
def calc(func):
	def calTime():
		st=time.time()
		print("start Time:",st)
		func()
		et=time.time()
		print("end Time:",et)
		d=et-st
		print("Total Time:",d)
	return calTime


def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
@calc
def read():
	f=fib()
	for i in range(n):
		print(next(f))

n=int(input("enter a number"))
read()
