import sys

class BucketNode():
	def __init__(self,size,time_stamp):
		self.size=size
		self.time_stamp=time_stamp
		self.next=None
	def count(self):
		return self.size
		
		
'''
def merge(n,MSBucket,Blist=[]):#50
	i=n-1
	#print("Blist",Blist)
	while i>1:
		if((Blist[i].size == Blist[i-1].size) and (Blist[i-1].size== Blist[i-2].size)):
			Blist[i - 2].size *=2
			Blist[i - 2].time_stamp = Blist[i - 1].time_stamp
			Blist[i - 1].time_stamp = Blist[i].time_stamp
			#print ("b[0]",Blist[0].size)
			j=i
			while j<n:
				Blist[j] = Blist[j+1]
				#print ("b[count_bucket-1]", Blist[count_bucket - 1].size)
				j+=1
			n = n-1
		i=i-1
	#print("n",n)
	return  Blist,n
'''
def merge(cbucket,MSBucket,Blist=[]):
	i=cbucket-1
	while i>MSBucket-1:
		if ((Blist[i].size == Blist[i - MSBucket].size)):
			Blist[i - MSBucket].size *=2
			Blist[i - MSBucket].time_stamp = Blist[i - MSBucket+1].time_stamp
			j=i-MSBucket+1
			while j<cbucket-1:
				Blist[j] = Blist[j+1]
				j+=1
			cbucket = cbucket - 1
		i=i-1
	return  Blist,cbucket




def estimate(count_window,count_bucket,n,Blist=[]):
	sum=0;i=count_bucket-1
	#print("count_window",count_window)
	#print("n",n)
	while i>=0:
		if (Blist[i].time_stamp >= n - count_window):
			#print("i",i)
			sum+=Blist[i].size
			#print("sum",sum)
		else :
			#print("Blist[i+1].size",Blist[i+1].size)
			#print("i",i)
			sum-=Blist[i+1].size//2
			break
		i-=1
	print("估算滑动窗口内1_bit个数：", sum)
	return sum

def accurate(count_window,Wlist=[]):
	#print ("Wlist：" , Wlist)
	n=0#bit个数
	i=0
	for i in range(count_windows):
		if(Wlist[i]==1):
			n+=1
	print ("滑动窗口内1_bit精确个数为：%d\n" % n)
	return n



if __name__=="__main__":
	n=1#时间戳
	global count_bucket
	count_bucket=0
	BucketList=[None]*10010
	accuracy=float(input("请输入精确度"))
	#accuracy=float(sys.argv[3])
	MaxSameBucket=int(1//(2*accuracy)+1)#可同时存在的最多的相同桶数
	#print("MaxSameBucket",MaxSameBucket)
	count_windows=int(input("请输入滑动窗口大小："))
	#count_windows=int(sys.argv[1])
	WindowsList=[None]*count_windows
	t=int(input("请输入时刻"))
	#t=int(sys.argv[2])
	fp = open("01stream.txt","r")
	while(1):
		line=fp.readline()
		if not line:
			break
		data=int(line.strip("\n"))
		p=(n-1)%int(count_windows)
		WindowsList[p]=data
		if (data==1):
			BucketList[count_bucket]=BucketNode(1,n)
			if (count_bucket >MaxSameBucket):
				BucketList,count_bucket=merge(count_bucket,MaxSameBucket,BucketList)
			count_bucket += 1
		n+=1
		if(n==t+1):
			break;
	print("字符流个数：%d\n" % (n-1))
	print("桶数目:%d\n"%(count_bucket))
	fp.close()
	i=0
	for i in range(count_bucket):
		print ("第%2d桶  桶大小:%5d   时间戳：%d\n"%(i,BucketList[i].size,BucketList[i].time_stamp))
	ENum=estimate(count_windows,count_bucket,n-1,BucketList)
	ANum=accurate(count_windows,WindowsList)
	print("错误率：",(1-ENum/ANum))