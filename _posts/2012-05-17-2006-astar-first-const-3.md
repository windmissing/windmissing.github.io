变态的比赛规则 
为了促进各部门员工的交流，百度 (baidu) 举办了一场全公司范围内的 " 拳皇友谊赛 " ，负责组织这场比赛的是百度的超级 " 拳皇 " 迷 W.Z. W.Z 不想用传统的淘汰赛或者循环赛的方式，而是自己制定了一个比赛规则。 
由于一些员工（比如同部门或者相临部门员工）平时接触的机会比较多，为了促进不同部门之间的交流， W.Z 希望员工自己组成不同组。不同组之间的每两个人都会进行一场友谊赛而同一组内的人则之间不会打任何比赛。 
比如 4 个人，编号为 1--4, 如果分为两个组并且 1,2 一个组， 3 ， 4 一个组，那么一共需要打四场比赛： 1 vs 3,1 vs 4,2 vs 3,2 vs 4. 而如果是 1,2,3 一组， 4 单独一组，那么一共需要打三场比赛 : 1 vs 4,2 vs 4,3 vs 4. 
很快 W.Z 意识到，这样的比赛规则可能会让比赛的场数非常多。 W.Z 想知道如果有 N 个人 , 通过上面这种比赛规则，总比赛场数有可能为 K 场吗？比如 3 个人，如果只分到一组则不需要比赛，如果分到两组则需要 2 场比赛 , 如果分为三组则需要 3 场比赛。但是无论怎么分都不可能只需要 1 场比赛。 
相信作为编程高手的你一定知道该怎么回答这个问题了吧？ 那么现在请你帮助 W.Z 吧。 
输入 
每行为一组数据，包含两个数字 N, K 。 (0<N<=500, K>=0) 
输出 
对输入的 N,K 如果 N 个员工通过一定的分组方式可能会一共需要 K 场比赛，则输出 "YES", 否则输出 "NO", 每组数据占一行。 
所有的输入输出均为标准输入输出。 
例子 
输入文件 : 
2 0 
2 1 
3 1 
3 2 
输出 : 
YES 
YES 
NO 
YES 

my answer：
还是DFS，一开始题目看错了，以为只分两组，用数学方法就可以了
分任意个组（最少一组），每组人数任意（最少一人）。
用DFS解，带一点点算不上剪枝的剪枝
暂时没想到更好的算法
#include <iostream>
#include <cmath>
using namespace std;

int n, k;
int ans[55];
bool flag;
void dfs(int start, int sum, int left, int ceil);
int main()
{
	int i;
	while(cin>>n>>k)
	{
		if(k == 0)
		{
			cout<<"YES"<<endl;
			continue;
		}
		flag = 0;
		dfs(1, 0, n, 0);
		if(flag)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}

void dfs(int start, int sum, int left, int ceil)
{
	if(sum > k)return;
	if(left == 0 && sum == k)
		flag = 1;
	int i, j;
	for(i = start; i <= left; i++)
	{
		if(flag)return;
		int temp = 0;
		for(j = 0; j < ceil; j++)
			temp = temp + ans[j] * i;
		ans[ceil]  = i;
		dfs(i, sum + temp, left - i, ceil + 1);
	}
	return;
}


