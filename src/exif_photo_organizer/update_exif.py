import os
import piexif
from PIL import Image
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env (optional for local development)
load_dotenv()

# Use IMAGE_FOLDER from env or default to the current directory
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", os.getcwd())

# Base timestamp starts from the current time
base_timestamp = datetime.now()
time_increment = timedelta(seconds=10)

# Get all image files and sort by filename (ensure proper order)
image_files = sorted([
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(('.jpg', '.jpeg'))
])

if not image_files:
    print(f"❌ No images found in '{IMAGE_FOLDER}'!")
    exit(1)

print(f"📷 Found {len(image_files)} images in '{IMAGE_FOLDER}'. Updating EXIF metadata and titles...\n")

for index, filename in enumerate(image_files):
    file_path = os.path.join(IMAGE_FOLDER, filename)

    # Open image
    img = Image.open(file_path)

    # Create a new timestamp based on order
    new_timestamp = base_timestamp + (index * time_increment)
    formatted_time = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")

    # Generate EXIF Title (Wedding Picture 01, Wedding Picture 02, ...)
    title = f"Picture {index + 1:02d}"

    # Load existing EXIF data
    exif_dict = piexif.load(img.info.get("exif", b""))

    # Modify DateTimeOriginal and CreateDate
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = formatted_time.encode()
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = formatted_time.encode()

    # Add Title to EXIF (IPTC Metadata)
    if "0th" not in exif_dict:
        exif_dict["0th"] = {}
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = title.encode()

    # Save modified EXIF data
    exif_bytes = piexif.dump(exif_dict)
    img.save(file_path, "jpeg", exif=exif_bytes)

    print(f"✅ Updated {filename} -> {formatted_time}, Title: {title}")

print("\n🎉 All images have been updated with new EXIF timestamps and titles!")