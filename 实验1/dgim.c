#include "stdio.h"
#include "stdlib.h"

typedef struct
{
    int size;
    int time_stamp;
}BucketNode,*Bucket;

int count_bucket = 0;

void merge(Bucket buc,int n);
void estimate(Bucket buc,int count_window,int n);
void accurate(int *slip_window,int count_window);

int main()
{
    int data;    //接收数据流
    int n = 1;    //时间戳
    int t;    //需要输入的任意时刻
    int i;

    Bucket buc  = (Bucket)malloc(50 * sizeof(BucketNode));    //桶_结构体指针数组

    int count_window;    //滑动窗口大小
    int *slip_window;    //滑动窗口数组
    FILE *fp;

    printf("请输入滑动窗口大小：\n");
    scanf("%d",&count_window);    //输入滑动窗口大小
    slip_window = (int *)malloc(count_window * sizeof(int));    //滑动窗口数组分配空间

    printf("请输入时刻：\n");
    scanf("%d",&t);

    fp = fopen("01stream.txt","r");    //打开文件
    while(1)
    {
        fscanf(fp,"%d",&data);    //读取一个数据
        if(feof(fp))
        {
            break;
        }

        *(slip_window + (n+1)% count_window) = data;    //把data数据放到滑动窗口数组中

        if(data == 1)    //如果读到的是1 创建新桶
        {
            buc[count_bucket].size = 1;
            buc[count_bucket].time_stamp = n;

            if(count_bucket > 1) ////桶总数目大于2的时候才有可能合并
            {
                merge(buc,count_bucket);    //合并    
            }
            count_bucket++;   //创建新桶，所以桶数目加1

        }
        n++;    //时间戳加1
        if(n == t + 1)
        {
            break;
        }
    }
    printf("字符流个数：%d\n",n - 1);
    printf("桶数目:%d\n",count_bucket);    //桶总数
    fclose(fp);

    for (i = 0; i < count_bucket; i++)
    {
        printf("第%2d桶  桶大小:%5d   时间戳：%d\n",i,buc[i].size,buc[i].time_stamp);
    }

    estimate(buc,count_window,n-1);
    accurate(slip_window,count_window);

}

//合并
void merge(Bucket buc,int n)
{
    int i,j;
    for(i = n-1; i > 1; i--)
    {
        if( (buc[i].size == buc[i-1].size) && (buc[i-1].size == buc[i-2].size) )
        {
            buc[i - 2].size *= 2;
            buc[i - 2].time_stamp = buc[i - 1].time_stamp;
            buc[i - 1]= buc[i];
            for(j = i;j < count_bucket; j++)
            {
                buc[j] = buc[j+1];
            }
            count_bucket--;
        }
    }
}

//估算
void estimate(Bucket buc,int count_window,int n)
{
    int i;
    int sum = 0;
    for(i = count_bucket-1; i >= 0; i--)
    {
        if(buc[i].time_stamp >= n - count_window)
        {
            sum += buc[i].size;
        }
        else
        {
            sum -= (buc[i+1].size)/2;
            break;
        }
    }

    printf("估算滑动窗口内1_bit个数：%d\n",sum);
}


//精确计算窗口1个数
void accurate(int *slip_window,int count_window)
{
    int n = 0,i;
    for(i = 0; i < count_window; i++)
    {
        if(*(slip_window + i) == 1)
        {
            n++;
        }
    }
    printf("滑动窗口内1_bit精确个数为：%d\n",n);

}
