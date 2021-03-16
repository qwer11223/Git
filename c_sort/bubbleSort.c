#include <stdio.h>
#include <stdlib.h>
#define N 1000
void bubbleSort(int *);
void showArr(const int *, int);

int main(void)
{
    int num[N];

    for (int i = 0; i < N; i++)
        num[i] = rand() % N;

    puts("arr:");
    showArr(num, N);

    bubbleSort(num);

    puts("sort:");
    showArr(num, N);

    while (getchar() != '\n')
        ;
    getchar();

    return 0;
}

void showArr(const int *a, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%4d ", a[i]);
        if ((i + 1) % 10 == 0)
            puts("");
    }
}

void bubbleSort(int *a)
{
    int tmp, c = 0;

    for (int i=0; i < N - 1; i++)
        for (int j=0; j < N - 1 - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
                printf("step: %d\n", ++c);
            }
        }
}