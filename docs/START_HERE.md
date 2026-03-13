# 📱 Google Play Console Tools Suite

**A complete, production-ready toolkit for preparing Android apps for Google Play Console submission.**

Generate app icons, validate screenshots, and fix aspect ratios — all from the command line.

---

## ⚡ 30-Second Quick Start

```bash
# 1. Generate all icon sizes from one image
python hy.py app-icon.png

# 2. Validate your screenshots
python screenshot_validator.py screenshots/

# 3. Fix any aspect ratio issues
python screenshot_converter.py bad-screenshot.png convert-16:9

# 4. Upload to Google Play Console
# https://play.google.com/console
```

---

## 🎯 What This Does

| Tool | Purpose | Output |
|---|---|---|
| **Icon Generator** | Create 22 icon sizes from one image | App icons, adaptive icons, notifications |
| **Screenshot Validator** | Check screenshots meet Google Play requirements | Pass/Fail report with specific issues |
| **Screenshot Converter** | Fix aspect ratio and resize screenshots | Corrected PNG/JPEG files |

All tools work together to prepare your app for Google Play Console submission in minutes.

---

## 📦 What's Included

### Python Tools (3 total)
- `hy.py` — Icon generator (22 sizes)
- `screenshot_validator.py` — Validates screenshots
- `screenshot_converter.py` — Resizes & fixes aspect ratios
- `index.py` — Interactive menu system

### Documentation (6 guides)
- `GOOGLE_PLAY_CONSOLE_TOOLS.md` — Complete overview
- `ICON_GENERATOR_README.md` — Icon generator detailed guide
- `SCREENSHOT_VALIDATOR_README.md` — Validator detailed guide
- `SCREENSHOT_CONVERTER_README.md` — Converter detailed guide
- `TOOLS_SUMMARY.md` — All tools reference
- `QUICK_REFERENCE.md` — Quick cheat sheet

### Configuration
- `requirements.txt` — Python dependencies

---

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Windows / Mac / Linux all work the same
```

### Optional: Google Cloud Storage Support

If you want to download icons from Google Cloud Storage:

```bash
# Install Google Cloud SDK
brew install google-cloud-sdk  # macOS
# or for other OS: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth application-default login
```

---

## 🛠️ Tool Overview

### 1️⃣ Icon Generator (`hy.py`)

Generate all 22 Google Play Console icon sizes from a single source image.

```bash
# Interactive mode
python hy.py

# With local image
python hy.py ~/Downloads/app-icon.png

# With custom output folder
python hy.py app-icon.png my_icons
```

**Generates:**
- ✓ Play Store listing icons (512×512, 1024×500)
- ✓ App icons for all DPI (36×36 to 192×192)
- ✓ Adaptive icons (Android 8.0+)
- ✓ Notification icons (20×20 to 96×96)
- ✓ **Total: 22 PNG files ready to upload**

**Supports:**
- Local files
- Google Cloud Storage (GCS)
- All common image formats
- Transparent backgrounds

---

### 2️⃣ Screenshot Validator (`screenshot_validator.py`)

Validate your app screenshots meet all Google Play Console requirements.

```bash
# Single screenshot
python screenshot_validator.py screenshot.png

# Entire directory
python screenshot_validator.py ./screenshots/
```

**Checks:**
- ✓ Format (PNG or JPEG)
- ✓ File size (max 8 MB)
- ✓ Aspect ratio (16:9 or 9:16)
- ✓ Dimensions (320–3,840 px per side)
- ✓ Detailed pass/fail reports

**Output:**
```
✓ PASS - screenshot.png
  ✓ Format: PNG
  ✓ File Size: 2.5 MB
  ✓ Dimensions: 1920x1080px ✓
  ✓ Aspect Ratio: 16:9 ['16:9']
```

---

### 3️⃣ Screenshot Converter (`screenshot_converter.py`)

Fix aspect ratios and resize screenshots to meet Google Play requirements.

```bash
# Convert to 16:9
python screenshot_converter.py screenshot.png convert-16:9

# Convert to 9:16
python screenshot_converter.py screenshot.png convert-9:16

# Resize to exact dimensions
python screenshot_converter.py screenshot.png resize 1920x1080

# Batch convert directory
python screenshot_converter.py ./screenshots convert-16:9
```

**Features:**
- Adds black bars (letterboxing) when needed
- Crops intelligently to maintain quality
- Batch processes entire directories
- Preserves image quality (PNG and JPEG)

---

## 📋 Complete Workflow

### Step 1: Generate Icons (5 min)

```bash
python hy.py ~/my-app-icon.png
# Creates: app_icons/ with 22 PNG files
# Ready for Google Play Console
```

### Step 2: Prepare Screenshots (10 min)

```bash
# Create screenshots folder
mkdir screenshots

