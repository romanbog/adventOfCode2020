#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fp;
	fp = fopen("input.txt", "r");
	char inputLine[100];
	//is our passport valid?
	int valid = 0;
	char * token;
	//no bools lol
	int byr = 0;
	int iyr = 0;
	int eyr = 0;
	int hgt = 0;
	int hcl = 0;
	int ecl = 0;
	int pid = 0;
	
	//in each line of the file:
	while(fgets(inputLine, 100, fp)){
		//if our first char is a newline, we have a new passport
		if(inputLine[0] == '\n'){
			//check if the previous passport was valid
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
			//get a new substring, demilited by spaces
			token = strtok(inputLine, " ");
			while(token != NULL){
				//check the first char of our substring, and sort our logic from there.
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
						//there's two things that start with e.
						//eyr
						if(token[1] == 'y'){
							eyr++;
							break;
						}
						//ecl
						else{
							ecl++;
							break;
						}
					case 'h':
						//two things that start with h
						//hgt
						if(token[1] == 'g'){
							hgt++;
							break;
						}
						//hcl
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
				//get the next substring from inputLine
				//this is just how strtok works
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
