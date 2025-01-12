# Media Organizer by Date

## Introduction

The **Media Organizer by Date** is a Python-based application designed to help users organize their photos and videos into folders based on their creation date (year and month). Users can choose to either **move** or **copy** files, with real-time progress tracking and verbose output.

---

## Features

- Organizes media files into `yyyy-mm` folder structures.
- Supports all common photo and video formats.
- Allows users to select source, destination, and error folders.
- Real-time progress bar and verbose output in the GUI.
- Option to move or copy files.
- Runs as a Python script (`mediaOrganizer.py`) or compiled executable (`mediaOrganizer.exe`).

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
     ```bash
     pip install pillow
     ```

### Download the Script

1. Clone or download the `mediaOrganizer.py` script to your computer.

---

## Usage

### Running the Script in CLI

1. Open a terminal (Command Prompt or PowerShell).
2. Navigate to the folder containing the script:
   ```bash
   cd path\to\your\script
