import random
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
	
def GetEsecmom(Num,lines):
	i=0
	while (i<lines):
		line =fp.readline()
		if not line:
			break
		data=int(line)
		#sum+=mdict[data]#mdict的和
		if i in SamplingPSet:
			SamplingKeySet.add(data)
			SamplingDict[data]=SamplingDict.get(data,0)+1
		if data in SamplingKeySet:
			SamplingDict[data]+=1
		i+=1
	return dictvalue2(Num,SamplingDict)

if __name__=="__main__":
	i=0
	mdict=dict()
	#sum=0
	secmom=0#真实二阶矩
	fp = open("stream_for_ams.txt","r")
	m=int(input("请输入分组数"))
	SamplingNum=int(input("请输入采样点个数"))#取样点位置
	SamplingPSet=set()#取样点位置集合
	SamplingKeySet=set()#取样点名称集合
	SamplingDict={}#取样点字典（data:vlaue）
	while 1:
		line =fp.readline()
		if not line:
			break
		data=int(line)
		mdict[data] = mdict.get(data, 0) + 1
		i+=1
	fp.close()#第一遍遍历得到个数和mdict字典
	
	while len(SamplingPSet)<=SamplingNum:
		SamplingPSet.add(int(random.random()*i))
	
	mlines=i//m
	Esecmom=[None]*m
	fp = open("stream_for_ams.txt","r")
	for t in range(0,m):
		Esecmom[t]=GetEsecmom(i,mlines)
	fp.close()
	
	secmom=dictvalue(mdict)
	#Esecmom=dictvalue2(SamplingNum,SamplingDict)
	#print("i",i)
	print("真实二阶矩为",secmom)
	print("平均Esecmom：",sum(Esecmom)//len(Esecmom))
	
	
	
	