# Add your app screenshots (PNG or JPEG)
# Recommended: 1920×1080 (16:9) or 1080×1920 (9:16)

# Validate all screenshots
python screenshot_validator.py screenshots/
```

### Step 3: Fix Issues (if needed)

```bash
# If aspect ratio is wrong:
python screenshot_converter.py bad-screenshot.png convert-16:9

# If size is wrong:
python screenshot_converter.py screenshot.png resize 1920x1080

# Re-validate
python screenshot_validator.py screenshot_converted.png
```

### Step 4: Upload to Google Play Console (5 min)

1. Go to [Google Play Console](https://play.google.com/console)
2. Select your app
3. **Store listing** → **Icon** → Upload icons from `app_icons/`
4. **Store listing** → **Screenshots** → Upload 2–8 validated screenshots
5. Save and publish

---

## 📐 Google Play Console Requirements

### Icons

| Requirement | Details |
|---|---|
| **Format** | PNG (transparent background) |
| **Source Size** | Minimum 512×512 |
| **Generated Sizes** | 22 different sizes (all automatic) |
| **Submission** | All sizes generated by this tool |

### Screenshots

| Requirement | Details |
|---|---|
| **Quantity** | 2–8 screenshots per language |
| **Format** | PNG or JPEG |
| **Aspect Ratio** | 16:9 (landscape) or 9:16 (portrait) |
| **Max File Size** | 8 MB each |
| **Dimensions** | Each side: 320–3,840 pixels |
| **Recommended** | 1920×1080 or 1080×1920 |

---

## 💡 Best Practices

### Icons
✓ Use at least 512×512 source image  
✓ PNG format with transparent background  
✓ Simple, recognizable at small sizes  
✓ Test on different device types  
✓ Make sure icon works on light and dark backgrounds  

### Screenshots
✓ Choose 2–5 best screenshots (quality over quantity)  
✓ First screenshot is featured — choose wisely!  
✓ Show real app features and functionality  
✓ Use consistent design language across all screenshots  
✓ Add text callouts to highlight key features  
✓ Portrait (9:16) recommended for mobile apps  
✓ Landscape (16:9) good for tablets and games  
✓ Use same dimensions for all (e.g., all 1920×1080)  

---

## 🔍 Common Issues & Solutions

### Problem: Wrong Aspect Ratio

```bash
# Screenshot is 4:3, needs 16:9
python screenshot_converter.py screenshot.png convert-16:9

# Result: Black bars added, keeps content visible
```

### Problem: File Size Too Large

```bash
# PNG: Already optimized automatically
# JPEG: Reduce quality in code or use image editor
```

### Problem: Dimensions Out of Range

```bash
# Screenshot too small or too large
python screenshot_converter.py screenshot.png resize 1920x1080

# Now exactly 1920×1080 pixels
```

### Problem: Wrong Format

```bash
# Convert BMP/TIFF to PNG first
# Then validate and upload
```

---

## 🎮 Usage Examples

### Generate Icons Only
```bash
python hy.py my-icon.png my-app-icons
# Output: my-app-icons/ with 22 PNG files
```

### Validate Entire Screenshot Folder
```bash
python screenshot_validator.py ./my-screenshots/

# Output:
# ✓ PASS - screenshot1.png
# ✓ PASS - screenshot2.png
# ✗ FAIL - screenshot3.png (aspect ratio)
# ✗ FAIL - screenshot4.png (too large)
# Summary: 2 passed, 2 failed
```

### Fix Multiple Screenshots
```bash
# Convert all 4:3 screenshots to 16:9
python screenshot_converter.py ./screenshots convert-16:9

# Then validate all converted files
python screenshot_validator.py ./screenshots

# All fixed!
```

### Download Icons from Cloud Storage
```bash
python hy.py
# Choose: Option 2 (Google Cloud Storage)
# Enter: Bucket name and icon path
# Result: Icons downloaded and 22 sizes generated
```

---

## 📚 Documentation

| File | Purpose |
|---|---|
| `GOOGLE_PLAY_CONSOLE_TOOLS.md` | Complete setup and workflow guide |
| `ICON_GENERATOR_README.md` | Icon generator detailed documentation |
| `SCREENSHOT_VALIDATOR_README.md` | Validator detailed documentation |
| `SCREENSHOT_CONVERTER_README.md` | Converter detailed documentation |
| `TOOLS_SUMMARY.md` | Complete reference for all tools |
| `QUICK_REFERENCE.md` | Quick cheat sheet and commands |

**Start here:** Read `QUICK_REFERENCE.md` for quick commands

---

## 🔧 Advanced Usage

### Using in Your Own Python Code

```python
from hy import generate_app_icons
from screenshot_validator import validate_screenshot

# Generate icons
generate_app_icons('my-icon.png', 'icons-output')

# Validate screenshot
results = validate_screenshot('screenshot.png')
if results['valid']:
    print("Screenshot is ready!")
