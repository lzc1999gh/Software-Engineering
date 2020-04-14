#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
//#include <stdbool.h>
int NodeNum = 0;            //ͳ�ƽ�����
typedef struct Node
{
    int data;
    struct Node* next;
}NODE, * PNODE;

//����һ����̬����������ͷָ��
PNODE CreatList()
{
    printf("����������������,��-1��������\n");
    PNODE head = (PNODE)malloc(sizeof(NODE));
    PNODE tail = head;
    int num = 0;
    int Flag = 1;
    scanf("%d", &num);
    //�������ݣ���0����
    while (num != -1)
    {
        PNODE pnew = (PNODE)malloc(sizeof(NODE));
        pnew->data = num;
        tail->next = pnew;
        tail = pnew;
        NodeNum++;
        scanf("%d", &num);
    }
    tail->next = NULL;
    return head;
}
//��������
void tarverse(PNODE head)
{
    PNODE phead = head->next;
    while (phead != NULL)
    {
        printf("%d ", phead->data);
        phead = phead->next;
    }
    printf("   ��ʱ����%d�����\n", NodeNum);
}
//�ж��Ƿ�Ϊ������
bool isEmpty(PNODE head)
{
    if (head->next == NULL)
    {
        printf("����Ϊ��\n");
        return true;
    }
    else
        return false;
}
//ɾ�����
void DelNode(PNODE head)
{
    int location = 0;
    printf("ɾ���ڼ�����㣿");
    scanf("%d", &location);
    PNODE p1 = head;
    PNODE p2 = p1->next;
    for (int i = 0; i < location - 1; i++)
    {
        p1 = p1->next;
        p2 = p2->next;
    }
    p1->next = p2->next;
    free(p2);
    p2 = NULL;
    NodeNum--;
}
//���ӽ��
void AddNode(PNODE head)
{
    PNODE p1 = head;
    PNODE p2 = p1->next;
    int location = 0;
    int newdata = 0;
    printf("����ڵڼ���λ�ã�");
    scanf("%d", &location);
    printf("�����½������:");
    scanf("%d", &newdata);
    PNODE pnew = (PNODE)malloc(sizeof(NODE));
    pnew->data = newdata;
    for (int i = 0; i < location - 1; i++)
    {
        p1 = p1->next;
        p2 = p2->next;
    }
    p1->next = pnew;
    pnew->next = p2;
    NodeNum++;
}
//�޸Ľ��
void AlterNode(PNODE head)
{
    PNODE p = head;
    int location = 0;
    int newdata = 0;
    printf("�޸ĵڼ�����㣿");
    scanf("%d", &location);
    printf("�����½������:");
    scanf("%d", &newdata);
    PNODE pnew = (PNODE)malloc(sizeof(NODE));
    pnew->data = newdata;
    for (int i = 0; i < location; i++)
    {
        p = p->next;
    }
    p->data = newdata;
}
int main()
{
    PNODE p = (PNODE)malloc(sizeof(NODE));
    p = CreatList();
    int operate_command;
    printf("��ǰ����Ϊ��\n");
    tarverse(p);
    int stop_mark = 1;
    //printf("��ѡ�������ʽ��\n���ӽ��������1\nɾ�����������2\n�޸Ľ��������3\n�˳�������0\n");
    while (stop_mark == 1)
    {
        printf("��ѡ�������ʽ��\n���ӽ��������1\nɾ�����������2\n�޸Ľ��������3\n�˳�������0\n");
        printf("�����룺");
        scanf("%d", &operate_command);
        if (operate_command == 1) {
            AddNode(p);
            tarverse(p);
        }
        else if (operate_command == 2)
        {
            DelNode(p);
            tarverse(p);
        }
        else if (operate_command == 3) 
        {
            AlterNode(p);
            tarverse(p);
        }
        else if (operate_command == 0)
        {
            printf("��������Ϊ��\n");
            tarverse(p);
            stop_mark = 0;
        }
    } 
    //system("pause");
    return 0;
}