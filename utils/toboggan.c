#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int toboggan(int moveHorizontal, int moveVertical){
	FILE *fp;
	int encountered = 0;
	int currentSquare = 0;
	char treeLine[31];
	fp = fopen("input.txt", "r");
	int tempCounter = 0;

	while(fscanf(fp, "%s\n", treeLine)!= EOF){
		//only calculate if we're on a moveVertical line.
        	if(tempCounter % moveVertical == 0){
			if(treeLine[currentSquare] == '#'){encountered++;}
			currentSquare += moveHorizontal;
			if(currentSquare > 30){
				currentSquare -= 31;
			}
		}
		tempCounter++;
        }

	fclose(fp);
	return encountered;
}
