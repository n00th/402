#! /usr/bin/python

from math import*
file = open("data/datatest.csv", "wb")


def f2(x):			#fonction -x
	return -x


def eulerplus(F,t0,tm,x0,n):
	t=t0
	x=0
	dt=(tm-t0)/float(n)	
	for i in range(n):	
		x_til=x0+F(x)*dt
		x=x0+0.5*(F(x0)+F(x_til))*dt
		file.write(str(t))
		file.write(" ")
		file.write(str(x))
		file.write("\n")
		print t,x
		x0=x		
		t+=dt

def euler(F,t0,tm,x0,n):
	t=t0
	x=0
	dt=(tm-t0)/float(n)	
	for i in range(n):	
		x=x0+F(x)*dt
		file.write(str(t))
		file.write(" ")
		file.write(str(x))
		file.write("\n")
		print t,x
		x0=x		
		t+=dt

def rugkut(F,t0,tm,x0,n):
	t=t0
	x=0
	dt=(tm-t0)/float(n)	
	for i in range(n):
		k1=F(x0)*dt
		k2=F(x0+0.5*k1)*dt
		k3=F(x0+0.5*k2)*dt
		k4=F(x0+k3)*dt
		x=x0+(1./6)*(k1+2*k2+2*k3+k4)
		file.write(str(t))
		file.write(" ")
		file.write(str(x))
		file.write("\n")
		print t,x
		x0=x		
		t+=dt


c=input("Choose euler or euler enhanced : ")
if c==1:
	print "choise made is 1"
	euler(f2,0,5,1,50)
elif c==2:
	print "choice made is 2"
	eulerplus(f2,0,5,1,50)
elif c==3:
	print "choice made is 3"	
	rugkut(f2,0,5,1,50)

