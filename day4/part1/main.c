#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	char inputLine[100];
	int valid = 0;
	char * token;
	
	int byr = 0;
	int iyr = 0;
	int eyr = 0;
	int hgt = 0;
	int hcl = 0;
	int ecl = 0;
	int pid = 0;
	
	//in each line of the file:
	while(fgets(inputLine, 100, fp)){
		if(inputLine[0] == '\n'){
			if(byr == 1 && iyr == 1 && eyr == 1 && hgt == 1 && hcl == 1 && ecl == 1 && pid == 1){valid++;}
			//reset all feilds
			//printf("new pass ============================\n");
			byr = 0;
			iyr = 0;
			eyr = 0;
			hgt = 0;
			hcl = 0;
			ecl = 0;
			pid = 0;
		}
		else{
			token = strtok(inputLine, " ");
			while(token != NULL){
				//printf("%s\n", token);
				//do stuff
				//char firstThree[3];
				//memcpy(firstThree, &token[0], 3);
				//printf("%s\n", firstThree);
				switch(token[0]){ //this is a hack
					case 'b':
						byr++;
						break;
					case 'c':
						break;
					case 'i':
						iyr++;
						break;
					case 'e':
						if(token[1] == 'y'){
							eyr++;
							break;
						}
						else{
							ecl++;
							break;
						}
					case 'h':
						if(token[1] == 'g'){
							hgt++;
							break;
						}
						else{
							hcl++;
							break;
						}
					case 'p':
						pid++;
						break;
					default: 
						printf("error \n");
					
				}
				token = strtok(NULL, " ");
			}
		}
		//for(int i; i < 100; i++){
			//inputLine[i] = '\0';
		//}
        }
	//check last passport lol
			if(byr == 1 && iyr == 1 && eyr == 1 && hgt == 1 && hcl == 1 && ecl == 1 && pid == 1){valid++;}
			//reset all feilds
			//printf("new pass ============================\n");
			byr = 0;
			iyr = 0;
			eyr = 0;
			hgt = 0;
			hcl = 0;
			ecl = 0;
			pid = 0;
		
	printf("valid passports: %d\n", valid);

	fclose(fp);
	return 0;
}
