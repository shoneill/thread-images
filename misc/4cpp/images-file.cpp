#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

//Global Constants
string IMG_MARKER = "href=\"//i.4cdn.org/";
string URL_START  = "\"//";

ifstream instream;
ofstream outstream;

//------------------------------------------------------------------------


//Extracts the URL from an inputted string
string extractURL(string input);
//Checks for duplicate URLs
bool isDupe(string input, vector<string> &urls);

void openFile(char *filename);


//------------------------------------------------------------------------
int main(int argc, char** argv)
{
    
    string str;
    vector<string> urls;

    instream.open(argv[1]);
    outstream.open(argv[2]);


    if (instream.fail()){
          cout << "failed to open file" << endl;
          exit(1);
    }
  
    while (instream.good()) {
        instream >> str;
        if(str.find(IMG_MARKER) != string::npos) {
            if(!isDupe(extractURL(str), urls)){
                urls.push_back(extractURL(str));
            }
        }
    }  
    
    for(size_t i = 0; i < urls.size(); i++){
        outstream << urls[i] << endl;
    }

    instream.close();
    outstream.close();
  
    return 0;
}

//----------------------------------------------------------------------------

string extractURL(string input)
{
    string extractedURL = "";
    size_t index = input.find(URL_START) + URL_START.size();
    for(size_t i = index; i < input.size() - 1; i++) { //-1 is for ending "
        extractedURL.push_back(input[i]);
    }
    return extractedURL;
}

bool isDupe(string input, vector<string> &urls) {
    for(size_t i = 0; i < urls.size(); i++){
        if(input == urls[i])
                return true;
    }
    return false;
}

//----------------------------------------------------------------------------
