
#include "FileHandler.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <cstddef>

using namespace std;

FileHandler::FileHandler(Logger* log) : logger(log) {}

vector<unsigned char> FileHandler::readFile(string filename) {
    vector<unsigned char> data;
    ifstream file(filename, ios::binary);
    
    if (!file.is_open()) {
        std::string msg = "Cannot open file: " + filename;
        logger->log("ERROR", msg);
        return data;
    }
    
    file.seekg(0, ios::end);
    long size = file.tellg();
    file.seekg(0, ios::beg);
    
    if (size > 0) {
        // Read into a string then copy to vector to satisfy some analyzers
        std::string buf;
        buf.resize(static_cast<std::size_t>(size));
        file.read(&buf[0], static_cast<std::streamsize>(size));
        data.assign(buf.begin(), buf.end());
    }
    file.close();
    
    {
        std::string msg = std::string("Read file: ") + filename + std::string(" (") + std::to_string(size) + std::string(" bytes)");
        logger->log("INFO", msg);
    }
    return data;
}

bool FileHandler::writeFile(string filename, vector<unsigned char> data) {
    ofstream file(filename, ios::binary);
    
    if (!file.is_open()) {
        std::string msg = "Cannot create file: " + filename;
        logger->log("ERROR", msg);
        return false;
    }
    
    if (!data.empty()) {
        std::string out(reinterpret_cast<char*>(data.data()), data.size());
        file.write(out.data(), static_cast<std::streamsize>(out.size()));
    }
    file.close();
    
    {
        std::string msg = std::string("Wrote file: ") + filename + std::string(" (") + std::to_string(data.size()) + std::string(" bytes)");
        logger->log("INFO", msg);
    }
    return true;
}

bool FileHandler::fileExists(string filename) {
    ifstream file(filename);
    return file.good();
}

long FileHandler::getFileSize(string filename) {
    ifstream file(filename, ios::binary | ios::ate);
    if (!file.is_open()) return -1;
    
    long size = file.tellg();
    file.close();
    return size;
}