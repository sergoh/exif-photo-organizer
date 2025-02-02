import os
from dotenv import load_dotenv
import piexif
from PIL import Image
from datetime import datetime, timedelta

# Load environment variables from `.env` if it exists
load_dotenv()

# Determine the folder to use
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", os.getcwd())  # Default to current directory

def update_exif_data(image_folder):
    """Modify EXIF timestamps for photos in the specified folder."""
    
    base_timestamp = datetime(2025, 1, 24, 12, 0, 0)
    time_increment = timedelta(seconds=10)

    # Get all image files and sort by filename
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg'))])

    if not image_files:
        print(f"❌ No images found in '{image_folder}'!")
        return

    print(f"📷 Found {len(image_files)} images. Updating EXIF metadata...\n")

    for index, filename in enumerate(image_files):
        file_path = os.path.join(image_folder, filename)

        img = Image.open(file_path)
        new_timestamp = base_timestamp + (index * time_increment)
        formatted_time = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")

        exif_dict = piexif.load(img.info.get("exif", b""))
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = formatted_time.encode()
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = formatted_time.encode()

        exif_bytes = piexif.dump(exif_dict)
        img.save(file_path, "jpeg", exif=exif_bytes)

        print(f"✅ Updated {filename} -> {formatted_time}")

    print("\n🎉 All images have been updated with new EXIF timestamps!")

def main():
    """Entry point for execution."""
    print(f"📂 Using image folder: {IMAGE_FOLDER}")
    update_exif_data(IMAGE_FOLDER)

if __name__ == "__main__":
    main()