#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	int encountered = 0;
	int currentSquare = 0;
	char treeLine[31];
	
	//in each line of the file:
	while(fscanf(fp, "%s\n", treeLine)!= EOF){
		if(treeLine[currentSquare] == '#'){encountered++;}
		//shift over three
		currentSquare += 3;
		//if currentSquare is out of bounds, subtract it back.
		if(currentSquare > 30){
			currentSquare -= 31;
		}
        }
	printf("total collisions: %d\n", encountered);

	fclose(fp);
	return 0;
}
