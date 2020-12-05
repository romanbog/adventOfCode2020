#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	char inputLine[100];
	int valid = 0;
	char * token;
	char toAtoi[4] = {'\0', '\0', '\0', '\0'};
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
			printf("new pass ============================\n");
			printf("byr%d\niyr%d\neyr%d\nhgt%d\nhcl%d\necl%d\npid%d\n", byr, iyr, eyr, hgt, hcl, ecl, pid);
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
				printf("%s", token);
				//printf("%s\n", token);
				//do stuff
				//char firstThree[3];
				//memcpy(firstThree, &token[0], 3);
				//printf("%s\n", firstThree);
				switch(token[0]){ //this is a hack
					case 'b':
						token = token + 4;
						memcpy(toAtoi, token, 4);
						int birthYear = atoi(toAtoi);
						if(birthYear >= 1920 && birthYear <= 2002){
							byr++;
						}
						//toAtoi = {'\0', '\0', '\0', '\0'};
						memset(&toAtoi[0], 0, sizeof(toAtoi));
						token = " ";
						break;
					case 'c':
						break;
					case 'i':
						token = token + 4;
						memcpy(toAtoi, token, 4);
						int issueYear = atoi(toAtoi);
						if(issueYear >= 2010 && issueYear <= 2020){
							iyr++;
						}
						//toAtoi = {'\0', '\0', '\0', '\0'};
						memset(&toAtoi[0], 0, sizeof(toAtoi));
						break;
					case 'e':
						if(token[1] == 'y'){
							token = token + 4;
							memcpy(toAtoi, token, 4);
							int expYear = atoi(toAtoi);
							if(expYear >= 2020 && expYear <= 2030){
								eyr++;
							}
							//toAtoi = {'\0', '\0', '\0', '\0'};
							memset(&toAtoi[0], 0, sizeof(toAtoi));
							break;
						}
						else{
							token = token + 4;
							char eyeColor[3];
							strncpy(eyeColor, token, 3);
							if(strstr("amb", eyeColor) != NULL || strstr("blu", eyeColor) != NULL || strstr("brn", eyeColor) != NULL || strstr("gry", eyeColor) != NULL || strstr("grn", eyeColor) != NULL || strstr("hzl", eyeColor) != NULL || strstr("oth", eyeColor) != NULL){
							ecl++;
							}
							//token = "notnull";
							break;
						}
					case 'h':
						if(token[1] == 'g'){
							token = token + 4;
							const char delims[2] = {'i', 'c'};
							char toAtoiSmall[3] = {'\0', '\0', '\0'};
							if(token[2] >= '0' && token[2] <= '9'){
								memcpy(toAtoiSmall, token, 3);
								token += sizeof(toAtoiSmall);
							}
							else{
								memcpy(toAtoiSmall, token, 2);
								token += sizeof(toAtoiSmall) - 1;
							}
							
							int height = atoi(toAtoiSmall);
							if(token[0] == 'i' && height >= 59 && height <= 76){
								hgt++;
							}
							else if(token[0] == 'c' && height >= 150 && height <= 193){
								hgt++;
							}
							break;
						}
						else{
							int valid = 1;
							token = token + 4;
							if(token[0] != '#'){valid = 0;}
							for(int i = 1; i <= 6; i++){
								//if(!(token[i] >= 'Z' && token[i] <= 'A' || token[i] >= 'z' && token[i] <= 'a' || token[i] >= '0' && token[i] <= '9')){
								if(!(isalpha(token[i]) || isdigit(token[i]))){
									valid = 0;
								}
							}
							//if((token[7] >= 'Z' && token[7] <= 'A' || token[7] >= 'z' && token[7] <= 'a' || token[7] >= '0' && token[7] <= '9')){valid = 0;}
							if(isalpha(token[7]) || isdigit(token[7])){valid = 0;}
							if(valid == 1){hcl++;}
							break;
						}
					case 'p':
						token = token + 4;
						int valid = 1;
						for(int i = 0; i <= 8; i++){
							if(!isdigit(token[i])){
								valid = 0;
							}
						}
						if(isdigit(token[9])){valid = 0;}
						if(valid == 1){pid++;}
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
			if(byr == 1 && iyr == 1 && eyr == 1 && hgt == 1 && hcl == 1 && ecl == 1 && pid == 1){valid++; printf("Valid!\n");}
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
