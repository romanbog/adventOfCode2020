#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	int total = 0;
	char c;
	int min;
	int max;
	char toFind;
	char pass[1000];

	while(fscanf(fp, "%d-%d %c: %s\n", &min, &max, &toFind, pass)!= EOF){
		int foundChars = 0;
		//parse pass string, looing for toFind chars
		for(int i = 0; i < 1000; i++){
			if(pass[i] == toFind){foundChars++;}
		}
		//determine foundChars is valid, increment total
		if(foundChars <= max && foundChars >= min){total++;}
		//reset string to all null chars
		for(int i = 0; i < 1000; i++){pass[i] = '\0';}

	}

	//display result
	printf("%d\n", total);

	fclose(fp);
	return 0;
}
