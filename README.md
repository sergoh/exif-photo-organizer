# 🌝 EXIF Photo Organizer

A simple tool that fixes photo timestamps so they show up in the correct order when imported to an iPhone.

---

## 👥 Download & Install  

### **1️⃣ Download the Program**  
1. **Go to the download page**:  
   [🔗 Latest Release](https://github.com/YOUR_GITHUB_USERNAME/exif-photo-organizer/releases/latest)
2. **Download the correct file for your operating system**:
   - **Mac**: `exif-photo-organizer-mac`
   - **Windows**: `exif-photo-organizer-win.exe`
   - **Linux**: `exif-photo-organizer-linux`

### **2️⃣ Move the File to Your Photos Folder**  
- Move the downloaded file to the **folder where your photos are stored**.

---

## 🚀 How to Run the Program  

### **🖥️ Mac (Apple)**
1. **Open the Terminal app** (Find it in Applications → Utilities).
2. **Navigate to your photos folder**, then **run the program**:
   ```bash
   cd /Users/YOURNAME/Pictures/YOURFOLDER
   chmod +x exif-photo-organizer-mac
   ./exif-photo-organizer-mac
   ```
   _(Replace "YOURNAME" with your actual username, and "YOURFOLDER" with the folder name where your photos are stored.)_

---

### **🖥️ Windows**
1. **Open the Command Prompt**:
   - Press **`Windows Key + R`**, type **`cmd`**, and press **Enter**.
2. **Navigate to your photos folder**, then **run the program**:
   ```powershell
   cd C:\Users\YourName\Pictures\YourFolder
   exif-photo-organizer-win.exe
   ```
   _(Replace "YourName" with your actual Windows username and "YourFolder" with the folder name where your photos are stored.)_

---

### **🖥️ Linux**
1. **Open a terminal**.
2. **Navigate to your photos folder**, then **run the program**:
   ```bash
   cd /home/YOURNAME/Pictures/YOURFOLDER
   chmod +x exif-photo-organizer-linux
   ./exif-photo-organizer-linux
   ```
   _(Replace "YOURNAME" with your actual Linux username.)_

---

## ✅ What This Program Does
- **Finds all photos (.JPG, .JPEG) in the folder.**
- **Fixes their timestamps so they appear in order on your iPhone.**
- **Takes only a few seconds to complete.**

When finished, you'll see ✅ confirmation messages.

---

## 🔍 How to Check If It Worked  
If you want to **verify that the timestamps were updated correctly**, you can check the photo details:

### **Mac**  
1. Right-click the photo → Click **Get Info**.  
2. Check the **Date Created** and **Date Modified** fields.  

### **Windows**  
1. Right-click the photo → Click **Properties** → Go to the **Details** tab.  
2. Check the **Date Taken** and **Created Date** fields.

---

## ❌ Troubleshooting  

### **1️⃣ The program says "No images found"**  
✅ Make sure your **photos are in the same folder as the program**.  
✅ Double-check the **folder name** before running the program.

### **2️⃣ Photos are still out of order on iPhone**  
✅ Try **AirDropping them in small batches**.  
✅ Ensure that the **modified timestamps** are correct (`exiftool` can help check this).  
✅ If necessary, delete the photos from your iPhone and **re-import them**.

---

## 🛠️ For Developers: Running the Script Manually  

If you want to use the Python script directly **(instead of using the compiled executable)**:

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/exif-photo-organizer.git
cd exif-photo-organizer
```

### **2️⃣ Install dependencies using Poetry**
```bash
poetry install
```

### **3️⃣ Run the script**
```bash
poetry run python update_exif.py
```

By default, the script **modifies images in the current directory**.

### **Optional: Using a `.env` file for a Custom Folder**
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

---

## 🛠️ Building a Standalone Executable

If you want to create a **buildable package** that runs without Python installed, you can use **PyInstaller**.

### **Steps to Build:**

1. **Ensure PyInstaller is installed**:
   ```bash
   poetry add --dev pyinstaller
   ```

2. **Create the standalone executable**:
   ```bash
   poetry run pyinstaller --onefile --name exif-photo-organizer-${{ runner.os }} update_exif.py
   ```

3. **Locate the built executable**:
   - On **Mac**, the file will be:
     ```bash
     ./dist/exif-photo-organizer-mac
     ```
   - On **Windows**, it will be:
     ```powershell
     dist\exif-photo-organizer-win.exe
     ```
   - On **Linux**, it will be:
     ```bash
     ./dist/exif-photo-organizer-linux
     ```

4. **Run the generated executable**:
   ```bash
   ./dist/exif-photo-organizer-mac  # Mac
   ./dist/exif-photo-organizer-linux  # Linux
   ```
   ```powershell
   dist\exif-photo-organizer-win.exe  # Windows
   ```

Now users can run the tool **without needing to install Python** by downloading the pre-built executable.

---

## 🌟 Credits  
Made with ❤️ by **Sergoh**  

📚 **License:** MIT License  

