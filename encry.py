import tkinter as tk
from tkinter import messagebox
import pyperclip
def encrypt_text():
    plaintext = input_text.get()
    encrypted_text = ''.join(str(ord(char)) for char in plaintext)
    messagebox.showinfo("Encrypted Text", f"Encrypted Text: {encrypted_text}")
def decrypt_text():
    encrypted_text = input_text.get()
    decrypted_text = ''.join(chr(int(encrypted_text[i:i+3])) for i in range(0, len(encrypted_text), 3))
    messagebox.showinfo("Decrypted Text", f"Decrypted Text: {decrypted_text}")
def copy_text():
    encrypted_text = input_text.get()
    pyperclip.copy(encrypted_text)
    messagebox.showinfo("Copied", "Encrypted text copied to clipboard.")
window = tk.Tk()
window.title("EncryWare")
window.geometry("350x420")
title_label = tk.Label(window, text="EncryWare", fg="black", font=("Helvetica", 16))
title_label.pack(pady=10)
input_text = tk.Entry(window, width=40)
input_text.pack(pady=10)
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=5)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.pack(pady=5)
copy_button = tk.Button(window, text="Copy", command=copy_text)
copy_button.pack(pady=5)
window.mainloop()
