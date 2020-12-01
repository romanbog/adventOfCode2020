#include <stdio.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	int array[1000] = {0};
	int i = 0;
	int tempInt;
	while(fscanf(fp, "%d\n", &tempInt) != EOF){
		array[i] = tempInt;
		i++;
	}

	for(int j = 0; j < 300; j++){
		printf("%d\n", array[j]);
	}
	
	for(int j = 0; j < 300; j++){
		for(int k = j; k < 300; k++){
			if(array[j] + array[k] == 2020){
				printf("Match Found! %d and %d.\n", array[j], array[k]);
				printf("Multpilying together... %d\n", array[j] * array[k]);
			}
		}
	}
	

}