else:
    print(f"Issues: {results['checks']}")
```

### Batch Processing Script

```bash
#!/bin/bash
# generate_all.sh

echo "Generating icons..."
python hy.py app-icon.png app_icons

echo "Converting screenshots..."
python screenshot_converter.py ./raw-screenshots convert-16:9

echo "Validating all screenshots..."
python screenshot_validator.py ./raw-screenshots

echo "Done! Ready for Google Play Console."
```

---

## 📊 File Structure

```
your-app-folder/
├── app-icon.png                        ← Your source icon
├── hy.py                               ← Icon generator
├── screenshot_validator.py             ← Validator
├── screenshot_converter.py             ← Converter
├── requirements.txt                    ← Dependencies
├── QUICK_REFERENCE.md                  ← Quick help
│
├── app_icons/                          ← Generated icons
│   ├── playstore_icon_512.png
│   ├── app_icon_mdpi.png
│   ├── adaptive_icon_108.png
│   └── ... (22 total)
│
└── screenshots/                        ← Your screenshots
    ├── screen-1.png
    ├── screen-2.png
    └── ...
```

---

## ⚡ Quick Commands Reference

```bash
# Generate all icons
python hy.py app-icon.png

# Validate one screenshot
python screenshot_validator.py screenshot.png

# Validate all screenshots
python screenshot_validator.py ./screenshots/

# Fix aspect ratio (16:9)
python screenshot_converter.py screenshot.png convert-16:9

# Fix aspect ratio (9:16)
python screenshot_converter.py screenshot.png convert-9:16

# Resize to exact size
python screenshot_converter.py screenshot.png resize 1920x1080

# Batch fix all screenshots in folder
python screenshot_converter.py ./screenshots convert-16:9
```

---

## 🆘 Troubleshooting

### Python Not Found
```bash
# Use python3 instead of python
python3 hy.py app-icon.png
```

### Package Not Found
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt
```

### Permission Denied
```bash
# Make script executable
chmod +x hy.py screenshot_validator.py screenshot_converter.py

# Then run
python hy.py app-icon.png
```

### Google Cloud Storage Error
```bash
# Authenticate first
gcloud auth application-default login

# Then try again
python hy.py
```

---

## 📞 Support & Resources

### Official Google Play Console
- [Google Play Console](https://play.google.com/console)
- [Icon Requirements](https://support.google.com/googleplay/android-developer/answer/1078870)
- [Screenshot Guidelines](https://support.google.com/googleplay/android-developer/answer/1233393)

### Image Format Specs
- [Pillow Documentation](https://pillow.readthedocs.io/) (image processing library)
- [Google Cloud Storage](https://cloud.google.com/storage/docs) (optional, for icon hosting)

---

## 🎓 Learning Resources

1. **Quick Start**: Read `QUICK_REFERENCE.md` (2 min)
2. **Setup**: Follow this README (5 min)
3. **Generate Icons**: Run `python hy.py` (2 min)
4. **Validate Screenshots**: Run `python screenshot_validator.py ./ss/` (1 min)
5. **Upload**: [Google Play Console](https://play.google.com/console) (5 min)

**Total Time**: ~15 minutes from start to submission!

---

## 📦 Dependencies

- **Pillow** (9.0.0+) — Image processing
- **google-cloud-storage** (2.0.0+) — Google Cloud Storage access (optional)

All automatically installed via `requirements.txt`.

---

## ✅ Pre-Launch Checklist

Before uploading to Google Play Console:

- [ ] Icons generated (all 22 sizes in `app_icons/`)
- [ ] 2–8 screenshots selected
- [ ] All screenshots validated (all ✓ pass)
- [ ] Consistent dimensions (all same size)
- [ ] App title and description complete
- [ ] Privacy policy URL added
- [ ] Contact email provided
- [ ] Screenshots ordered (best first)
- [ ] No personal data in screenshots
- [ ] Tested in Google Play Console preview

---

## 🚀 Ready to Launch?

1. **Run**: `python index.py --help` to see all tools
2. **Generate**: `python hy.py app-icon.png` to create icons
3. **Validate**: `python screenshot_validator.py ./screenshots/` to check screenshots
4. **Upload**: Go to [Google Play Console](https://play.google.com/console)
5. **Publish**: Follow the console upload wizard

**Your app will be ready in minutes!**

---

## 📄 License

Open source. Use freely for your Google Play Console submissions.

---

## 🏆 Version Info

- **Version**: 1.0 (Production Ready)
- **Updated**: March 2026
- **Python**: 3.7+
- **Status**: ✓ Tested and verified

---

**Questions?** Check the detailed documentation files included in this package.

**Ready to submit?** Go to [Google Play Console](https://play.google.com/console)

**Quick help?** Run: `python index.py --help`

Happy releasing! 🎉
