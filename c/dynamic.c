/*
 * =====================================================================================
 *
 *       Filename:  dynamic_arr.c
 *
 *    Description:  数组版本
 *
 *        Version:  1.0
 *        Created:  2013年11月21日 14时27分20秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  ZHU XU (~_~), splk008@qq.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <stdio.h>

#define MAX 4

struct node {
	int a;
	int b;
	int locate; /*  记录着原始序列的位置信息 */
};

int max(int a, int b);

int main(int argc, char *argv[])
{
	struct node input[MAX];
	int num = MAX;    /* 用于读取用户输入,确定数组长度 */
	struct node temp;
	int i;
	int j;
	int area; /* 记录着要插入的位置信息 */
	int val;  /* 记录着当前的最小代价 */
	int val_old;
	int num_tmp;
	int min;

	printf("请输入作业：\n");
	for (i = 0; i < num; i++)
		scanf("%d %d %d\n",&input[i].a, &input[i].b, &input[i].locate);

	val = input[0].a + input[0].b;
	area = 0;

	for (i = 1; i < MAX; i++){
		val_old = val;
		if (input[i-1].b >= input[i].a){
			val += input[i].b;
		}else{
			val = val - input[i-1].b + input[i].a + input[i].b;
		}
		min = val;
		area = i;
		for (j = 0; j < i; j++){
			num_tmp = val_old;
			if (j == 0){
				/* 在头元素前插入 */
				num_tmp = num_tmp - input[0].a + input[i].a + max(input[i].b, input[0].a);
			}else{
				/* 在数组中间插入 */
				num_tmp = num_tmp - max(input[j-1].b, input[j].a) + max(input[i].a, input[j-1].b) + max(input[i].b, input[j].a);
			}
			if (num_tmp < min){
				min = num_tmp;
				area = j;
			}
		}
		val = min;

		/* 更改位置, 即将i移动到area之前 */
		temp = input[i];
		for (j = i; j > area; j--){
			input[j] = input[j-1];
		}
		input[j] = temp;
	}

	printf("具有最短时间的序列如下:\n");
	printf("a  b  locate\n");
	for (i = 0; i < MAX; ++i){
		printf("%d  %d  %d\n",input[i].a, input[i].b, input[i].locate);
	}

	return 0;
}

int max(int a, int b)
{
	if (a > b)
		return a;
	else
		return b;
}
