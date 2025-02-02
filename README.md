# 🌝 EXIF Photo Organizer

A Python script that modifies the **EXIF timestamps** of images so they appear in the correct order when imported to an iPhone.

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/exif-photo-organizer.git
   cd exif-photo-organizer
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

---

## 🛠️ Usage

This tool processes all images in the **current directory** where it is executed. Users do not need to provide a path.

### **For Local Development (Optional .env Support)**
If you want to specify a different folder for development, you can use a `.env` file.

#### **Steps to set it up:**
1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```
2. **Edit `.env` and set the correct path** to your photos directory:
   ```ini
   IMAGE_FOLDER=/Users/yourusername/path/to/photos
   ```
3. **Save the file.**

If no `.env` file is present, the script will default to using the **current directory** where it is executed.

**Note:** The `.env` file is ignored in Git (`.gitignore`) to prevent accidental sharing of sensitive data.

### **Running the Script**

Simply navigate to the folder where your images are stored and run the executable.

#### **Mac/Linux:**
```bash
cd /path/to/photos
/path/to/exif-photo-organizer
```

#### **Windows:**
```bash
cd C:\Users\YourName\Pictures
C:\path\to\exif-photo-organizer.exe
```

The program will automatically detect all `.jpg` and `.jpeg` files in the **current folder** and modify their timestamps.

### **Optional: Verify EXIF Data**
If you want to check that the timestamps were updated correctly, install `exiftool` and run:

```bash
brew install exiftool  # macOS
sudo apt install libimage-exiftool-perl  # Linux

exiftool /Users/yourusername/path/to/photos/photo1.jpg
```

Look for `DateTimeOriginal` and `CreateDate` fields to confirm that the timestamps were updated.

---

## 🛠️ Building a Standalone Executable
To create an executable version of this tool that users can run without installing Python, follow these steps:

1. **Ensure you have PyInstaller installed:**
   ```bash
   poetry add --dev pyinstaller
   ```

2. **Modify `pyproject.toml` to allow PyInstaller:**
   ```toml
   [tool.poetry.dependencies]
   python = ">=3.11,<3.14"
   ```
   Then, update Poetry:
   ```bash
   poetry lock --no-update
   poetry install
   ```

3. **Create the executable:**
   ```bash
   poetry run pyinstaller --onefile --name exif-photo-organizer update_exif.py
   ```

4. **Run the generated executable:**
   ```bash
   ./dist/exif-photo-organizer
   ```
   Or on Windows:
   ```bash
   dist\exif-photo-organizer.exe
   ```

Now users can **run the tool without installing Python** by downloading the pre-built executable.

---

## 💡 Troubleshooting

### **1️⃣ The script says "No images found in the specified folder"**
- Ensure that the **current directory** contains `.jpg` or `.jpeg` files.
- Check that the folder path doesn’t have typos.

### **2️⃣ The images are still out of order on iPhone**
- Try **AirDropping them in small batches**.
- Ensure that the **modified timestamps** are correct (`exiftool` can help check this).
- If necessary, delete and re-import the images.

---

## 🏆 Credits
Made with ❤️ by **Sergoh**

---

## 📚 License
This project is licensed under the **MIT License**. See `LICENSE` for details.

