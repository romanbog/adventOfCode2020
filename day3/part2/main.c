#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	int encountered = 0;
	int currentSquare = 0;
	char treeLine[31];
	long long int totalMultiplied = 1;
	
	//correctly increment toMove 
	for(int toMove = 1; toMove <= 7; toMove = toMove + 2){
		fp = fopen("input.txt", "r");
		while(fscanf(fp, "%s\n", treeLine)!= EOF){
			if(treeLine[currentSquare] == '#'){encountered++;}
			currentSquare += toMove;
			//if currentSquare is out of bounds, subtract it back. 
			//This looks funky, but it's actually correct. I hate off by 1 errors! 
			if(currentSquare > 30){
				currentSquare = currentSquare - 31;
			}
        	}
		//sum totals, clean up for next run
		totalMultiplied *= encountered;
		encountered = 0;
		currentSquare = 0;
		fclose(fp);
	}

	//clean up for final run
	int tempCounter = 0;
	currentSquare = 0;
	fp = fopen("input.txt", "r");

	while(fscanf(fp, "%s\n", treeLine)!= EOF){
		//only calculate if we're on an odd line.
        	if(tempCounter % 2 == 0){
			if(treeLine[currentSquare] == '#'){encountered++;}
			currentSquare++;
			if(currentSquare > 30){
				currentSquare -= 31;
			}
		}
		tempCounter++;
        }
	totalMultiplied *= encountered;

	printf("total is: %lld\n", totalMultiplied);

	fclose(fp);
	return 0;
}
