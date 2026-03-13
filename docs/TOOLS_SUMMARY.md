# Google Play Console Tools Suite - Complete Reference

A comprehensive toolkit for preparing Android apps for Google Play Console submission.

## Available Tools

### 🎨 Icon Generator (`hy.py`)
**Generate all app icons from a single source image**

```bash
python hy.py [source_image] [output_folder]
```

**What it does:**
- Generates 22 icon sizes for all Android devices
- Creates app icons, adaptive icons, notification icons
- Generates Play Store listing and featured graphics
- Downloads icons from Google Cloud Storage (optional)

**Output:** 22 PNG files ready for Google Play Console

**Examples:**
```bash
python hy.py                              # Interactive mode
python hy.py app-icon.png                # Generate from local file
python hy.py app-icon.png my_icons       # Custom output folder
```

📖 **Full documentation:** [ICON_GENERATOR_README.md](ICON_GENERATOR_README.md)

---

### ✓ Screenshot Validator (`screenshot_validator.py`)
**Validate screenshots meet Google Play Console requirements**

```bash
python screenshot_validator.py <file_or_directory>
```

**What it checks:**
- ✓ Format (PNG or JPEG)
- ✓ File size (max 8 MB)
- ✓ Aspect ratio (16:9 or 9:16)
- ✓ Dimensions (320–3,840 px per side)
- ✓ Quantity (2–8 required)

**Output:** Pass/Fail validation report

**Examples:**
```bash
python screenshot_validator.py screenshot.png          # Single file
python screenshot_validator.py ./screenshots/          # Directory
```

📖 **Full documentation:** [SCREENSHOT_VALIDATOR_README.md](SCREENSHOT_VALIDATOR_README.md)

---

### 🔄 Screenshot Converter (`screenshot_converter.py`)
**Fix aspect ratio and resize screenshots**

```bash
python screenshot_converter.py <file_or_directory> <action>
```

**What it does:**
- Converts to 16:9 (landscape) aspect ratio
- Converts to 9:16 (portrait) aspect ratio
- Resizes to exact dimensions
- Adds black bars (letterboxing) when needed
- Batch processes entire directories

**Output:** Converted PNG/JPEG files

**Examples:**
```bash
# Convert single file to 16:9
python screenshot_converter.py screenshot.png convert-16:9

# Resize to exact dimensions
python screenshot_converter.py screenshot.png resize 1920x1080

# Batch convert directory to 9:16
python screenshot_converter.py ./screenshots convert-9:16
```

📖 **Full documentation:** [SCREENSHOT_CONVERTER_README.md](SCREENSHOT_CONVERTER_README.md)

---

## Quick Start Workflow

### Step 1: Generate Icons (5 minutes)
```bash
python hy.py ~/Downloads/app-icon.png
# ✓ Creates app_icons/ with 22 icon files
```

### Step 2: Prepare Screenshots (10 minutes)
```bash
# If screenshots need aspect ratio fix:
python screenshot_converter.py bad_screenshot.png convert-16:9

# Validate all screenshots:
python screenshot_validator.py ./screenshots/
```

