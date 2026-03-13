from PIL import Image
import os
import io
from google.cloud import storage
from pathlib import Path

def download_icon_from_gcs(bucket_name, blob_name, local_path="temp_icon.png"):
    """
    Download an icon from Google Cloud Storage
    
    Args:
        bucket_name: GCS bucket name
        blob_name: Path to the icon in the bucket
        local_path: Where to save the downloaded icon locally
    
    Returns:
        Path to the downloaded icon
    """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(local_path)
        print(f"✓ Downloaded icon from GCS: {bucket_name}/{blob_name}")
        return local_path
    except Exception as e:
        print(f"✗ Error downloading from GCS: {e}")
        raise

def generate_app_icons(source_image_path, output_folder="app_icons"):
    """
    Generate all required Google Play Console icon sizes from a source image
    
    Args:
        source_image_path: Path to the source icon image
        output_folder: Where to save generated icons
    """
    # Check if output folder path exists as a file (not directory)
    if os.path.isfile(output_folder):
        print(f"✗ Error: '{output_folder}' is a file, not a directory. Please use a different folder name.")
        raise FileExistsError(f"Cannot create directory '{output_folder}' - it exists as a file.")
    
    os.makedirs(output_folder, exist_ok=True)
    
    try:
        img = Image.open(source_image_path)
        print(f"✓ Loaded source image: {source_image_path}")
    except Exception as e:
        print(f"✗ Error loading image: {e}")
        raise
    
    # Google Play Console required icon sizes for all devices
    required_sizes = {
        # Play Store Console
        "playstore_icon_512": (512, 512),
        "playstore_featured_1024x500": (1024, 500),
        
        # Android App Icons (mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi)
        "app_icon_ldpi": (36, 36),      # Low DPI
        "app_icon_mdpi": (48, 48),      # Medium DPI
        "app_icon_hdpi": (72, 72),      # High DPI
        "app_icon_xhdpi": (96, 96),     # Extra High DPI
        "app_icon_xxhdpi": (144, 144),  # Extra Extra High DPI
        "app_icon_xxxhdpi": (192, 192), # Extra Extra Extra High DPI
        
        # Large icons
        "app_icon_512": (512, 512),
        
        # Adaptive Icon foreground/background (Android 8.0+)
        "adaptive_icon_foreground_108": (108, 108),
        "adaptive_icon_foreground_162": (162, 162),
        "adaptive_icon_foreground_216": (216, 216),
        
        # Notification icons
        "notification_icon_20": (20, 20),
        "notification_icon_24": (24, 24),
        "notification_icon_29": (29, 29),
        "notification_icon_30": (30, 30),
        "notification_icon_36": (36, 36),
        "notification_icon_40": (40, 40),
        "notification_icon_48": (48, 48),
        "notification_icon_60": (60, 60),
        "notification_icon_72": (72, 72),
        "notification_icon_96": (96, 96),
    }
    
    generated_count = 0
    for name, size in required_sizes.items():
        try:
            resized = img.resize(size, Image.Resampling.LANCZOS)
            output_path = os.path.join(output_folder, f"{name}.png")
            resized.save(output_path)
            print(f"  ✓ {name}.png ({size[0]}x{size[1]})")
            generated_count += 1
        except Exception as e:
            print(f"  ✗ Error generating {name}.png: {e}")
    
    print(f"\n✓ Generated {generated_count} icons successfully!")
    print(f"✓ All icons saved to '{output_folder}/' folder")
    return generated_count

def main():
    """Main function to handle user input and process icons"""
    import sys
    
    print("=" * 60)
    print("Google Play Console Icon Generator")
    print("=" * 60)
    
    source_image = None
    output_folder = "app_icons"
    
    if len(sys.argv) > 1:
        # If argument provided, use it as local file path
        source_image = sys.argv[1]
        if not os.path.exists(source_image):
            print(f"✗ File not found: {source_image}")
            return
        print(f"\nUsing local file: {source_image}")
        
        # If second argument provided, use as output folder
        if len(sys.argv) > 2:
            output_folder = sys.argv[2]
    else:
        # Interactive mode
        print("\nChoose input source:")
        print("1. Local file")
        print("2. Google Cloud Storage")
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "2":
            # GCS mode
            bucket = input("Enter GCS bucket name: ").strip()
            blob_path = input("Enter icon path in bucket (e.g., icons/app-icon.png): ").strip()
            print("\nDownloading from Google Cloud Storage...")
            source_image = download_icon_from_gcs(bucket, blob_path)
        else:
            # Local file mode
            source_image = input("Enter path to your icon image: ").strip()
            if not os.path.exists(source_image):
                print(f"✗ File not found: {source_image}")
                return
        
        print()
        
        # Get output folder (optional)
        output_folder = input("Enter output folder name (default: app_icons): ").strip() or "app_icons"
    
    # Generate icons
    print(f"\nGenerating icons in '{output_folder}/'...\n")
    generate_app_icons(source_image, output_folder)
    
    # Cleanup temp file if it was downloaded from GCS
    if "google.cloud" in str(sys.modules) and os.path.exists("temp_icon.png"):
        os.remove("temp_icon.png")
    
    print("\n" + "=" * 60)
    print("Done! Your icons are ready for Google Play Console.")
    print("=" * 60)

if __name__ == "__main__":
    main()