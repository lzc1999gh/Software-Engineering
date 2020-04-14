#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
//#include <stdbool.h>
int NodeNum = 0;            //统计结点个数
typedef struct Node
{
    int data;
    struct Node* next;
}NODE, * PNODE;

//创建一个动态链表并返回其头指针
PNODE CreatList()
{
    printf("创建链表，输入数据,以-1结束输入\n");
    PNODE head = (PNODE)malloc(sizeof(NODE));
    PNODE tail = head;
    int num = 0;
    int Flag = 1;
    scanf("%d", &num);
    //输入数据，以0结束
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
//遍历链表
void tarverse(PNODE head)
{
    PNODE phead = head->next;
    while (phead != NULL)
    {
        printf("%d ", phead->data);
        phead = phead->next;
    }
    printf("   此时共有%d个结点\n", NodeNum);
}
//判断是否为空链表
bool isEmpty(PNODE head)
{
    if (head->next == NULL)
    {
        printf("链表为空\n");
        return true;
    }
    else
        return false;
}
//删除结点
void DelNode(PNODE head)
{
    int location = 0;
    printf("删除第几个结点？");
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
//增加结点
void AddNode(PNODE head)
{
    PNODE p1 = head;
    PNODE p2 = p1->next;
    int location = 0;
    int newdata = 0;
    printf("添加在第几个位置？");
    scanf("%d", &location);
    printf("输入新结点数据:");
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
//修改结点
void AlterNode(PNODE head)
{
    PNODE p = head;
    int location = 0;
    int newdata = 0;
    printf("修改第几个结点？");
    scanf("%d", &location);
    printf("输入新结点数据:");
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
    printf("当前链表为：\n");
    tarverse(p);
    int stop_mark = 1;
    //printf("请选择操作方式：\n增加结点请输入1\n删除结点请输入2\n修改结点请输入3\n退出请输入0\n");
    while (stop_mark == 1)
    {
        printf("请选择操作方式：\n增加结点请输入1\n删除结点请输入2\n修改结点请输入3\n退出请输入0\n");
        printf("请输入：");
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
            printf("最终链表为：\n");
            tarverse(p);
            stop_mark = 0;
        }
    } 
    //system("pause");
    return 0;
}