### Step 3: Upload to Google Play Console (5 minutes)
1. Open [Google Play Console](https://play.google.com/console)
2. Select your app
3. Go to **Store listing** → **Icon** → Upload icons from `app_icons/`
4. Go to **Screenshots** → Upload 2–8 validated screenshots
5. Save and publish

---

## File Organization

```
.
├── TOOLS_SUMMARY.md                   ← You are here
├── GOOGLE_PLAY_CONSOLE_TOOLS.md       ← Overview & setup
├── ICON_GENERATOR_README.md           ← Icon generator docs
├── SCREENSHOT_VALIDATOR_README.md     ← Validator docs
├── SCREENSHOT_CONVERTER_README.md     ← Converter docs
│
├── hy.py                              ← Icon generator
├── screenshot_validator.py            ← Screenshot validator
├── screenshot_converter.py            ← Screenshot converter
├── requirements.txt                   ← Dependencies
│
├── app_icons/                         ← Generated icons folder
│   ├── playstore_icon_512.png
│   ├── app_icon_mdpi.png
│   ├── adaptive_icon_*.png
│   └── notification_icon_*.png
│
└── screenshots/                       ← Your app screenshots (optional)
    ├── screenshot_1.png
    ├── screenshot_2.png
    └── ...
```

---

## Google Play Console Requirements

### App Icons
| Requirement | Details |
|---|---|
| **Formats** | PNG with transparency |
| **Sizes Generated** | 22 different sizes (icons, adaptive, notifications) |
| **Submission** | All sizes generated automatically |

### Screenshots
| Requirement | Details |
|---|---|
| **Format** | PNG or JPEG |
| **Quantity** | 2–8 per language |
| **Aspect Ratio** | 16:9 (landscape) or 9:16 (portrait) |
| **Max Size** | 8 MB each |
| **Dimensions** | Each side: 320–3,840 pixels |
| **Recommended** | 1920×1080 (16:9) or 1080×1920 (9:16) |

---

## Common Tasks

### Task 1: Generate All Icon Sizes

```bash
python hy.py my-app-icon.png my_icons
# Output: 22 files in my_icons/ folder
# Ready for Google Play Console
```

### Task 2: Validate Screenshots

```bash
python screenshot_validator.py ./my_screenshots/
# Reports which screenshots pass/fail
# Shows specific issues for each file
```

### Task 3: Fix Aspect Ratio

```bash
# Screenshot is 4:3, needs to be 16:9
python screenshot_converter.py screenshot.png convert-16:9
# Creates: screenshot_converted.png (now 16:9)

# Validate it
python screenshot_validator.py screenshot_converted.png
```

### Task 4: Batch Fix Multiple Screenshots

```bash
# Convert all screenshots to 16:9
python screenshot_converter.py ./screenshots convert-16:9

# Validate all converted screenshots
python screenshot_validator.py ./screenshots
```

### Task 5: Download Icons from Cloud Storage

```bash
python hy.py
# Choose: Option 2 (Google Cloud Storage)
# Enter bucket name and icon path
# Icons downloaded and all 22 sizes generated
```

---

## Troubleshooting

### Icon Issues

❌ **"File not found"**
```bash
# Use absolute path
python hy.py /Users/username/Downloads/icon.png
```

❌ **"Google Cloud Storage error"**
```bash
# Set up authentication
gcloud auth application-default login
```

### Screenshot Issues

❌ **"Aspect ratio not 16:9"**
```bash
# Convert it
python screenshot_converter.py wrong.png convert-16:9
```

❌ **"File size > 8 MB"**
```bash
# PNG: Already optimized
# JPEG: Reduce quality in code (line 20: quality=85)
```

❌ **"Dimensions out of range"**
```bash
# Resize to safe dimensions
python screenshot_converter.py small.png resize 1920x1080
```

---

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Optional: Google Cloud Storage Setup

```bash
brew install google-cloud-sdk
gcloud auth application-default login
```

### 3. Verify Installation

```bash
python hy.py --help
python screenshot_validator.py --help
python screenshot_converter.py --help
```

---

## Tips & Best Practices

### Icons
✓ Use at least 512×512 source image  
✓ PNG with transparent background  
✓ Make icon recognizable at small sizes (36×36)  
✓ Test on different device sizes  

### Screenshots
✓ Show real app features first  
✓ First screenshot is featured — choose wisely  
✓ Use 2–5 best screenshots (quality over quantity)  
✓ Add text callouts to highlight features  
✓ Use consistent design language  
✓ Portrait (9:16) recommended for mobile  
✓ Landscape (16:9) for tablets/games  

### Workflow
✓ Generate icons first  
✓ Convert/fix screenshots second  
✓ Validate all before uploading  
✓ Keep original files as backup  
✓ Test in Google Play Console preview  

---

## Tool Features Matrix

| Feature | Icon Gen | Validator | Converter |
|---------|----------|-----------|-----------|
| Generate icons | ✓ | - | - |
| Validate format | - | ✓ | - |
| Validate size | - | ✓ | - |
| Check aspect ratio | - | ✓ | - |
| Fix aspect ratio | - | - | ✓ |
| Resize images | - | - | ✓ |
| Batch process | ✓ | ✓ | ✓ |
| GCS integration | ✓ | - | - |

---

## Support & Resources

### Google Play Console Official Docs
- [App Icons](https://support.google.com/googleplay/android-developer/answer/1078870)
- [Screenshots](https://support.google.com/googleplay/android-developer/answer/1233393)
- [Store Listing](https://support.google.com/googleplay/android-developer/answer/113156)

### Quick Links
- [Google Play Console](https://play.google.com/console)
- [Pillow Docs](https://pillow.readthedocs.io/) (image library)
- [Google Cloud Storage Docs](https://cloud.google.com/storage/docs)

---

## Advanced Usage

### Custom Python Script

If you want to use these tools in your own Python code:

```python
from hy import generate_app_icons
from screenshot_validator import validate_screenshot

# Generate icons
generate_app_icons('my-icon.png', 'output_folder')

# Validate screenshot
results = validate_screenshot('screenshot.png')
if not results['valid']:
    print(f"Issues: {results['checks']}")
```

### Batch Processing Script

```bash
#!/bin/bash
for img in base_images/*.png; do
    python hy.py "$img" "icons_$(basename $img .png)"
done

python screenshot_validator.py screenshots/
```

---

## Version Info

- **Python**: 3.7+
- **Pillow**: 9.0.0+
- **google-cloud-storage**: 2.0.0+ (optional)
- **Last Updated**: March 2026

---

## License

Open source. Use freely for your Google Play Console submissions.

---

**Happy releasing! 🚀**

For detailed information on specific tools, see:
- Icon Generator: [ICON_GENERATOR_README.md](ICON_GENERATOR_README.md)
- Screenshot Validator: [SCREENSHOT_VALIDATOR_README.md](SCREENSHOT_VALIDATOR_README.md)
- Screenshot Converter: [SCREENSHOT_CONVERTER_README.md](SCREENSHOT_CONVERTER_README.md)
