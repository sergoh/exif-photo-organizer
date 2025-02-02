# 🌝 Photo Organizer

A simple tool that creates **renamed copies** of photos with timestamps in the correct order for iPhone Photos.

---

## 👥 Download & Install  

### **1️⃣ Download the Program**  
1. **Go to the download page**:  
   [🔗 Latest Release](https://github.com/sergoh/exif-photo-organizer/releases/latest)
2. **Download the correct file**:
   - **Mac**: `photo-organizer-mac`
   - **Windows**: `photo-organizer-win.exe`
   - **Linux**: `photo-organizer-linux`

### **2️⃣ Move the File to Your Photos Folder**  
- Move the downloaded file to the **folder where your photos are stored**.

---

## 🚀 How to Run the Program  

### **🖥️ Mac (Apple)**
1. **Find Your Photos Folder Path**:
   - Open **Finder**.
   - Navigate to the folder where your photos are stored.
   - **Right-click the folder** and select **"Get Info"**.
   - Look for **"Where:"** and copy the full path.
   - Alternatively, drag the folder into the Terminal to automatically paste the path.

2. **Open the Terminal app** (Find it in Applications → Utilities).
3. **Navigate to your photos folder**, then **run the program**:
   ```bash
   cd /PATH/TO/YOUR/PICTURE/FOLDER
   chmod +x photo-organizer-mac
   ./photo-organizer-mac
   ```
   _(Replace "/PATH/TO/YOUR/PICTURE/FOLDER" with the actual path you copied from Finder.)_

#### **🔧 If You See a macOS Security Warning**
If you get an error saying **"Apple cannot verify the app for malware"**, follow these steps:

1. **Go to System Settings → Privacy & Security**.
2. Scroll down and look for a message saying:
   - *"photo-organizer-mac was blocked from use"*
3. Click **"Allow Anyway."**
4. Run the program again:
   ```bash
   ./photo-organizer-mac
   ```
5. macOS will still warn you. Click **"Open Anyway."**

#### **🔧 Remove Quarantine Warning Permanently**
If macOS keeps blocking the file, remove its **quarantine flag**:
```bash
xattr -d com.apple.quarantine photo-organizer-mac
```
Then, try running the program again:
```bash
./photo-organizer-mac
```

---

### **🖥️ Windows**
1. **Open the Command Prompt**:
   - Press **`Windows Key + R`**, type **`cmd`**, and press **Enter**.
2. **Navigate to your photos folder**, then **run the program**:
   ```powershell
   cd C:\Users\YourName\Pictures\YourFolder
   photo-organizer-win.exe
   ```
   _(Replace "YourName" with your actual Windows username and "YourFolder" with the folder name where your photos are stored.)_

---

### **🖥️ Linux**
1. **Open the Terminal.**
2. **Navigate to your photos folder**:
   ```bash
   cd /home/yourname/Pictures/yourfolder
   ```
3. **Make the file executable and run it**:
   ```bash
   chmod +x photo-organizer-linux
   ./photo-organizer-linux
   ```

---

## 🛠️ What This Program Does
- **Creates renamed copies of all `.JPG` and `.JPEG` files in the folder.**
- **Adds timestamps to ensure correct ordering on iPhone.**
- **Renames files to `Wedding Picture 01.jpg`, `Wedding Picture 02.jpg`, etc.**
- **Leaves the original files untouched.**

When finished, you'll see ✅ confirmation messages.

---

## 🔍 How to Verify It Worked  
If you want to **check that the files were created and renamed correctly**, follow these steps:

### **Mac**  
1. Open **Finder** and navigate to the folder.
2. Check that new files appear as **"Wedding Picture 01.jpg", "Wedding Picture 02.jpg", etc."**

### **Windows**  
1. Open **File Explorer** and navigate to the folder.
2. Confirm that new copies exist and are correctly ordered.

### **Linux**  
1. Open the Terminal and list the files:
   ```bash
   ls -l
   ```
2. Check that the newly created images are in correct order.

---

## 🛠️ For Developers: Running the Script Manually  

If you want to use the Python script directly **(instead of using the compiled executable)**:

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/sergoh/exif-photo-organizer.git
cd exif-photo-organizer
```

### **2️⃣ Install dependencies using Poetry**
```bash
poetry install
```

### **3️⃣ Run the script**
```bash
poetry run python src/exif_photo_organizer/update_exif.py
```

By default, the script **creates new copies in the current directory**.

---

## 🛠️ Building a Standalone Executable  
If you want to manually build a standalone executable without relying on GitHub Actions, follow these steps:

### **1️⃣ Install PyInstaller**
Make sure you have **Poetry** installed and run:
```bash
poetry add --dev pyinstaller
```

### **2️⃣ Build the Executable for Your OS**
Run one of the following based on your operating system:

#### **Mac (Apple)**
```bash
poetry run pyinstaller --onefile --name photo-organizer-mac src/exif_photo_organizer/update_exif.py
```

#### **Windows**
```powershell
poetry run pyinstaller --onefile --name photo-organizer-win.exe src/exif_photo_organizer/update_exif.py
```

#### **Linux**
```bash
poetry run pyinstaller --onefile --name photo-organizer-linux src/exif_photo_organizer/update_exif.py
```

### **3️⃣ Locate the Built Executable**
- **Mac/Linux:**  
  ```bash
  ./dist/photo-organizer-mac  # or photo-organizer-linux
  ```
- **Windows:**  
  ```powershell
  dist\photo-organizer-win.exe
  ```

---

## 🌟 Credits  
Made with ❤️ by **Sergoh**  

📚 **License:** MIT License  

