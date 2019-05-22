#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 1000//������ĸ���
#define M 5//����

#define SIZE 10000

typedef struct
{
    int element;
    int count;
}ATTRIBUTE;


int main()
{
    ATTRIBUTE attr[100000];
    int secmom=0;//��ʵ���׾�
    int data;//���ն�ȡ֮���ֵ
    int i=0,j,k;//ѭ�����Ʊ���
    int count_tmp=0;//��ʱ��������
    //int n=5;//������ĸ���
    double secmom_estima=0;
    ATTRIBUTE sample[10000];
    int tmp;
    int a[10000];
    int loc[N];//����λ�ñ�����������
    int sample_group[M][N];
    //FILE *fp =fopen("./stream_for_ams.txt","r");

    FILE *fp =fopen("stream_sample_ams.txt","r");

    srand(time(0));
    for(j=0;j<N;j++)
    {
        loc[j]=rand()%SIZE;//��ȡ�������λ��
    }

    for(j=0;j<N;j++)//���λ������
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

    if(fp == NULL)//�ļ���ȡʧ��
    {
        printf("file can't open!\n");
        exit(0);
    }
    while(!feof(fp))
    {
        fscanf(fp,"%d",&data);
        a[i]=data;//������
        /***************����*****************/
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

        /*****************��ʵ***********************/
        for(j=0;j<count_tmp;j++)
        {
            if(attr[j].element == data)//��������ݱ������count+1
            {
                attr[j].count +=1;
                break;//ɨ��ȶԳɹ��˳�ѭ��
            }
        }
        if( j == count_tmp)//���û�и����ݵ�һ�γ���
        {
            attr[count_tmp].element=data;//��¼
            attr[count_tmp].count=1;
            count_tmp++;//��¼��һ�γ��ֵ���
        }
        printf("%.2lf%%\r", i * 100.0/ SIZE);
        i++;
    }

    /******************��Ϲ��ƶ��׾�***********************/
    for(i=0;i<M;i++)//����M
    {
        for(j=0;j<N;j++)//ÿ��N�����λ��
        {
            loc[j]=rand()%SIZE;//��ȡ�������λ��
        }
        for(j=0;j<N;j++)//���λ������
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

    /************��������Ϲ��ƶ��׾�**********************/
    for(j=0;j<N;j++)
    {
        secmom_estima+=SIZE*(2.0*sample[j].count-1);
    }
    printf("����Ϲ��ƶ��׾�:%.2lf\n",secmom_estima/N);

    /***********��ʵ���׾�*************/
    for(j=0;j<count_tmp;j++)
    {
        //printf("%d\t%d\n",attr[j].element,attr[j].count);
        secmom+=attr[j].count*attr[j].count;
    }
    printf("������%d\n",count_tmp);
    printf("��ʵ���׾�Ϊ:%d\n",secmom);

    system("pause");
    return 0;
}