"""
Quick test script to verify Python GUI setup
"""

import sys
import os
from pathlib import Path

print("="*60)
print("AES Encryption Tool - Setup Verification")
print("="*60)

# Check Python version
print(f"\n✓ Python Version: {sys.version}")

# Check tkinter
try:
    import tkinter as tk
    print("✓ tkinter (GUI library): Available")
except ImportError:
    print("✗ tkinter: NOT AVAILABLE")
    print("  Please reinstall Python with tkinter support")

# Check for C++ executable
exe_path = Path(__file__).parent / "ProjectAES" / "aes_tool.exe"
if exe_path.exists():
    print(f"✓ C++ Backend: Found at {exe_path}")
else:
    print(f"✗ C++ Backend: NOT FOUND at {exe_path}")
    print("  Build it with:")
    print("    cd ProjectAES")
    print("    g++ -std=c++11 -Wall main.cpp AES.cpp FileHandler.cpp Logger.cpp -o aes_tool.exe")

# Check for GUI files
gui_basic = Path(__file__).parent / "aes_gui.py"
gui_modern = Path(__file__).parent / "aes_gui_modern.py"

print(f"\n✓ Basic GUI: {'Found' if gui_basic.exists() else 'NOT FOUND'}")
print(f"✓ Modern GUI: {'Found' if gui_modern.exists() else 'NOT FOUND'}")

print("\n" + "="*60)
print("Setup Status: READY" if exe_path.exists() else "Setup Status: NEEDS BUILD")
print("="*60)

print("\nTo launch the GUI:")
print("  Basic:  python aes_gui.py")
print("  Modern: python aes_gui_modern.py  (requires: pip install customtkinter)")
print("\nOr use the launcher scripts:")
print("  .\\launch_gui.ps1")
print("  .\\launch_gui_modern.ps1")

input("\nPress Enter to exit...")
