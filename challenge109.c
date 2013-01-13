#include <stdio.h>

int dig(char *str);

int dig(char *str){
	char *s = str;
	while(*s){
		if(!isdigit(*s)){
			return 1;
		}
		s++;
	}
	return 0;
}

int main(int argc, char** argv){
	char* str1 = "hello";
	char* str2 = "5";
	char* str3 = "5.5";
	
	printf("%d\n", dig(str1));
	printf("%d\n", dig(str2));
	printf("%d\n", dig(str3));
	
	return 0;
}