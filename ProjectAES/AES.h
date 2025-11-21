#ifndef AES_H
#define AES_H

#include <vector>
#include <string>
#include "FileHandler.h"
#include "Logger.h"

using namespace std;

class AES {
private:
    static const int BLOCK_SIZE = 16;
    vector<unsigned char> key;
    Logger* logger;
    
    vector<unsigned char> encryptBlock(vector<unsigned char> block);
    vector<unsigned char> decryptBlock(vector<unsigned char> block);
    vector<unsigned char> addPadding(vector<unsigned char> data);
    vector<unsigned char> removePadding(vector<unsigned char> data);
    
public:
    AES(Logger* log);
    void setKey(string password);
    bool encryptFile(string inputFile, string outputFile, FileHandler* fh);
    bool decryptFile(string inputFile, string outputFile, FileHandler* fh);
};

#endif