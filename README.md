### **Updated README**

#### **Introduction**

The **Media Organizer by Date** is a Python-based application designed to help users organize their photos and videos into folders based on their creation date (year and month). Users can choose to either **move** or **copy** files, with real-time progress tracking and verbose output.

* * * * *

### **Features**

-   Organizes media files into `yyyy-mm` folder structures.
-   Supports all common photo and video formats.
-   Allows users to select source, destination, and error folders.
-   Real-time progress bar and verbose output in the GUI.
-   Option to move or copy files.
-   Runs as a Python script (`mediaOrganizer.py`) or compiled executable (`mediaOrganizer.exe`).

* * * * *

### **Supported Formats**

-   **Photos:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff`, `.bmp`, `.webp`
-   **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.webm`

* * * * *

### **Installation**

#### **Prerequisites**

1.  **Python 3.8 or Later**

    -   Download and install Python from [python.org](https://www.python.org/).
    -   Ensure you check the option **"Add Python to PATH"** during installation.
2.  **Required Libraries**

    -   Install dependencies by running:

        pip install pillow

#### **Download the Script**

1.  Clone or download the `mediaOrganizer.py` script to your computer.

* * * * *

### **Usage**

#### **Running the Script in CLI**

1.  Open a terminal (Command Prompt or PowerShell).
2.  Navigate to the folder containing the script:

    cd path\to\your\script

3.  Run the script:

    python mediaOrganizer.py

4.  The GUI will open. Use it to:
    -   Select the **source folder** containing the media files.
    -   Select the **destination folder** where organized files will be saved.
    -   Select the **error folder** for files without valid metadata.
    -   Choose to **move** or **copy** files.
    -   Click "Organize" to start processing.

#### **Running the Script as an EXE**

1.  **Compile the Script to an Executable** (This is already done, hence the exe in this GIT, but you can do it yourself if you want to):

    -   Install PyInstaller:

        pip install pyinstaller

    -   Compile the script:

        pyinstaller --noconsole --onefile mediaOrganizer.py

    -   The compiled `.exe` file will be located in the `dist` folder and will be named `mediaOrganizer.exe`.
2.  **Run the EXE File**:

    -   Double-click the `mediaOrganizer.exe` file to launch the application.
    -   Follow the GUI instructions as described above.

* * * * *

### **Example Workflow**

1.  **Select Source Folder:** Choose `C:\Users\YourName\Pictures`.
2.  **Select Destination Folder:** Choose `C:\Users\YourName\OrganizedMedia`.
3.  **Select Error Folder:** Choose `C:\Users\YourName\ErrorMedia`.
4.  **Choose Move or Copy:** Select the desired option.
5.  **Click Organize:** Watch progress in the log and progress bar.

* * * * *

### **Troubleshooting**

1.  **Python Not Recognized in CLI**

    -   Ensure Python is installed and added to PATH.
    -   Verify by running:

        python --version

2.  **Missing Libraries**

    -   Install missing dependencies:

        pip install pillow

3.  **Issues with EXE**

    -   Ensure PyInstaller is correctly installed and used.
    -   Recompile the script if necessary.
4.  **Files Not Organized**

    -   Check the error folder for files without metadata.

* * * * *

### **Contributing**

Contributions are welcome, but I probably won't do very much with this going forward. I wrote this to help me organize thousands of old photos from an external hard drive. You're welcome to provide suggestions though.

* * * * *

### **License**

This project is licensed under the MIT License. See the LICENSE file for more details.
