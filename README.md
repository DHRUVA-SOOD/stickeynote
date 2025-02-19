# stickeynote
# Sticky Note App

## Overview
The **Sticky Note App** is a simple **offline** note-taking application built with Python and Tkinter. It allows users to create sticky notes that are linked to folders on their system. Clicking a note will open the corresponding folder in the file explorer. The application is **persistent**, meaning it saves notes across sessions, and it **automatically starts when the computer is turned on**.

## Features
- **Create Sticky Notes**: Users can enter a note title and link it to a folder of their choice.
- **Open Linked Folder**: Clicking on a note will open the corresponding folder in the file explorer.
- **Color Customization**: Users can choose a background color for each note.
- **Persistent Storage**: Notes are saved in a JSON file (`sticky_notes.json`) and are loaded when the app starts.
- **Auto-Startup**: The app automatically adds itself to the Windows startup folder.

## How It Works
### 1. Creating a Note
- Enter the note text in the input box.
- Select a folder that the note will be linked to.
- Choose a background color for the note.
- The note appears in the app as a clickable button.

### 2. Opening a Linked Folder
- Clicking on a note will open the **linked folder** in Windows File Explorer.
- This is achieved using Python's `os.startfile(path)` function, which opens a directory in the default file manager.

### 3. Saving Notes
- Notes are stored in a **JSON file** (`sticky_notes.json`) so that they remain available after restarting the app.
- When the app launches, it loads the saved notes and displays them with their assigned colors.

### 4. Auto-Starting on Boot
- The app copies itself to the **Windows Startup folder**, ensuring it runs automatically when the computer starts.
- This is managed using the `shutil.copy()` function.

## How to Run the App
1. Install Python (if not installed already).
2. Run the script using:
   ```sh
   python stickynote.py
   ```
3. To convert it into an **executable file** (optional):
   ```sh
   pip install pyinstaller
   pyinstaller --onefile --windowed stickynote.py
   ```
   The `.exe` file will be generated in the `dist/` folder.
4. Move the executable to a convenient location and run it.

## Future Improvements
- Add support for **editing** existing notes.
- Allow users to link **specific files** instead of just folders.
- Provide an option to **remove** notes.
- Enhance the UI with better styling.

## License
This project is open-source and can be modified as needed. Enjoy using your **Sticky Note App**! 🚀

