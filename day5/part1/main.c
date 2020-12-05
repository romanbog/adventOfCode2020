#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h> 

int findRow(char rowInput[7]){
	//printf("%s\n", rowInput);
	int rowMin = 0;
	int rowMax = 127;
	
	for(int i = 0; i <= 7; i++){
		if(rowInput[i] == 'F'){
			rowMax = floor((double)rowMax - (((double)rowMax - rowMin) / 2));
		}
		else if(rowInput[i] == 'B'){
			rowMin = ceil((double)rowMin + (((double)rowMax - rowMin) /2));
		}
	}
	return rowMax;
}


int findColumn(char columnInput[3]){
	//printf("%s\n", columnInput);
	int columnMin = 0;
	int columnMax = 7;
	
	for(int i=0; i<=3; i++){
		if(columnInput[i] == 'L'){
			columnMax = floor((double)columnMax - (((double)columnMax - columnMin) / 2));
		}
		else if(columnInput[i] == 'R'){
			columnMin = ceil((double)columnMin + (((double)columnMax - columnMin) / 2));
		}
	}
	return columnMax;
}

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	char fullID[10];
	int maxFoundID = 0;
	
	//in each line of the file:
	while(fscanf(fp, "%s\n", fullID)!= EOF){
		//printf("%s\n", fullID);
		//set up our input strings
		char rowChars[7];
		strncpy(rowChars, fullID, 7);
		rowChars[7] = 0;
		//printf("%s", rowChars);
		//printf("%d", findRow(rowChars));
		char columnChars[3];
		strncpy(columnChars, &fullID[7], 3);
		columnChars[3] = 0;
		//printf("%d\n", findColumn(columnChars));
		int ID = findRow(rowChars) * 8 + findColumn(columnChars);
		if(maxFoundID < ID){
			maxFoundID = ID;
		}
		
        }
	printf("Maximum ID: %d\n", maxFoundID);

	fclose(fp);
	return 0;
}
