#include <stdio.h>
#include <omp.h>
int main() {
	int y = 0;
	int x = 3;
	#pragma omp parallel 
	{
		while (x >0) {
			y = y+1;
			x = x-1;
		}
	}
	printf("%d", x)
}
