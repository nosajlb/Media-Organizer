from tkinter import Tk, Label, Button, Radiobutton, StringVar, filedialog, Text, Scrollbar, END, Frame, messagebox
from tkinter.ttk import Progressbar
import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import time

SUPPORTED_EXTENSIONS = {
    "photos": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".webp"],
    "videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"]
}

class MediaOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Organizer by Date")
        self.root.geometry("500x700")
        self.root.resizable(False, False)

        # Folder paths
        self.source_folder = ""
        self.destination_folder = ""
        self.error_folder = ""

        # Operation mode (move or copy) - Default to "copy"
        self.operation = StringVar(value="copy")

        # Organization mode (sort yyyy-mm, yyyy, or dump) - Default to "sort"
        self.organization_mode = StringVar(value="sort")

        # GUI Components
        Label(root, text="Media Organizer by Date", font=("Arial", 20, "bold")).pack(pady=5)
        Label(root, text="by Jason L. Barnette", font=("Arial", 12, "italic")).pack(pady=5)

        Button(root, text="Select Source Folder", command=self.select_source_folder).pack(pady=5)
        self.source_label = Label(root, text="Source Folder: Not selected", fg="gray")
        self.source_label.pack()

        Button(root, text="Select Destination Folder", command=self.select_destination_folder).pack(pady=5)
        self.destination_label = Label(root, text="Destination Folder: Not selected", fg="gray")
        self.destination_label.pack()

        Button(root, text="Select Error Folder", command=self.select_error_folder).pack(pady=5)
        self.error_label = Label(root, text="Error Folder: Not selected", fg="gray")
        self.error_label.pack()

        Label(root, text="Select Organization Mode:").pack(pady=5)
        Radiobutton(root, text="Sort into yyyy-mm folders", variable=self.organization_mode, value="sort").pack()
        Radiobutton(root, text="Sort into yyyy folders", variable=self.organization_mode, value="year").pack()
        Radiobutton(root, text="Dump all into a single folder", variable=self.organization_mode, value="dump").pack()

        # Operation mode: Default to "copy"
        Radiobutton(root, text="Copy Files", variable=self.operation, value="copy").pack()
        Radiobutton(root, text="Move Files", variable=self.operation, value="move").pack()

        Button(root, text="Organize", command=self.organize_files).pack(pady=10)

        # Progress bar
        self.progress = Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Output log
        log_frame = Frame(root)
        log_frame.pack(pady=10, fill="both", expand=True)

        self.log = Text(log_frame, height=15, wrap="word", state="normal")
        self.log.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(log_frame, command=self.log.yview)
        scrollbar.pack(side="right", fill="y")
        self.log.config(yscrollcommand=scrollbar.set)

    def log_message(self, message):
        """Adds a message to the log output."""
        self.log.insert(END, message + "\n")
        self.log.see(END)
        self.root.update()  # Refresh the GUI to show updates in real time

    def select_source_folder(self):
        self.source_folder = filedialog.askdirectory(title="Select Source Folder")
        if self.source_folder:
            self.source_label.config(text=f"Source Folder: {self.source_folder}", fg="black")
            self.log_message(f"Selected source folder: {self.source_folder}")

    def select_destination_folder(self):
        self.destination_folder = filedialog.askdirectory(title="Select Destination Folder")
        if self.destination_folder:
            self.destination_label.config(text=f"Destination Folder: {self.destination_folder}", fg="black")
            self.log_message(f"Selected destination folder: {self.destination_folder}")

    def select_error_folder(self):
        self.error_folder = filedialog.askdirectory(title="Select Error Folder")
        if self.error_folder:
            self.error_label.config(text=f"Error Folder: {self.error_folder}", fg="black")
            self.log_message(f"Selected error folder: {self.error_folder}")

    def organize_files(self):
        if not all([self.source_folder, self.destination_folder, self.error_folder]):
            messagebox.showerror("Error", "Please select all folders before organizing.")
            return

        operation_type = self.operation.get()
        organization_mode = self.organization_mode.get()
        self.log_message(f"Starting organization ({operation_type}, mode: {organization_mode})...")
        self.run_organizer(self.source_folder, self.destination_folder, self.error_folder, operation_type, organization_mode)
        self.log_message("Media organization complete!")
        messagebox.showinfo("Success", "Media organization complete!")

    def run_organizer(self, source_dir, dest_dir, error_dir, operation, organization_mode):
        total_files = sum(len(files) for _, _, files in os.walk(source_dir))
        processed_files = 0
        self.progress["maximum"] = total_files

        for root, _, files in os.walk(source_dir):
            for filename in files:
                filepath = os.path.join(root, filename)

                if not self.has_supported_extension(filename):
                    continue

                try:
                    if organization_mode == "sort":
                        year, month = self.get_file_date(filepath)
                        if year and month:
                            folder_name = f"{year}-{month}"
                            target_folder = os.path.join(dest_dir, folder_name)
                        else:
                            target_folder = error_dir
                    elif organization_mode == "year":
                        year, _ = self.get_file_date(filepath)
                        if year:
                            folder_name = f"{year}"
                            target_folder = os.path.join(dest_dir, folder_name)
                        else:
                            target_folder = error_dir
                    else:  # Dump all into a single folder
                        target_folder = dest_dir

                    os.makedirs(target_folder, exist_ok=True)
                    unique_filename = self.create_unique_filename(target_folder, filename)
                    new_path = os.path.join(target_folder, unique_filename)

                    if operation == "move":
                        os.rename(filepath, new_path)
                    elif operation == "copy":
                        shutil.copy2(filepath, new_path)

                    self.log_message(f"{operation.capitalize()}d: {filename} -> {new_path}")
                except Exception as e:
                    self.log_message(f"Error processing {filename}: {e}")

                processed_files += 1
                self.progress["value"] = processed_files
                self.root.update()

    def has_supported_extension(self, filename):
        _, ext = os.path.splitext(filename)
        return ext.lower() in SUPPORTED_EXTENSIONS["photos"] + SUPPORTED_EXTENSIONS["videos"]

    def get_file_date(self, filepath):
        try:
            if os.path.splitext(filepath)[1].lower() in SUPPORTED_EXTENSIONS["photos"]:
                img = Image.open(filepath)
                exif_data = img._getexif()
                if exif_data:
                    for tag_id, value in exif_data.items():
                        if TAGS.get(tag_id, tag_id) == 'DateTimeOriginal':
                            date = value.split(" ")[0]
                            year, month, _ = date.split(":")
                            return year, month
        except Exception:
            pass

        timestamp = os.path.getmtime(filepath)
        year = time.strftime("%Y", time.localtime(timestamp))
        month = time.strftime("%m", time.localtime(timestamp))
        return year, month

    def create_unique_filename(self, directory, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base}-{counter:02}{ext}"
            counter += 1
        return new_filename


if __name__ == "__main__":
    root = Tk()
    app = MediaOrganizerApp(root)
    root.mainloop()
