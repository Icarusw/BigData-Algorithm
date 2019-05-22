from AMS1 import *


if __name__=="__main__":
	i=0
	n=0
	time=int(input("请输入时刻："))
	SamplingNum=int(input("请输入采样点个数："))#取样点个数
	SamplingDataset=set()
	SamplingDict={}
	TrueSamplingDict={}
	fp = open("stream_for_ams.txt","r")
	while 1:
		if i>=time:
			break
		line =fp.readline()
		if not line:
			break
		data=int(line)
		if len(SamplingDataset)<SamplingNum:
			SamplingDataset.add(data)
		else:
			p=random.random()
			if(p<(SamplingNum/(i+1))):#还i未更新
				x=SamplingDataset.pop()
				del SamplingDict[x]
		if data in SamplingDataset:
			SamplingDict[data] = SamplingDict.get(data, 0) + 1
		TrueSamplingDict[data]=TrueSamplingDict.get(data,0)+1
		i+=1
	print(SamplingDict)
	#print("TrueSamplingDict",TrueSamplingDict)
	secomon=dictvalue(TrueSamplingDict)
	Esecmom=dictvalue2(i,SamplingDict)
	print("真实二阶矩",secomon)
	print("Esecmom",Esecmom)
	fp.close()