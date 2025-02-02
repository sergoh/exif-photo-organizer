import os
import piexif
from PIL import Image
from datetime import datetime, timedelta
# Absolute path to your photos
IMAGE_FOLDER = "/Users/sergoh/Desktop/2025-01-24 V&S wedding/Photos"

# Base timestamp to start from (adjust date & time as needed)
base_timestamp = datetime(2025, 1, 24, 12, 0, 0)  # Year-Month-Day Hour:Min:Sec
time_increment = timedelta(seconds=10)  # Increment time per photo

# Get all image files and sort by filename (ensure proper order)
image_files = sorted([f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.jpeg'))])

if not image_files:
    print("❌ No images found in the specified folder!")
    exit(1)

print(f"📷 Found {len(image_files)} images. Updating EXIF metadata...\n")

for index, filename in enumerate(image_files):
    file_path = os.path.join(IMAGE_FOLDER, filename)

    # Open image
    img = Image.open(file_path)

    # Create a new timestamp based on order
    new_timestamp = base_timestamp + (index * time_increment)
    formatted_time = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")

    # Load existing EXIF data
    exif_dict = piexif.load(img.info.get("exif", b""))

    # Modify DateTimeOriginal and CreateDate
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = formatted_time.encode()
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = formatted_time.encode()

    # Save modified EXIF data
    exif_bytes = piexif.dump(exif_dict)
    img.save(file_path, "jpeg", exif=exif_bytes)

    print(f"✅ Updated {filename} -> {formatted_time}")

print("\n🎉 All images have been updated with new EXIF timestamps!")