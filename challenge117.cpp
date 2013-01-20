#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main(int argc, char** argv){
	ifstream f(argv[1]);
	int c, index = 0, row = 0;
	
	if (!f.is_open()){
		cout << "Invalid file" << endl;
	}
	else{
		c = f.get();
		while(!f.eof()){
			if(index % 16 == 0){
				cout << endl;
				cout << hex << setfill('0') << setw(8) << row++ << "\t";
			}
			cout << hex << setfill('0') << setw(2) << c << " ";
			c = f.get();
			index++;
		}
		cout << endl;
		f.close();
	}
	return 0;
}