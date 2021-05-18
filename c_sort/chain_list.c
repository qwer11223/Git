#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int num;
	struct node *next;
} Node;

Node *create(int data)
{
	Node *p;
	p = (Node *)malloc(sizeof(Node));
	if (p == NULL)
		exit(-1);
	p->num = data;
	p->next = NULL;
	return p;
}

void show(Node *head)
{
	Node *p = head;
	int flag = 1;
	while (p->next != NULL || flag)
	{
		if (p->next == NULL)
		{
			printf("%d", p->num);
			flag = 0;
		}
		else
		{
			printf("%d -> ", p->num);
			p = p->next;
		}
	}
}

int main(void)
{
	Node *head, *p1, *p2;

	for (int i = 0; i < 5; i++)
	{
		p2 = create(i);

		if (i == 0)
			head = p1 = p2;
		else
		{
			p1->next = p2;
			p1 = p2;
		}
	}
	show(head);
	setbuf(stdin, NULL);
	getchar();
	return 0;
}
