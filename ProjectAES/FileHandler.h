#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <vector>
#include <string>
#include "Logger.h"

using namespace std;

class FileHandler {
private:
    Logger* logger;
    
public:
    FileHandler(Logger* log);
    vector<unsigned char> readFile(string filename);
    bool writeFile(string filename, vector<unsigned char> data);
    bool fileExists(string filename);
    long getFileSize(string filename);
};

#endif