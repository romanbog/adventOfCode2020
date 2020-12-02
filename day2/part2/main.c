#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	int total = 0;
	int min;
	int max;
	char toFind;
	char pass[1000];

	while(fscanf(fp, "%d-%d %c: %s\n", &min, &max, &toFind, pass)!= EOF){
		int foundChars = 0;
		//look at pass[min] and pass[max], determine if they contain the toFind char.
		//array index starts at 1, so we have to subtract min and max.
		if(pass[min-1] == toFind){foundChars++;}
		if(pass[max-1] == toFind){foundChars++;}
		//increment total only if there is 1 foundChar
		if(foundChars == 1){total++;}
		
		//reset string to null
		for(int i = 0; i < 1000; i++){
			pass[i] = '\0';
		}
	}
	
	//display result
	printf("%d\n", total);

	fclose(fp);
	return 0;
}
