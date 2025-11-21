#ifndef LOGGER_H
#define LOGGER_H

#include <string>
#include <fstream>

using namespace std;

class Logger {
private:
    ofstream logFile;
    string getTimestamp();
    
public:
    Logger();
    ~Logger();
    void log(const string &level, const string &message);
    // convenience overloads
    void log(const char* level, const string &message);
    void log(const string &level, const char* message);
    void log(const char* level, const char* message);
};

#endif