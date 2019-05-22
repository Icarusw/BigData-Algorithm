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
    int data;    //����������
    int n = 1;    //ʱ���
    int t;    //��Ҫ���������ʱ��
    int i;

    Bucket buc  = (Bucket)malloc(50 * sizeof(BucketNode));    //Ͱ_�ṹ��ָ������

    int count_window;    //�������ڴ�С
    int *slip_window;    //������������
    FILE *fp;

    printf("�����뻬�����ڴ�С��\n");
    scanf("%d",&count_window);    //���뻬�����ڴ�С
    slip_window = (int *)malloc(count_window * sizeof(int));    //���������������ռ�

    printf("������ʱ�̣�\n");
    scanf("%d",&t);

    fp = fopen("01stream.txt","r");    //���ļ�
    while(1)
    {
        fscanf(fp,"%d",&data);    //��ȡһ������
        if(feof(fp))
        {
            break;
        }

        *(slip_window + (n+1)% count_window) = data;    //��data���ݷŵ���������������

        if(data == 1)    //�����������1 ������Ͱ
        {
            buc[count_bucket].size = 1;
            buc[count_bucket].time_stamp = n;

            if(count_bucket > 1) ////Ͱ����Ŀ����2��ʱ����п��ܺϲ�
            {
                merge(buc,count_bucket);    //�ϲ�    
            }
            count_bucket++;   //������Ͱ������Ͱ��Ŀ��1

        }
        n++;    //ʱ�����1
        if(n == t + 1)
        {
            break;
        }
    }
    printf("�ַ���������%d\n",n - 1);
    printf("Ͱ��Ŀ:%d\n",count_bucket);    //Ͱ����
    fclose(fp);

    for (i = 0; i < count_bucket; i++)
    {
        printf("��%2dͰ  Ͱ��С:%5d   ʱ�����%d\n",i,buc[i].size,buc[i].time_stamp);
    }

    estimate(buc,count_window,n-1);
    accurate(slip_window,count_window);

}

//�ϲ�
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

//����
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

    printf("���㻬��������1_bit������%d\n",sum);
}


//��ȷ���㴰��1����
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
    printf("����������1_bit��ȷ����Ϊ��%d\n",n);

}
