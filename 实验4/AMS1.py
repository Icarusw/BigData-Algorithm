import random
#import numpy as np
def dictvalue(dict={}):
	i=len(dict)
	sum=0
	values=list(dict.values())
	while i>0:
		sum+=values[i-1]**2
		i-=1
	return sum
	
	
def dictvalue2(n,dict={}):
	i=len(dict)
	sum=0
	values=list(dict.values())
	while i>0:
		sum+=(values[i-1]*2-1)*n
		i-=1
	return sum//len(dict)
	
def GetEsecmom(Num,lines,t):
	i=0
	while (i<lines):
		line =fp.readline()
		if not line:
			break
		data=int(line)
		nl=[p+t*lines for p in SamplingPSet]
		if i in nl:
			SamplingKeySet.add(data)
			SamplingDict[data]=SamplingDict.get(data,0)+1
		if data in SamplingKeySet:
			SamplingDict[data]+=1
		i+=1
	#print(lines)
	#print(SamplingDict)
	return dictvalue2(Num,SamplingDict)

if __name__=="__main__":
	j=0
	esum=0
	m=int(input("请输入分组数："))
	SamplingNum=int(input("请输入采样点个数："))#取样点个数
	n=int(input("请输入循环次数："))#循环次数
	WEsecmomlist=[None]*n
	for j in range(0,n):
		i=0
		mdict=dict()
		#sum=0
		secmom=0#真实二阶矩
		fp = open("stream_for_ams.txt","r")
		SamplingPSet=set()#取样点位置集合
		SamplingKeySet=set()#取样点名称集合
		SamplingDict={}#取样点字典(data:vlaue)
		while 1:
			line =fp.readline()
			if not line:
				break
			data=int(line)
			mdict[data] = mdict.get(data, 0) + 1
			i+=1
		fp.close()#第一遍遍历得到个数i和mdict字典
		
		while len(SamplingPSet)<=SamplingNum:
			SamplingPSet.add(int(random.random()*(i//m)))
		
		mlines=i//m
		Esecmom=[None]*m
		fp = open("stream_for_ams.txt","r")
		for t in range(0,m):
			Esecmom[t]=GetEsecmom(i,mlines,t)
		fp.close()
		
		secmom=dictvalue(mdict)
		Esecmom.sort()
		#print(Esecmom)
		#print("WEsecmomlist",WEsecmomlist)
		print("真实二阶矩为",secmom)
		if m%2==1:
			WEsecmomlist[j]=Esecmom[(m-1)//2]
		else:
			WEsecmomlist[j]=(Esecmom[m//2-1]+Esecmom[m//2])//2
		print("平均WEsecmomlist[j]：",WEsecmomlist[j])
	while j>=0:
		esum+=(WEsecmomlist[j]-secmom)**2
		j-=1
	error_sum=(esum/n)**0.5
	print("error_sum",error_sum)