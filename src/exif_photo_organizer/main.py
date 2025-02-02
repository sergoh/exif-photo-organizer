import os
import shutil
import time
from PIL import Image
from datetime import datetime, timedelta
from dotenv import load_dotenv
import piexif

# Load environment variables from .env (optional for local development)
load_dotenv()

# Use IMAGE_FOLDER from env or default to the current directory
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", os.getcwd())

# Create output folder inside IMAGE_FOLDER
OUTPUT_FOLDER = os.path.join(IMAGE_FOLDER, "output")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Ensure output folder exists

# Base timestamp starts from the current time
base_timestamp = datetime.now()
time_increment = timedelta(seconds=1)  # Each new file is 1 second apart

# Get all image files and sort by filename (ensuring proper order)
image_files = sorted([
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(('.jpg', '.jpeg'))
])

if not image_files:
    print(f"❌ No images found in '{IMAGE_FOLDER}'!")
    exit(1)

print(f"📷 Found {len(image_files)} images in '{IMAGE_FOLDER}'. Creating ordered copies in '{OUTPUT_FOLDER}'...\n")

for index, filename in enumerate(image_files):
    old_file_path = os.path.join(IMAGE_FOLDER, filename)

    # Generate new filename: "Picture 01.jpg"
    new_filename = f"Picture {index + 1:02d}.jpg"
    new_file_path = os.path.join(OUTPUT_FOLDER, new_filename)

    # Open image
    img = Image.open(old_file_path)

    # Create a new timestamp based on order
    new_timestamp = base_timestamp + (index * time_increment)
    formatted_time = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")

    # Load existing EXIF data
    exif_dict = piexif.load(img.info.get("exif", b""))

    # Modify DateTimeOriginal and CreateDate
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = formatted_time.encode()
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = formatted_time.encode()

    # Save modified EXIF data in new copy
    exif_bytes = piexif.dump(exif_dict)
    img.save(new_file_path, "jpeg", exif=exif_bytes)

    # ✅ Modify file system timestamps (creation & modification date)
    timestamp_seconds = new_timestamp.timestamp()
    os.utime(new_file_path, (timestamp_seconds, timestamp_seconds))

    print(f"✅ Created {new_filename} -> {formatted_time}")

    # Small delay to prevent identical timestamps
    time.sleep(0.5)

print("\n🎉 All images have been copied, renamed, and timestamps adjusted successfully!")