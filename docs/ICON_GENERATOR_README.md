# Google Play Console Icon Generator

Generate all required Google Play Console icons from a single source image. Supports downloading icons from Google Cloud Storage and generates all device-specific sizes automatically.

## Features

✓ Download icons directly from Google Cloud Storage (GCS)  
✓ Generate 20+ icon sizes for all Android devices  
✓ Support for adaptive icons (Android 8.0+)  
✓ Notification icons for various DPIs  
✓ Play Store list and featured image sizes  
✓ Easy-to-use interactive mode or command-line  

## Required Icon Sizes Generated

- **Play Store Console**: 512x512, 1024x500 (featured)
- **App Icons**: 36x36, 48x48, 72x72, 96x96, 144x144, 192x192, 512x512
- **Adaptive Icons**: 108x108, 162x162, 216x216
- **Notification Icons**: 20x20 to 96x96 (multiple DPI variants)

## Installation

```bash
pip install -r requirements.txt
```

### Google Cloud Storage Setup (Optional)

If you want to download icons from GCS:

1. Install Google Cloud SDK:
   ```bash
   brew install google-cloud-sdk  # macOS
   ```

2. Set up authentication:
   ```bash
   gcloud auth application-default login
   ```

   Or set the environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
   ```

## Usage

### Option 1: Interactive Mode

```bash
python hy.py
```

Then choose:
- `1` for local file
- `2` for Google Cloud Storage

### Option 2: Command Line with Local File

```bash
python hy.py /path/to/your/icon.png
```

### Option 3: From Google Cloud Storage (Interactive)

After running `python hy.py`, select option `2` and enter:
- GCS bucket name: `my-bucket`
- Icon path in bucket: `icons/app-icon.png`

## Example

```bash
# Download from GCS and generate all icons
python hy.py

# Or use a local file
python hy.py ~/Downloads/my-app-icon.png
```

This will create an `app_icons/` directory with all generated icons ready for Google Play Console.

## Output Structure

```
app_icons/
├── playstore_icon_512.png
├── playstore_featured_1024x500.png
├── app_icon_mdpi.png
├── app_icon_hdpi.png
├── app_icon_xhdpi.png
├── app_icon_xxhdpi.png
├── app_icon_xxxhdpi.png
├── adaptive_icon_foreground_108.png
├── adaptive_icon_foreground_162.png
├── notification_icon_24.png
└── ... (and more)
```

## Requirements

- Python 3.7+
- Pillow (for image processing)
- google-cloud-storage (for GCS support)

## Tips

- Source image should be at least 512x512 pixels for best quality
- PNG format recommended
- Ensure your source image has transparent background for adaptive icons
- All generated icons are PNG format (transparent background supported)

## Environment Variables

Set these to avoid entering credentials repeatedly:

```bash
export GCS_BUCKET="my-bucket"
export GCS_ICON_PATH="icons/app-icon.png"
```
