#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 1000//采样点的个数
#define M 5//分组

#define SIZE 10000

typedef struct
{
    int element;
    int count;
}ATTRIBUTE;


int main()
{
    ATTRIBUTE attr[100000];
    int secmom=0;//真实二阶矩
    int data;//接收读取之后的值
    int i=0,j,k;//循环控制变量
    int count_tmp=0;//临时计数变量
    //int n=5;//采样点的个数
    double secmom_estima=0;
    ATTRIBUTE sample[10000];
    int tmp;
    int a[10000];
    int loc[N];//采样位置保存在数组里
    int sample_group[M][N];
    //FILE *fp =fopen("./stream_for_ams.txt","r");

    FILE *fp =fopen("stream_sample_ams.txt","r");

    srand(time(0));
    for(j=0;j<N;j++)
    {
        loc[j]=rand()%SIZE;//获取随机采样位置
    }

    for(j=0;j<N;j++)//随机位置排序
    {
        for(k=j+1;k<N;k++)
        {
            if(loc[j] > loc[k])
            {
                tmp = loc[k];
                loc[k]=loc[j];
                loc[j]=tmp;
            }
        }
    }

    if(fp == NULL)//文件读取失败
    {
        printf("file can't open!\n");
        exit(0);
    }
    while(!feof(fp))
    {
        fscanf(fp,"%d",&data);
        a[i]=data;//存数据
        /***************采样*****************/
        for(j=0;j<N;j++)
        {
            if(loc[j] == i)
            {
                sample[j].element=data;
                sample[j].count=0;
            }
            if(sample[j].element == data)
            {
                sample[j].count+=1;
            }
        }

        /*****************真实***********************/
        for(j=0;j<count_tmp;j++)
        {
            if(attr[j].element == data)//如果该数据被存过则count+1
            {
                attr[j].count +=1;
                break;//扫描比对成功退出循环
            }
        }
        if( j == count_tmp)//如果没有该数据第一次出现
        {
            attr[count_tmp].element=data;//记录
            attr[count_tmp].count=1;
            count_tmp++;//记录第一次出现的数
        }
        printf("%.2lf%%\r", i * 100.0/ SIZE);
        i++;
    }

    /******************组合估计二阶矩***********************/
    for(i=0;i<M;i++)//分组M
    {
        for(j=0;j<N;j++)//每组N个随机位置
        {
            loc[j]=rand()%SIZE;//获取随机采样位置
        }
        for(j=0;j<N;j++)//随机位置排序
        {
            for(k=j+1;k<N;k++)
            {
                if(loc[j] > loc[k])
                {
                    tmp = loc[k];
                    loc[k]=loc[j];
                    loc[j]=tmp;
                }
            }
        }
        for(j=0;j<N;j++)
        {
            if(loc[j] == i)
            {
                sample_group[i][j]=
                sample[j].count=0;
            }
            if(sample[j].element == data)
            {
                sample[j].count+=1;
            }
        }

    }

    /************估计无组合估计二阶矩**********************/
    for(j=0;j<N;j++)
    {
        secmom_estima+=SIZE*(2.0*sample[j].count-1);
    }
    printf("无组合估计二阶矩:%.2lf\n",secmom_estima/N);

    /***********真实二阶矩*************/
    for(j=0;j<count_tmp;j++)
    {
        //printf("%d\t%d\n",attr[j].element,attr[j].count);
        secmom+=attr[j].count*attr[j].count;
    }
    printf("独立数%d\n",count_tmp);
    printf("真实二阶矩为:%d\n",secmom);

    system("pause");
    return 0;
}