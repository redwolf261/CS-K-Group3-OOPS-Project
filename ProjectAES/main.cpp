#include <iostream>
#include <string>
#include <cstddef>
#include "AES.h"
#include "FileHandler.h"
#include "Logger.h"

using namespace std;
using std::string;
using std::size_t;

int main() {
    Logger logger;
    FileHandler fileHandler(&logger);
    AES aes(&logger);
    
    cout << "\n=== AES FILE ENCRYPTION TOOL ===\n\n";
    
    string filename, password;
    int choice;
    
    cout << "1. Encrypt File\n";
    cout << "2. Decrypt File\n";
    cout << "Enter choice: ";
    cin >> choice;
    cin.ignore();
    
    cout << "Enter file path: ";
    getline(cin, filename);
    
    // Check if file exists
    if (!fileHandler.fileExists(filename)) {
        cout << "Error: File does not exist!" << endl;
        return 1;
    }
    
    cout << "Enter password: ";
    getline(cin, password);
    
    if (password.length() == 0) {
        cout << "Error: Password cannot be empty!" << endl;
        return 1;
    }
    
    aes.setKey(password);
    
    if (choice == 1) {
        string encrypted = filename + ".enc";
        if (aes.encryptFile(filename, encrypted, &fileHandler)) {
            cout << "\nSuccess! Encrypted file: " << encrypted << endl;
        } else {
            cout << "\nEncryption failed!" << endl;
        }
    } else if (choice == 2) {
        string decrypted;
        if (filename.size() > 4 && filename.substr(filename.size() - 4) == ".enc") {
            decrypted = filename.substr(0, filename.size() - 4);
        } else {
            decrypted = filename;
        }
        
        // Find the last directory separator (works for both / and \)
        size_t lastSlash = decrypted.find_last_of("/\\");
        if (lastSlash != string::npos) {
            // Insert "decrypted_" before the filename, not the whole path
            decrypted.insert(lastSlash + 1, "decrypted_");
        } else {
            // No path separators, just prepend to filename
            decrypted = "decrypted_" + decrypted;
        }
        
        if (aes.decryptFile(filename, decrypted, &fileHandler)) {
            cout << "\nSuccess! Decrypted file: " << decrypted << endl;
        } else {
            cout << "\nDecryption failed!" << endl;
        }
    } else {
        cout << "Invalid choice!" << endl;
        return 1;
    }
    
    return 0;
}