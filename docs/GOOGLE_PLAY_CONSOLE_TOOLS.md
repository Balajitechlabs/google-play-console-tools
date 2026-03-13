# Google Play Console Tools Suite

A complete toolkit for preparing and uploading your Android app to Google Play Console. Includes icon generation, icon validation, and screenshot validation.

## Tools Overview

### 1. **Icon Generator** (`hy.py`)
Generate all required Google Play Console icon sizes from a single source image.

- 📱 Generates 22 icon variants for ALL devices
- ☁️ Download from Google Cloud Storage
- 💾 Save to local directory
- ✓ Ready for Play Store listing

### 2. **Screenshot Validator** (`screenshot_validator.py`)
Validate your app screenshots meet Google Play Console requirements.

- ✓ Checks format (PNG/JPEG)
- ✓ Verifies file size (max 8 MB)
- ✓ Confirms aspect ratio (16:9 or 9:16)
- ✓ Validates dimensions (320–3,840 px)
- 📊 Batch validate entire directories
- 📋 Detailed validation reports

## Quick Start

### Installation

```bash
# Install all dependencies
pip install -r requirements.txt

# Optional: Set up Google Cloud Storage access
gcloud auth application-default login
```

### Generate Icons

```bash
# Interactive mode
python hy.py

# Or with local image
python hy.py ~/Downloads/app-icon.png

# Or with custom output folder
python hy.py app-icon.png my_play_icons
```

Generated icons are saved to `app_icons/` (or custom folder).

### Validate Screenshots

```bash
# Single screenshot
python screenshot_validator.py screenshot.png

# Entire folder
python screenshot_validator.py ./screenshots/
```

## Complete Workflow

### Step 1: Create/Upload Icon
```bash
# Option A: Use existing local icon
python hy.py ~/Downloads/app-icon.png

# Option B: Download from Google Cloud Storage
python hy.py
# Select option 2, enter bucket name and icon path
```

✅ Result: All 22 icon sizes in `app_icons/`

### Step 2: Prepare Screenshots
```bash
# Create screenshots folder
mkdir -p screenshots

# Add your PNG/JPEG screenshots (16:9 or 9:16 aspect ratio)
# Recommended: 1920×1080 (landscape) or 1080×1920 (portrait)

# Validate all screenshots
python screenshot_validator.py screenshots/
```

✅ Result: All screenshots validated and ready

### Step 3: Upload to Google Play Console

1. Open [Google Play Console](https://play.google.com/console)
2. Select your app
3. **Icon & Graphics** → Upload app icon from `app_icons/`
4. **Store listing** → **Screenshots** → Upload 2–8 screenshots
5. Reorder screenshots (first one is featured)
6. Save and review

## File Structure

```
.
├── hy.py                              # Icon generator
├── screenshot_validator.py             # Screenshot validator
├── requirements.txt                    # Dependencies
├── ICON_GENERATOR_README.md           # Icon generator docs
├── SCREENSHOT_VALIDATOR_README.md     # Screenshot validator docs
├── 
├── app_icons/                         # Generated icons (auto-created)
│   ├── playstore_icon_512.png
│   ├── app_icon_mdpi.png
│   ├── app_icon_hdpi.png
│   ├── adaptive_icon_*.png
│   └── notification_icon_*.png
│
└── screenshots/                       # Your screenshots (optional)
    ├── screenshot_1.png
    ├── screenshot_2.png
    └── ...
```

## Google Play Console Requirements

### Icons

| Size | Purpose | Details |
|---|---|---|
| 512×512 | Play Store Listing | PNG, transparent background |
| 1024×500 | Featured Image | Landscape, promotional |
| 36–192 px | App Icons | Various DPI (mdpi, hdpi, etc.) |
| 108–216 px | Adaptive Icons | Android 8.0+ |
| 20–96 px | Notifications | Different DPI variants |

### Screenshots

| Property | Requirement |
|---|---|
| Format | PNG or JPEG |
| Quantity | 2–8 screenshots |
| Aspect Ratio | 16:9 or 9:16 |
| Max File Size | 8 MB each |
| Dimensions | 320–3,840 px per side |
| Recommended | 1920×1080 or 1080×1920 |

## Examples

### Generate All Icons (Interactive)

```bash
python hy.py
# Choose option 1 for local file
# Enter path: /Users/you/icon.png
# Enter folder name: app_icons
```

### Batch Validate Screenshots

```bash
python screenshot_validator.py ./my_screenshots/

# Output:
# ✓ PASS - screenshot_1.png
# ✓ PASS - screenshot_2.png
# ✓ PASS - screenshot_3.png
# ...
# ✓ All screenshots are ready for Google Play Console!
```

### Upload from Cloud Storage

```bash
python hy.py
# Choose option 2 for Google Cloud Storage
# Enter bucket: my-app-assets
# Enter icon path: icons/app-logo.png
# Icons downloaded and generated!
```

## Troubleshooting

### Icon Generation Issues

❌ **"File not found"**
- Check the file path exists
- Use absolute path: `/full/path/to/icon.png`

❌ **"Command not found: gcloud"**
- Install Google Cloud SDK: `brew install google-cloud-sdk`

❌ **"Permission denied"** (GCS)
- Run: `gcloud auth application-default login`

### Screenshot Validation Issues

❌ **"Aspect ratio not 16:9 or 9:16"**
- Crop or resize screenshot to correct ratio
- Use: 1920×1080 (16:9) or 1080×1920 (9:16)

❌ **"File size exceeds 8 MB"**
- Compress PNG/JPEG
- Reduce quality or resolution

❌ **"Dimensions out of range"**
- Must be 320–3,840 px per side
- Resize to maintain aspect ratio

## Tips & Best Practices

### Icons
- ✓ Use at least 512×512 source image for quality
- ✓ PNG format with transparent background recommended
- ✓ Test on different devices (phone, tablet, watch)
- ✓ Make sure icon is recognizable at small sizes

### Screenshots
- ✓ Show real app features, not just generic text
- ✓ First screenshot is featured — make it count!
- ✓ Use 2–5 best screenshots (more isn't always better)
- ✓ Add text callouts to highlight features
- ✓ Use consistent design/fonts across all screenshots
- ✓ Portrait (9:16) is recommended for mobile apps

## Related Links

- [Google Play Console](https://play.google.com/console)
- [App Icons Requirements](https://support.google.com/googleplay/android-developer/answer/1078870)
- [Screenshots Requirements](https://support.google.com/googleplay/android-developer/answer/1233393)
- [Testing Your App](https://support.google.com/googleplay/android-developer/answer/113156)

## Dependencies

- **Pillow** — Image processing
- **google-cloud-storage** — Google Cloud Storage integration (optional)

## License

Open source. Use freely for your Google Play Console submissions.

## Support

For issues or improvements, check the individual tool documentation:
- [Icon Generator Docs](ICON_GENERATOR_README.md)
- [Screenshot Validator Docs](SCREENSHOT_VALIDATOR_README.md)
