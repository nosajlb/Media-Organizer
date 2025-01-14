# Media Organizer by Date
**Media Organizer by Date** is a versatile tool that helps you organize your photos and videos by sorting them into year-month, year-only folders, or dumping them into a single folder of your choice. I created this application because I needed some way to sort through decades of family photos. You're welcome to pull this code and improve on it as you wish.

Created by Jason L. Barnette.


## Introduction

The **Media Organizer by Date** is a Python-based application designed to help users organize their photos and videos into folders based on their creation date. Users can choose between three organization modes:
- Organize into `yyyy-mm` (year-month) folders.
- Organize into `yyyy` (year-only) folders.
- Dump all media files into a single destination folder.

The application provides real-time progress tracking, verbose logging, and a user-friendly GUI. It can also run via the CLI for advanced users.

---

## Features

- **Multiple Organization Modes:** Choose between year-month, year-only, or a single destination folder.
- **Move or Copy Files:** Decide whether to move files or create duplicates in the destination folder.
- **Real-Time Progress Tracking:** Monitor progress through a GUI progress bar and logs.
- **Support for Photos and Videos:** Works with common photo and video file formats.
- **Run in GUI or CLI Mode:** Flexible operation for different user needs.
- **Cross-Platform Compatibility:** Works on Windows with Python installed or as a standalone executable.

---

## Supported Formats

- **Photos:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff`, `.bmp`, `.webp`
- **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.webm`

---

## Installation

### Prerequisites

1. **Python 3.8 or Later**
   - Download and install Python from [python.org](https://www.python.org/).
   - Ensure you check the option **"Add Python to PATH"** during installation.

2. **Required Libraries**
   - Install dependencies by running:
     ```
     pip install pillow
     ```

---

## Usage

### Running in GUI Mode

1. Open a terminal (Command Prompt or PowerShell).
2. Navigate to the folder containing the script:
     ```
     cd path\to\your\script
     ```
3. Launch the application:
     ```
     python mediaOrganizer.py
     ```
4. Use the GUI to:
   - Select the **source folder** containing your media files.
   - Select the **destination folder** where organized files will be saved.
   - Select the **error folder** for files without valid metadata.
   - Choose your **organization mode**:
     - `yyyy-mm` folders.
     - `yyyy` folders.
     - Single folder (dump all files).
   - Choose to **move** or **copy** files.
   - Click **"Organize"** to start processing.

---

### Running in CLI Mode

1. Open a terminal (Command Prompt or PowerShell).
2. Run the script with the required arguments:
     ```
     python mediaOrganizer.py <source_folder> <destination_folder> <error_folder> [--operation move|copy] [--mode sort|year|dump]
     ```
3. Example command:
     ```
     python mediaOrganizer.py "C:\Users\YourName\Pictures" "C:\Users\YourName\OrganizedMedia" "C:\Users\YourName\ErrorMedia" --operation copy --mode year
     ```

   - `<source_folder>`: Folder containing your media files.
   - `<destination_folder>`: Folder where organized files will be saved.
   - `<error_folder>`: Folder for files without valid metadata.
   - `--operation`: Specify whether to `move` or `copy` files (default: `copy`).
   - `--mode`: Specify the organization mode:
     - `sort` for `yyyy-mm` folders.
     - `year` for `yyyy` folders.
     - `dump` for dumping all files into a single folder.

---

### Compiling the Code to an Executable

If you'd like to distribute or run the program without needing Python installed, you can compile it into a standalone `.exe` file. However, there is already an exe in the offial github if you wish to use that.

1. **Install PyInstaller**:
     ```
     pip install pyinstaller
     ```

2. **Compile the Script**:
     ```
     pyinstaller --noconsole --onefile mediaOrganizer.py
     ```

3. The compiled `.exe` will be located in the `dist` folder.

4. Optional: Add a custom icon:
     ```
     pyinstaller --noconsole --onefile --icon=icon.ico mediaOrganizer.py
     ```

---

## Verifying File Integrity

To ensure the downloaded executable file (`mediaOrganizer.exe`) is authentic and has not been tampered with, verify its MD5 checksum.

### MD5 Checksum
The expected MD5 checksum for the current release is:
f680fa2277dd62d1a4344859405a10d3

### How to Verify the Checksum
1. Download the executable file from the release.
2. Open a terminal (Command Prompt or PowerShell on Windows).
3. Navigate to the directory containing the `mediaOrganizer.exe` file.
4. Run the following command:
certutil -hashfile mediaOrganizer.exe MD5
5. Compare the generated checksum with the one listed above. If they match, the file is intact.

### Example Output
If the checksum matches, the output will look like this:
MD5 hash of mediaOrganizer.exe:
<insert_md5_checksum_here>
CertUtil: -hashfile command completed successfully.

If the checksum does not match, download the file again or contact the developer.

---

### Example Workflow

1. Select the folder containing your photos and videos.
2. Choose a destination folder where organized files will be saved.
3. Specify a folder to store files without metadata.
4. Decide whether to move or copy the files.
5. Start the organization process and monitor progress in the GUI or terminal.

---

### Troubleshooting

1. **Python Not Recognized**:
   - Ensure Python is installed and added to your system’s PATH.
   - Verify by running:
     ```
     python --version
     ```

2. **Missing Libraries**:
   - Install missing dependencies using:
     ```
     pip install pillow
     ```

3. **Permission Issues**:
   - Ensure you have write access to the destination and error folders.

4. **Executable Not Working**:
   - Verify that all required resources (e.g., `icon.ico`) are present during compilation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
