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

int searchID(int ID[2000], int IDtoCheck){
	for(int i = 0; i <= 2000; i++){
		if(ID[i] == IDtoCheck){
			return 1;
		}
	}
	return 0;
}

int cmpFunc(const void * a, const void * b){
	return( *(int*)a - *(int*)b);
}

int findMissingID(int ID[2000]){
	for(int i = 0; i < 2000; i++){
		if(ID[i+1] == ID[i] + 2){
			printf("ID Found: %d\n", ID[i] + 1);
		}
	}
}

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	char fullID[10];
	//int maxFoundID = 0;
	int planeMap[127][7];
	//set entire array to 0
	memset(planeMap, 0, sizeof(int) * 127 * 7);
	int ID[2000] = { };
	int idRow = 0;
	
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

		ID[idRow] = findRow(rowChars) * 8 + findColumn(columnChars);
		idRow++;
		//struct Seat newSeat;

		//newSeat.row = findRow(rowChars);
		//newSeat.col = findColumn(columnChars);
		//newSeat.ID = newSeat.row * 8 + newSeat.col;

		//planeMap[newSeat.row][newSeat.col] = newSeat;

		planeMap[findRow(rowChars)][findColumn(columnChars)] = 1;
		
        }
	//printf("Maximum ID: %d\n", maxFoundID);
	for(int i=1; i <= 126; i++){
		for(int c = 0; c <= 7; c++){
			if(planeMap[i][c] ==0){
				//printf("empty seat: row %d col %d\n", i, c);
				int IDtoSearch = i * 8 + c;
				//printf("empty seat: row %d col %d id %d\n", i, c, IDtoSearch);
				
				if((searchID(ID, (IDtoSearch + 1))==1) && (searchID(ID, (IDtoSearch - 1))) == 1){
					printf("Match found! %d\n", IDtoSearch);
				}
				//if(planeMap[i+1][c] == 1 && planeMap[i-1][c] == 1){
					//printf("seat matching criteria: row %d col %d\n", i, c);
					
				//}
			}
		}
	}
	qsort(ID, 2000, sizeof(int), cmpFunc);
	findMissingID(ID);

	fclose(fp);
	return 0;
}
