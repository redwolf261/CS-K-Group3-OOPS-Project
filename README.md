# 🔐 AES File Encryption Tool

A robust file encryption/decryption application combining a high-performance C++ AES implementation with a modern Python GUI frontend.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![C++](https://img.shields.io/badge/C++-11-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7+-green.svg)

## 📋 Features

- ✅ **AES-128 Encryption** - Industry-standard encryption algorithm
- ✅ **File Encryption/Decryption** - Secure any file type
- ✅ **Modern GUI** - User-friendly Python interface
- ✅ **Password Protection** - Secure with custom passwords
- ✅ **Cross-Platform** - Works on Windows, Linux, macOS
- ✅ **Detailed Logging** - Track all operations
- ✅ **PKCS#7 Padding** - Proper block alignment

## 🚀 Quick Start

### Prerequisites

- **C++ Compiler** (g++ with C++11 support)
- **Python 3.7+**
- **Optional:** CustomTkinter for modern GUI (`pip install customtkinter`)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ProjectAES.git
cd ProjectAES
```

2. **Build the C++ backend**
```bash
cd ProjectAES
g++ -std=c++11 -Wall main.cpp AES.cpp FileHandler.cpp Logger.cpp -o aes_tool.exe
cd ..
```

3. **Install Python dependencies (optional)**
```bash
pip install -r requirements.txt
```

### Running the Application

**Option 1: Modern GUI (Recommended)**
```bash
python aes_gui_modern.py
```

**Option 2: Basic GUI**
```bash
python aes_gui.py
```

**Option 3: Command Line**
```bash
cd ProjectAES
./aes_tool.exe
```

**Option 4: PowerShell Launchers**
```powershell
.\launch_gui_modern.ps1  # Modern GUI
.\launch_gui.ps1         # Basic GUI
```

## 📂 Project Structure

```
ProjectAES/
├── ProjectAES/              # C++ Source Code
│   ├── main.cpp            # CLI entry point
│   ├── AES.cpp/.h          # AES encryption/decryption
│   ├── FileHandler.cpp/.h  # File I/O operations
│   ├── Logger.cpp/.h       # Logging system
│   └── aes_tool.exe        # Compiled executable
│
├── aes_gui.py              # Basic Python GUI (tkinter)
├── aes_gui_modern.py       # Modern Python GUI (CustomTkinter)
├── launch_gui.ps1          # PowerShell launcher (basic)
├── launch_gui_modern.ps1   # PowerShell launcher (modern)
├── test_setup.py           # Setup verification script
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🎨 GUI Screenshots

The GUI provides:
- 📁 File selection with browse dialog
- 🔐 Encrypt/Decrypt operation selection
- 🔑 Password input with show/hide toggle
- 📊 Real-time operation logs
- ✅ Success/error notifications

## 🔧 Usage Examples

### Encrypting a File

1. Launch the GUI
2. Select **Encrypt File**
3. Browse and select your file
4. Enter a strong password
5. Click **Process File**
6. Encrypted file saved as `filename.ext.enc`

### Decrypting a File

1. Launch the GUI
2. Select **Decrypt File**
3. Browse and select the `.enc` file
4. Enter the **same password** used for encryption
5. Click **Process File**
6. Decrypted file saved as `decrypted_filename.ext`

## 🔒 Security Features

- **AES-128 Encryption** with full implementation
- **Inverse transformations** for proper decryption
- **Password-based key derivation**
- **PKCS#7 padding** for block alignment
- **No password storage** - passwords never saved to disk
- **Secure file handling** - original files remain unchanged

## 🛠️ Technical Details

### AES Implementation

- **Algorithm:** AES-128 (128-bit key)
- **Block Size:** 16 bytes (128 bits)
- **Mode:** ECB (demonstration purposes)
- **Padding:** PKCS#7
- **Rounds:** 10 (standard for AES-128)

### Architecture

```
┌─────────────────┐         ┌──────────────────┐
│   Python GUI    │◄───────►│  C++ Backend     │
│  (Frontend)     │ Process │  (aes_tool.exe)  │
│                 │ Control │                  │
└─────────────────┘         └──────────────────┘
```

### Components

**C++ Backend:**
- S-box and Inverse S-box tables
- Key expansion algorithm
- SubBytes, ShiftRows, MixColumns transformations
- Inverse transformations for decryption
- File I/O with binary handling
- Comprehensive error logging

**Python Frontend:**
- Subprocess communication with C++ backend
- File browser integration
- Real-time status updates
- Input validation
- Cross-platform path handling

## 📝 Building from Source

### Windows (MinGW/MSYS2)
```bash
cd ProjectAES
g++ -std=c++11 -Wall main.cpp AES.cpp FileHandler.cpp Logger.cpp -o aes_tool.exe
```

### Linux/macOS
```bash
cd ProjectAES
g++ -std=c++11 -Wall main.cpp AES.cpp FileHandler.cpp Logger.cpp -o aes_tool
```

## 🧪 Testing

```bash
# Verify setup
python test_setup.py

# Test encryption/decryption
echo "Test message" > test.txt
# Use GUI to encrypt test.txt
# Use GUI to decrypt test.txt.enc with same password
# Compare original and decrypted files
```

## ⚠️ Important Notes

### Security Considerations

- **For demonstration purposes** - Not intended for production use
- **ECB mode** used (consider CBC/GCM for production)
- **No salt/IV** - Consider adding for enhanced security
- **Password strength** - Use strong, unique passwords
- **Backup important data** before encryption

### Password Recovery

⚠️ **PASSWORDS CANNOT BE RECOVERED**
- No password storage mechanism
- No password recovery option
- Wrong password = corrupted decryption
- **Keep your passwords safe!**

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Implement CBC or GCM mode
- [ ] Add salt and IV for key derivation
- [ ] Implement AES-256
- [ ] Add password strength meter
- [ ] Create batch file processing
- [ ] Add file integrity checking (HMAC)
- [ ] Implement secure password storage options
- [ ] Add drag-and-drop support
- [ ] Create unit tests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Your Name - [Your GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- AES algorithm based on FIPS 197 specification
- Python GUI using tkinter and CustomTkinter
- Inspired by the need for accessible encryption tools

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation in `COMPLETE_GUIDE.md`

---

**⭐ Star this repo if you find it useful!**
