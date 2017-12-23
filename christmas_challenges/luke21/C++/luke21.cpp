# include <iostream>
# include <fstream>
# include <sstream>
# include <string>

using namespace std;

int main()
{

    ifstream myfile("testfile.txt", ios::in);
    if(myfile.is_open()){
        cout << "myfile is open" << endl;
        string line;
        while( getline(myfile,line) ){  //Reading file line by line
            string relation, person1, person2;
            istringstream words(line);  //Spliting string on whitespace.
            words >> relation;
            words >> person1;
            words >> person2;
        }
        myfile.close();
    }

    return 0;
}
