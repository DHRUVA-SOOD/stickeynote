import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import shutil
import sys

NOTES_FILE = "sticky_notes.json"

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Note App")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        self.notes = []  # Store notes as (text, path, color)
        
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Note", command=self.add_note, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=5)
        
        self.note_frame = tk.Frame(root, bg="#f0f0f0")
        self.note_frame.pack(fill=tk.BOTH, expand=True)
        
        self.load_notes()
        self.add_to_startup()
    
    def add_note(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Warning", "Note text cannot be empty!")
            return
        
        path = filedialog.askdirectory(title="Select Folder")
        if not path:
            return
        
        color = colorchooser.askcolor(title="Choose Note Color")[1] or "#ffffff"
        
        note_button = tk.Button(self.note_frame, text=text, width=40, bg=color, command=lambda: self.open_folder(path))
        note_button.pack(pady=5)
        
        self.notes.append((text, path, color))
        self.save_notes()
        self.text_entry.delete(0, tk.END)
    
    def open_folder(self, path):
        os.startfile(path)  # Opens folder in file explorer
    
    def save_notes(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self.notes, f)
    
    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                self.notes = json.load(f)
            
            for text, path, color in self.notes:
                note_button = tk.Button(self.note_frame, text=text, width=40, bg=color, command=lambda p=path: self.open_folder(p))
                note_button.pack(pady=5)
    
    def add_to_startup(self):
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        script_path = sys.argv[0]
        shortcut_path = os.path.join(startup_folder, "StickyNoteApp.lnk")
        
        if not os.path.exists(shortcut_path):
            try:
                shutil.copy(script_path, shortcut_path)
            except Exception as e:
                print("Failed to add to startup:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()
