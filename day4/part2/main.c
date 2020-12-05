#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	//line from file
	char inputLine[100];
	//Is each passport valid? 
	int valid = 0;
	//substring from file
	char * token;
	//used to split token for atoi
	char toAtoi[4] = {'\0', '\0', '\0', '\0'};
	//bools don't exist lol 
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
			//if we're at a newline, check if the previous password was valid.
			if(byr == 1 && iyr == 1 && eyr == 1 && hgt == 1 && hcl == 1 && ecl == 1 && pid == 1){valid++;}
			//reset all feilds
			byr = 0;
			iyr = 0;
			eyr = 0;
			hgt = 0;
			hcl = 0;
			ecl = 0;
			pid = 0;
		}
		else{
			//split up the inputLine with space as delimiter
			token = strtok(inputLine, " ");
			//while token is valid
			while(token != NULL){
				switch(token[0]){ //this entire thing is a hack
					case 'b':
						//BYR
						//Shift the string up 4, removing 'byr:'
						token = token + 4;
						//copy four positions of the token into toAtoi
						//this removes trailing newLines and other garbage
						memcpy(toAtoi, token, 4);
						//convert toAtoi into birthYear
						int birthYear = atoi(toAtoi);
						//check if birthYear is valid
						if(birthYear >= 1920 && birthYear <= 2002){
							byr++;
						}
						//reset toAtoi so there's no trash in it later
						memset(&toAtoi[0], 0, sizeof(toAtoi));
						break;
					case 'c':
						//no need to do anything here!
						break;
					case 'i':
						//shift up our string 4, removing 'iyr:'
						token = token + 4;
						//copy four positions of the token into toAtoi
						//this removes trailing newLines and other garbage
						memcpy(toAtoi, token, 4);
						int issueYear = atoi(toAtoi);
						//check if iyr is valid
						if(issueYear >= 2010 && issueYear <= 2020){
							iyr++;
						}
						//reset toAtoi
						memset(&toAtoi[0], 0, sizeof(toAtoi));
						break;
					case 'e':
						//if second char is y, it must be an eyr
						if(token[1] == 'y'){
							//same story as iyr 
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
						//otherwise, it's an ecl
						else{
							token = token + 4;
							char eyeColor[3];
							//copy string into eyecolor. 
							//again, it removes trailing trash and newlines
							strncpy(eyeColor, token, 3);
							//call strstr to see if string matches.
							if(strstr("amb", eyeColor) != NULL || strstr("blu", eyeColor) != NULL || strstr("brn", eyeColor) != NULL || strstr("gry", eyeColor) != NULL || strstr("grn", eyeColor) != NULL || strstr("hzl", eyeColor) != NULL || strstr("oth", eyeColor) != NULL){
							ecl++;
							}
							break;
						}
					case 'h':
						//if second postition of token is a g, it must be hgt
						if(token[1] == 'g'){
							token = token + 4;
							//delimers for either inches or cm
							//const char delims[2] = {'i', 'c'};
							//temporary atoi char
							char toAtoiSmall[3] = {'\0', '\0', '\0'};
							//if third position is a digit, then the number is three wide
							if(token[2] >= '0' && token[2] <= '9'){
								//copy three characters from token
								memcpy(toAtoiSmall, token, 3);
								token += sizeof(toAtoiSmall);
							}
							//otherwise, it's only two chars.
							else{
								//copy two chars from token
								memcpy(toAtoiSmall, token, 2);
								token += sizeof(toAtoiSmall) - 1;
							}
							
							int height = atoi(toAtoiSmall);
							//if it's inches, figure out if it's the right size
							if(token[0] == 'i' && height >= 59 && height <= 76){
								hgt++;
							}
							//same thing, but for cm.
							else if(token[0] == 'c' && height >= 150 && height <= 193){
								hgt++;
							}
							break;
						}
						else{
							//let's say the string is valid
							int valid = 1;
							//throw out first 3 chars; "hcl:" 
							token = token + 4;
							//if there's no # up front, it's a write off
							if(token[0] != '#'){valid = 0;}
							//check each char to see if it's a letter or digit.
							for(int i = 1; i <= 6; i++){
								if(!(isalpha(token[i]) || isdigit(token[i]))){
									valid = 0;
								}
							}
							//if we're longer than we need to be, invalidate
							if(isalpha(token[7]) || isdigit(token[7])){valid = 0;}
							if(valid == 1){hcl++;}
							break;
						}
					case 'p':
						//shift up four, removing "pid:" 
						token = token + 4;
						int valid = 1;
						//go through each char, making sure it's a digit
						for(int i = 0; i <= 8; i++){
							if(!isdigit(token[i])){
								valid = 0;
							}
						}
						//if it's longer than it needs to be, invalidate
						if(isdigit(token[9])){valid = 0;}
						if(valid == 1){pid++;}
						break;
					default: 
						//if we don't mach any case
						printf("error \n");
					
				}
				//get the next token from our input string
				//this is literally how strtok does this
				token = strtok(NULL, " ");
			}
		}
        }
	//check last passport lol
	if(byr == 1 && iyr == 1 && eyr == 1 && hgt == 1 && hcl == 1 && ecl == 1 && pid == 1){valid++;}
	
	printf("valid passports: %d\n", valid);

	fclose(fp);
	return 0;
}
