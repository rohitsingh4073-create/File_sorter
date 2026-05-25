# 📂 Python File Sorter

A lightweight, interactive command-line tool built in Python that automatically organizes messy directories into clean, categorized folders. 

This project was built to learn and master Python's modern `pathlib` library.

---

## ✨ Features

*   **Interactive CLI:** Easy-to-use menu system for sorting folders or exiting the program safely.
*   **Smart Categorization:** Automatically groups files into distinct folders based on their extensions:
    *   `MY_IMAGES` (.jpg, .png, .gif, etc.)
    *   `MY_DOCUMENTS` (.pdf, .docx, .txt)
    *   `MY_SPREADSHEETS` (.xlsx, .numbers)
    *   `MY_AUDIO` (.mp3, .wav, etc.)
    *   `MY_VIDEOS` (.mp4, .mkv, .mov)
    *   `MY_ARCHIVES` (.zip, .tar, .rar)
*   **Robust Error Handling:** Features custom exceptions (`InvalidFilePathError`) to validate user inputs, ensuring directories exist and preventing accidental crashes.
*   **Cross-Platform Safe:** Built using `pathlib`, making it automatically compatible with Windows, macOS, and Linux file systems.

---

## 🛠️ How it Works (`pathlib` in Action)

Instead of relying on old-school `os.path` tricks, this project utilizes modern Python workflows:
1.  **Validation:** Employs `.exists()` and `.is_dir()` to verify the targeted path before executing any operations.
2.  **Safety First:** Uses `.mkdir(parents=True, exist_ok=True)` to create sorting folders seamlessly without crashing if they already exist.
3.  **Encapsulation:** Leverages `.suffix` to elegantly isolate file extensions, comparing them against the sorting dictionary.

---

### Prerequisites
Make sure you have Python 3.4+ installed on your machine.
