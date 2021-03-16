#include <stdio.h>
#include <stdlib.h>
#define N 1000
void qucikSort(int *, int, int);
void showArr(const int *, int);

int main(void)
{
    int num[N];

    for (int i = 0; i < N; i++)
        num[i] = rand() % N;

    puts("arr:");
    showArr(num, N);

    qucikSort(num, 0, N - 1);

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

void qucikSort(int *a, int low, int high)
{
    if (low < high)
    {
        int pivot = a[low];
        int i = low;
        int j = high;
        static int c = 0;

        while (i < j)
        {
            while (i < j && a[j] >= pivot)
                j--;
            if (i < j)
                a[i++] = a[j];

            while (i < j && a[i] < pivot)
                i++;
            if (i < j)
                a[j--] = a[i];

            printf("step: %d\n", ++c);
        }

        a[i] = pivot;

        qucikSort(a, low, i - 1);
        qucikSort(a, i + 1, high);
    }
}