#! /usr/bin/python

import math
import sys


def slope(p,r,k):
	return r*p*(1-p/k)


def vh(h,p0,r,t0,k,n):
	file = open("data/rval_"+str(r)+".dat", "wb")
	tmax=k
	p=p0
	t=t0
	i=0
	dt=(tmax-t0)/float(n)
	while (i<=n):
		p=p+h(p,r,k)*dt
		file.write("%f %f %f\n" % (float(t),float(p),float(h(p,r,k))))
		print t,p,h(p,r,k)
		i+=1
		t+=dt
	file.close()

vh(slope,sys.argv,sys.argv,sys.argv,sys.argv,sys.argv)

