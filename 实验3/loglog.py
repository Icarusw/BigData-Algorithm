import random
import math

def p(y):
	n=0
	while y%2==0:
		if y==0:
			break
		n+=1
		y>>=1
	return n 

if __name__=="__main__":
	esum=0
	DataSet=set()
	a=int(random.random()*2**25)
	m=int(input("请输入分组数:"))
	M=[0]*m
	fp=open("stream_for_fm.txt","r")
	while(1):
		line=fp.readline()
		if not line:
			break
		data=int(line)
		DataSet.add(data)
		hx=hash(data)
		j=hx%m
		w=math.floor(hx/m)
		M[j]=max(M[j],p(int(w)))
	s=sum(M)/m
	e=0.39701*m*(2**s)
	print("DataSet:",len(DataSet))
	print("e:",e)
	fp.close()