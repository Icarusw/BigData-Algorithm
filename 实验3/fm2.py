import random
import time
def GetmiddleMaxn(a=list):
	t=len(a)
	if t%2==1:
		return a[(t-1)//2]
	else:
		return (a[(t-1)//2]+a[t//2])//2

def Getaverage(a=list):
	nsum = 0
	for i in range(0,len(a)):
		nsum += a[i]
	return nsum / len(a)

def myhash(x,a,b):
	y=(a*x)%(2**25)
	return y

def GetMaxn(lines,f1,lnum):
	averageMaxn=0
	Maxn=[0]*lnum
	i=0
	c=2**25
	a=[None]*lnum;b=[None]*lnum;hx=[None]*lnum
	#print("GetMaxn")
	start_time=time.time()
	for t in range(0,lnum):
		a[t]=int(random.random()*c+1)
		b[t]=int(random.random()*c+1)
	end_time0=time.time()
	if (end_time0-start_time)>1:
		print("123")
		#break;
	while(i<lines):
		#print("while")
		n=[0]*lnum
		line=f1.readline()
		if not line:
			break
		data=int(line)
		ASet.add(data)
		end_time1=time.time()
		if (end_time1-start_time)>3:
			print("1234")
		for t in range(0,lnum):
			#print("for")
			hx[t]=myhash(data,a[t],b[t])
			end_time2=time.time()
			if (end_time2-start_time)>3:
				print("1234")
			while hx[t]%2==0:
				if hx[t]==0:
					n[t]=1
					print("0",end=' ')
					break
				n[t]+=1
				hx[t]>>=1
				end_time3=time.time()
				if (end_time3-start_time)>3:
					print(hx,t)
					print("12345")
			if n[t]>=Maxn[t]:
				Maxn[t]=n[t]
		i+=1
	
	print("next",end=' ')
	averageMaxn=Getaverage(Maxn)
	return averageMaxn,f1

if __name__=="__main__":
	esum=0
	m=int(input("请输入分组数:"))
	l=int(input("请输入哈希函数个数:"))
	n=int(input("请输入循环次数："))#循环次数
	middleMaxnlist=[None]*n
	for t in range(0,n):
		ASet=set()#set去重
		MaxN=[None]*m
		middleMaxn=0
		mlines=350000//m
		fp = open("stream_for_fm.txt","r")
		for i in range(0,m):
			MaxN[i],fp=GetMaxn(mlines,fp,l)
		fp.close()
		#print("Maxn",MaxN)
		middleMaxn=int(GetmiddleMaxn(MaxN))
		middleMaxnlist[t]=middleMaxn
		print("估计2**middleMaxn",2**middleMaxn,end=' ')
		a=(i+1)*(t+1)//(m*n)
		print("\r{0}%".format(a),end='')
	print("不同元素的个数：",len(ASet))#set去重
	print("middleMaxnlist",middleMaxnlist)
	j=n
	while j>=0:
		esum+=(middleMaxnlist[j-1]-len(ASet))**2
		j-=1
	error_sum=(esum/n)**0.5
	print("error_sum",error_sum)
	
	