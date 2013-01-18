#include <stdio.h>

int main(int argc, char** argv){
	FILE *f;
	int c, index = 0, row = 0;
	f = fopen(argv[1], "r");
	
	//if the file doesn't exist
	if (f == NULL){
		printf("Invalid file\n");
	}
	else{
		//get the first char
		c = fgetc(f);
		while(c != EOF){
			//if it's time to move to the next line
			if(index % 16 == 0){
				printf("\n");
				//prints row number with formatting
				printf("%08x\t", row++);
			}
			//prints hex value with formatting
			printf("%02x ", c);
			//gets next char
			c = fgetc(f);
			index++;
		}
		printf("\n");
		
		//cleanup
		fclose(f);
	}
	
	return 0;
}