#include<stdio.h>
int main()
{
    if(1)
    {
        printf("Yes");
    }

    int a,b;
    while(scanf("%d%d",&a,&b)!=-1)
        printf("%d\n",a+b);

}
