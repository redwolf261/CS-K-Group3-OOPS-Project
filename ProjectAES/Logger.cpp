#include "Logger.h"
#include <ctime>
#include <iostream>
#include <cstring>

using namespace std;

Logger::Logger() {
    logFile.open("operations.log", ios::app);
}

Logger::~Logger() {
    if (logFile.is_open()) {
        logFile.close();
    }
}

string Logger::getTimestamp() {
    time_t now = time(0);
    char buffer[80];
    strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", localtime(&now));
    return string(buffer);
}

void Logger::log(const string &level, const string &message) {
    string logEntry = string("[") + getTimestamp() + string("] [") + level + string("] ") + message;
    
    if (logFile.is_open()) {
        logFile << logEntry << endl;
        logFile.flush();
    }
    
    if (level == "ERROR") {
        cerr << logEntry << endl;
    }
}

void Logger::log(const char* level, const string &message) {
    log(string(level), message);
}

void Logger::log(const string &level, const char* message) {
    log(level, string(message));
}

void Logger::log(const char* level, const char* message) {
    log(string(level), string(message));
}