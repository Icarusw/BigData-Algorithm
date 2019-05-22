import random
import sys
import time
if __name__=="__main__":
	start_time=time.time()
	s=int(input("请输入集合大小："))
	#s=int(sys.argv[1])
	SList=[None]*s
	SumOfSList=0
	i=0#当前个数
	sum=0
	fp = open("stream.txt","r")
	while(1):
		#print(i,end='')
		line=fp.readline()
		if not line:
			break
		data=int(line)
		sum+=data
		if (i<s):
			SList[i]=data
			SumOfSList+=data
		else:
			p=random.random()
			if(p<(s/(i+1))):#还i未更新
				t=random.randint(0,s-1)
				SumOfSList -= SList[t]
				SList[t]=data
				SumOfSList += data
		i+=1
		#print("\r",end='')
	fp.close()
	print("i",i)
	print("SumOfSList=",SumOfSList)
	print("SumOfSList/s=",SumOfSList/s)
	print("sum/i=",sum/i)
	print("错误率：",(1-(SumOfSList/s)/(sum/i)))
	end_time=time.time()
	print("time%.2f"%float(end_time-start_time))