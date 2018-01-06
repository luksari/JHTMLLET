#include <iostream>
#include <fstream>
#include <tuple>
#include <utility>

using namespace std;

void tagToUpper(string& code, ofstream& out);
pair<int, int> getData; // Global variable - bleeeee


int main(int argc, char* argv[])
{
    if(argc != 3){
       cerr << "Usage: " << argv[0] << " Input_file Output_file" << endl;
       return -1;
    }

    ifstream in(argv[1]);
    ofstream out(argv[2]);
    string code;
    pair<int, int> data;



    if(in.is_open()){
        if(out.is_open()){
            while(getline (in,code)){
              tagToUpper(code, out);
              data = make_pair(data.first+=getData.first, data.second+=getData.second);
            }
            in.close();
            out.close();

        }
        else{
            cerr << "Unable to open file" << argv[2] << endl;
            return -1;
        }
    }
    else{
        cerr << "Unable to open file" << argv[1] << endl;
        return -1;
    }
    return 0;
}

void tagToUpper(string& code, ofstream& out)
{
    bool tagOpened = false;
    bool noCloseTag = false;
    int tags = 0, letters = 0;
    string meta = "<meta";
    string html = "<html";

        for(unsigned int i = 0; i < code.length(); i++){
            if(code.find(meta) != string::npos){
                code.replace(code.find(meta),meta.length(),"<META");
                noCloseTag = true;
                tags++;
                letters+=4;

            }
            if(code.find(html) != string::npos){
                code.replace(code.find(html),html.length(),"<HTML");
                noCloseTag = true;
                tags++;
                letters+=4;

            }
            if(!tagOpened && !noCloseTag)
            {
                if(code.at(i) == '<'){
                    tagOpened = true;
                    tags++;
                }
            }
            else
            {
                if(code.at(i) == '>' || (code.at(i) == '/' && code.at(i+1) == '>')) // Self enclosing tag
                    tagOpened = false;

                else //Check if it is not closed yet
                {
                    if(code.at(i) >= 97 && code.at(i) <= 122 && !noCloseTag){ // Check if it is small letter
                        code[i] -= 32; // Dividing 32 from char code makes letter CAPITAL
                        letters++;

                    }
                }
            }
            out << code[i];
        }
        out << endl;
        getData = make_pair(tags, letters);
    }




