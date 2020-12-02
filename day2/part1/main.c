#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <mcheck.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	//int *array;
	int total = 0;
	int tempInt;
	int fileLineCount = 0;
	char c;
	//mtrace();
/*
	while(!feof(fp)){
		c = fgetc(fp);
		if(c == '\n'){fileLineCount++;}
	}
	printf("%d\n", fileLineCount);
	fclose(fp);
	fp = fopen("input.txt", "r");
*/
	//allocate memory
	//array = (int*)malloc(fileLineCount * sizeof(int));
	/*
	while(fscanf(fp, "%d\n", &tempInt) != EOF){
		array[i] = tempInt;
		i++;
	}
	*/
	int min;
	int max;
	char toFind;
	//string pass; 
	//char pass[20];
	char pass[1000];
	while(fscanf(fp, "%d-%d %c: %s\n", &min, &max, &toFind, pass)!= EOF){
		int foundChars = 0;
		for(int i = 0; i < 1000; i++){
			if(pass[i] == toFind){
				foundChars++;
			}
		}
		if(foundChars <= max && foundChars >= min){
			total++;
		}
		for(int i = 0; i < 1000; i++){
			pass[i] = '\0';
		}

	}

	printf("%d\n", total);
	//free(array);

	//muntrace();
	return 0;
}
