
#include <stdio.h>
double x(int n) {
	if (n < 0 || n > 5) return 0;
	else if (n < 4) return n + 1;
	else return 6 - n;
}

double y(int n) {
	if (n < 0) return 0;
	else return x(n) + x(n-2) - 0.5 * y(n-1);
}

int main() {
	FILE *fp = fopen("filter_output.dat", "w");
	for (int i = 0; i < 20; i++) {
		fprintf(fp, "%lf\n", y(i));
	}
	fclose(fp);
	return 0;
}
