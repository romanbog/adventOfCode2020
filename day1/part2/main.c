#include <stdio.h>
#include <stdlib.h>
//#include <mcheck.h> //memory debugging

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	int *array;
	int i = 0;
	int tempInt;
	int fileLineCount = 0;
	char c;
	//mtrace(); //memory debugging

	//count number of lines in input.txt
	while(!feof(fp)){
		c = fgetc(fp);
		if(c == '\n'){fileLineCount++;}
	}
	printf("%d\n", fileLineCount);
	fclose(fp);
	//re-open input
	fp = fopen("input.txt", "r");

	array = (int*)malloc(fileLineCount * sizeof(int));
	//load input into array
	while(fscanf(fp, "%d\n", &tempInt) != EOF){
		array[i] = tempInt;
		i++;
	}

	//prints array, for testing
	/*
	for(int j = 0; j < fileLineCount; j++){
		printf("%d\n", array[j]);
	}
	*/
	for(int j = 0; j < fileLineCount; j++){
		for(int k = j; k < fileLineCount; k++){
			for(int m = k; m < fileLineCount; m++){
				if(array[j] + array[k] + array[m] == 2020){
					printf("Match Found! %d, %d, and %d.\n", array[j], array[k], array[m]);
					printf("Multpilying together... %d\n", array[j] * array[k] * array[m]);
				}
			}
		}
	}
	//free allocated memory
	free(array);

	//muntrace();//memory debugging
	return 0;
}
