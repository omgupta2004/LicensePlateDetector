import tkinter as tk
from tkinter import messagebox
import os
from detector import detect_license_plates

def start_detection():
    messagebox.showinfo("Info", "Detection starting. Please wait...")
    detect_license_plates()
    messagebox.showinfo("Done", "Detection complete! Check log and snapshots.")

def open_log_file():
    path = os.path.abspath("database/plate_log.csv")
    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showerror("Error", "Log file not found.")

def view_snapshots():
    path = os.path.abspath("static/snapshots")
    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showerror("Error", "Snapshots folder not found.")

root = tk.Tk()
root.title("License Plate Detector")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="License Plate Detector", font=("Helvetica", 16, "bold")).pack(pady=20)
tk.Button(root, text="Start Detection", width=25, command=start_detection).pack(pady=10)
tk.Button(root, text="View Log File", width=25, command=open_log_file).pack(pady=10)
tk.Button(root, text="View Snapshots", width=25, command=view_snapshots).pack(pady=10)

root.mainloop()
