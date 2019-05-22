import random
def myhash(x,a,bite):
	y=(a*x)%bite
	#print(y)
	return y

def CreateBloom(data,bite,a,hashNum,bloomList):
	for i in range(0,hashNum):
		t[i]=myhash(data,a[i],bite)
		bloomList[t[i]]=1
	return bloomList
	
def bloom(data,hashNum,a,bite,Bloomlist=[]):
	for i in range(0,hashNum):
		t[i]=myhash(data,a[i],bite)
		if Bloomlist[t[i]]==0:
			return 0
	return 1  

if __name__=="__main__":
	Dataset=set()
	Bite=int(input("请输入比特大小"))
	HNum=int(input("请输入哈希函数数目"))
	a=[None]*HNum;t=[None]*HNum;Blist=[0]*Bite
	for i in range(0,HNum):
		a[i]=int(random.random()*1000+1)
	print(a)
	f1 = open("stream_for_bm.txt","r")
	while 1:
		line=f1.readline()
		if not line:
			break
		data=int(line)
		Dataset.add(data)
		Blist=CreateBloom(data,Bite,a,HNum,Blist)
	f1.close()
	print(Blist)
	f2 =open("stream_for_query.txt","r")
	i=0
	error_true=0
	error_error=0
	while 1:
		line2=f2.readline()
		if not line2:
			break
		Testdata=int(line2)
		if bloom(Testdata,HNum,a,Bite,Blist):
			if Testdata not in Dataset:
				error_true+=1
		else:
			if Testdata in Dataset:
				print(Testdata)
				error_error+=1
		i+=1
	f2.close()
	print("error_true",error_true)
	print("error_error",error_error)
	print("error_true\i",error_true/i)
	print("error_error\i",error_error/i)