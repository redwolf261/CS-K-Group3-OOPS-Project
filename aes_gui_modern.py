"""
AES Encryption Tool - Modern GUI Frontend with CustomTkinter
Beautiful, modern interface that connects to the C++ AES executable backend
Install: pip install customtkinter
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import os
from pathlib import Path
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AESEncryptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES File Encryption Tool")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Path to the C++ executable
        self.exe_path = Path(__file__).parent / "ProjectAES" / "aes_tool.exe"
        
        # Check if executable exists
        if not self.exe_path.exists():
            messagebox.showerror("Error", f"AES tool executable not found at:\n{self.exe_path}")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = ctk.CTkLabel(
            self.root,
            text="🔐 AES File Encryption Tool",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Operation selection
        operation_label = ctk.CTkLabel(
            main_frame,
            text="Select Operation:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        operation_label.pack(pady=(20, 10))
        
        self.operation_var = ctk.StringVar(value="encrypt")
        
        operation_frame = ctk.CTkFrame(main_frame)
        operation_frame.pack(pady=(0, 20))
        
        encrypt_radio = ctk.CTkRadioButton(
            operation_frame,
            text="Encrypt File",
            variable=self.operation_var,
            value="encrypt",
            font=ctk.CTkFont(size=12)
        )
        encrypt_radio.pack(side="left", padx=20, pady=10)
        
        decrypt_radio = ctk.CTkRadioButton(
            operation_frame,
            text="Decrypt File",
            variable=self.operation_var,
            value="decrypt",
            font=ctk.CTkFont(size=12)
        )
        decrypt_radio.pack(side="left", padx=20, pady=10)
        
        # File selection
        file_label = ctk.CTkLabel(
            main_frame,
            text="Select File:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        file_label.pack(pady=(0, 10))
        
        file_frame = ctk.CTkFrame(main_frame)
        file_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.file_path_var = ctk.StringVar()
        self.file_entry = ctk.CTkEntry(
            file_frame,
            textvariable=self.file_path_var,
            font=ctk.CTkFont(size=12),
            width=450,
            placeholder_text="No file selected"
        )
        self.file_entry.pack(side="left", padx=(10, 10), pady=10)
        
        browse_btn = ctk.CTkButton(
            file_frame,
            text="Browse",
            command=self.browse_file,
            font=ctk.CTkFont(size=12),
            width=100
        )
        browse_btn.pack(side="left", padx=(0, 10), pady=10)
        
        # Password section
        password_label = ctk.CTkLabel(
            main_frame,
            text="Enter Password:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        password_label.pack(pady=(0, 10))
        
        password_frame = ctk.CTkFrame(main_frame)
        password_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.password_var = ctk.StringVar()
        self.password_entry = ctk.CTkEntry(
            password_frame,
            textvariable=self.password_var,
            font=ctk.CTkFont(size=12),
            width=450,
            show="*",
            placeholder_text="Enter encryption/decryption password"
        )
        self.password_entry.pack(side="left", padx=(10, 10), pady=10)
        
        self.show_password_var = ctk.BooleanVar()
        show_pass_check = ctk.CTkCheckBox(
            password_frame,
            text="Show",
            variable=self.show_password_var,
            command=self.toggle_password,
            font=ctk.CTkFont(size=11),
            width=80
        )
        show_pass_check.pack(side="left", padx=(0, 10), pady=10)
        
        # Process button
        self.process_btn = ctk.CTkButton(
            main_frame,
            text="🔒 Process File",
            command=self.process_file,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            fg_color="#27ae60",
            hover_color="#229954"
        )
        self.process_btn.pack(fill="x", padx=20, pady=(0, 20))
        
        # Status/Log section
        log_label = ctk.CTkLabel(
            main_frame,
            text="Status Log:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        log_label.pack(pady=(0, 10))
        
        self.log_text = ctk.CTkTextbox(
            main_frame,
            font=ctk.CTkFont(family="Consolas", size=11),
            height=150
        )
        self.log_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.log("✓ Welcome to AES File Encryption Tool!")
        self.log(f"✓ C++ Backend: {self.exe_path}")
        self.log("─" * 60)
        
    def browse_file(self):
        """Open file browser dialog"""
        if self.operation_var.get() == "encrypt":
            filename = filedialog.askopenfilename(
                title="Select file to encrypt",
                filetypes=[("All Files", "*.*")]
            )
        else:
            filename = filedialog.askopenfilename(
                title="Select file to decrypt",
                filetypes=[("Encrypted Files", "*.enc"), ("All Files", "*.*")]
            )
        
        if filename:
            self.file_path_var.set(filename)
            self.log(f"📁 Selected file: {filename}")
    
    def toggle_password(self):
        """Toggle password visibility"""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
    
    def log(self, message):
        """Add message to log text widget"""
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
    
    def process_file(self):
        """Process the file using C++ backend"""
        file_path = self.file_path_var.get().strip()
        password = self.password_var.get().strip()
        operation = self.operation_var.get()
        
        # Validation
        if not file_path:
            messagebox.showwarning("Warning", "Please select a file!")
            return
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Selected file does not exist!")
            return
        
        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return
        
        if not self.exe_path.exists():
            messagebox.showerror("Error", f"AES tool executable not found!\n{self.exe_path}")
            return
        
        # Disable button during processing
        self.process_btn.configure(state="disabled", text="⏳ Processing...")
        self.log("─" * 60)
        self.log(f"🔄 Operation: {operation.upper()}")
        self.log(f"📄 File: {file_path}")
        
        # Run in separate thread to keep GUI responsive
        thread = threading.Thread(target=self.run_encryption, args=(file_path, password, operation))
        thread.daemon = True
        thread.start()
    
    def run_encryption(self, file_path, password, operation):
        """Run the C++ executable with proper input"""
        try:
            # Prepare input for the C++ program
            choice = "1" if operation == "encrypt" else "2"
            input_data = f"{choice}\n{file_path}\n{password}\n"
            
            # Run the executable
            process = subprocess.Popen(
                str(self.exe_path),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.exe_path.parent
            )
            
            # Send input and get output
            stdout, stderr = process.communicate(input=input_data, timeout=30)
            
            # Process output
            self.root.after(0, self._handle_output, stdout, stderr, process.returncode, file_path, operation)
            
        except subprocess.TimeoutExpired:
            self.root.after(0, self.log, "❌ ERROR: Operation timed out!")
            self.root.after(0, messagebox.showerror, "Error", "Operation timed out!")
            self.root.after(0, self._reset_button)
        except Exception as e:
            self.root.after(0, self.log, f"❌ ERROR: {str(e)}")
            self.root.after(0, messagebox.showerror, "Error", f"An error occurred:\n{str(e)}")
            self.root.after(0, self._reset_button)
    
    def _handle_output(self, stdout, stderr, returncode, file_path, operation):
        """Handle the output from the C++ program"""
        # Log output
        if stdout:
            for line in stdout.strip().split('\n'):
                if line.strip() and "===" not in line:
                    self.log(f"  {line}")
        
        if stderr:
            self.log("⚠️ STDERR:")
            for line in stderr.strip().split('\n'):
                if line.strip():
                    self.log(f"  {line}")
        
        # Check success
        if returncode == 0 and "Success!" in stdout:
            if operation == "encrypt":
                output_file = file_path + ".enc"
                self.log(f"✓ Success! Encrypted: {output_file}")
                messagebox.showinfo("Success", f"File encrypted successfully!\n\nOutput: {output_file}")
            else:
                # Try to extract output filename from stdout
                if "Decrypted file:" in stdout:
                    output_file = stdout.split("Decrypted file:")[-1].strip()
                    self.log(f"✓ Success! Decrypted: {output_file}")
                    messagebox.showinfo("Success", f"File decrypted successfully!\n\nOutput: {output_file}")
                else:
                    self.log("✓ Success! File decrypted.")
                    messagebox.showinfo("Success", "File decrypted successfully!")
        else:
            self.log("❌ Operation failed!")
            messagebox.showerror("Error", "Operation failed! Check the log for details.")
        
        self._reset_button()
    
    def _reset_button(self):
        """Reset the process button"""
        self.process_btn.configure(state="normal", text="🔒 Process File")


def main():
    root = ctk.CTk()
    app = AESEncryptionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
