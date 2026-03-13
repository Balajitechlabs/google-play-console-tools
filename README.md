# 🎨 Google Play Console Tools

**Complete toolkit for preparing Android apps for Google Play Console submission.**

Generate app icons, validate screenshots, and fix aspect ratios — all from the command line. Production-ready, well-tested, and fully documented.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![FMHY](https://img.shields.io/badge/Listed-FMHY-orange)

---

## ⚡ Quick Start

```bash
# 1. Clone and install
git clone https://github.com/Balajitechlabs/google-play-console-tools.git
cd google-play-console-tools
pip install -r requirements.txt

# 2. Generate all icon sizes from one image
python src/icon_generator.py app-icon.png

# 3. Validate your screenshots
python src/screenshot_validator.py screenshots/

# 4. Fix aspect ratio issues
python src/screenshot_converter.py bad-screenshot.png convert-16:9

# 5. Upload to Google Play Console
# https://play.google.com/console
```

---

## 📦 What's Included

### 3 Powerful Tools

| Tool | Purpose | Output |
|---|---|---|
| **Icon Generator** | Create all 22 Google Play icon sizes from one image | Ready-to-upload PNG files |
| **Screenshot Validator** | Validate screenshots meet all Google Play requirements | Detailed pass/fail report |
| **Screenshot Converter** | Fix aspect ratios and resize screenshots | Corrected JPEG/PNG files |

### Complete Documentation

- 📖 [Getting Started](docs/START_HERE.md) — Start here!
- 🔧 [Tool Guides](docs/) — Detailed documentation for each tool
- ⚡ [Quick Reference](docs/QUICK_REFERENCE.md) — Cheat sheet
- 📚 [Full Overview](docs/GOOGLE_PLAY_CONSOLE_TOOLS.md) — Complete guide

---

## 🚀 Features

✅ Generate **22 icon sizes** automatically (Play Store, app icons, adaptive icons, notifications)  
✅ Download icons from **Google Cloud Storage**  
✅ Validate against all **Google Play requirements**  
✅ Fix **aspect ratio issues** (16:9 or 9:16)  
✅ Batch process **entire directories**  
✅ Detailed **error reporting** with solutions  
✅ **No dependencies** except Pillow  
✅ Works on **Windows, macOS, Linux**  
✅ MIT License - **Completely free**  
✅ Production-ready and **battle-tested**  

---

## 📋 Requirements

### Icons
- Format: PNG (transparent background)
- Source size: Minimum 512×512
- Generates: 22 different sizes automatically

### Screenshots
- Quantity: 2–8 per language
- Format: PNG or JPEG
- Aspect ratio: 16:9 or 9:16
- Max size: 8 MB each
- Dimensions: 320–3,840 px per side
- Recommended: 1920×1080 or 1080×1920

---

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (comes with Python)

### Install from source

```bash
# Clone the repository
git clone https://github.com/Balajitechlabs/google-play-console-tools.git
cd google-play-console-tools

# Install dependencies
pip install -r requirements.txt

# (Optional) Install for system-wide access
pip install -e .
```

### Install from pip (coming soon)

```bash
pip install google-play-console-tools
```

### Optional: Google Cloud Storage support

```bash
# Install Google Cloud SDK
brew install google-cloud-sdk  # macOS
# or follow: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth application-default login
```

---

## 📖 Usage

### Icon Generator

Generate all icon sizes from a single image:

```bash
# Interactive mode
python src/icon_generator.py

# With local image
python src/icon_generator.py app-icon.png

# With custom output folder
python src/icon_generator.py app-icon.png my_icons
```

**Generates:**
- Play Store listing icons (512×512, 1024×500)
- App icons (36×36 to 192×192)
- Adaptive icons (108×108 to 216×216)
- Notification icons (20×20 to 96×96)

### Screenshot Validator

Validate screenshots meet all requirements:

```bash
# Single screenshot
python src/screenshot_validator.py screenshot.png

# Entire directory
python src/screenshot_validator.py ./screenshots/
```

**Checks:**
- Format (PNG or JPEG)
- File size (max 8 MB)
- Aspect ratio (16:9 or 9:16)
- Dimensions (320–3,840 px)

### Screenshot Converter

Fix aspect ratios and resize:

```bash
# Convert to 16:9 (landscape)
python src/screenshot_converter.py screenshot.png convert-16:9

# Convert to 9:16 (portrait)
python src/screenshot_converter.py screenshot.png convert-9:16

# Resize to exact dimensions
python src/screenshot_converter.py screenshot.png resize 1920x1080

# Batch convert directory
python src/screenshot_converter.py ./screenshots convert-16:9
```

---

## 🎯 Complete Workflow

### Step 1: Prepare Icons

```bash
python src/icon_generator.py ~/my-app-icon.png
# Creates: app_icons/ with 22 PNG files
```

### Step 2: Prepare Screenshots

```bash
# Place screenshots in a folder
mkdir screenshots
# Add your PNG or JPEG screenshots

# Validate all
python src/screenshot_validator.py screenshots/

# Fix any issues
python src/screenshot_converter.py bad.png convert-16:9

# Re-validate
python src/screenshot_validator.py screenshots/
```

### Step 3: Upload to Google Play Console

1. Go to [Google Play Console](https://play.google.com/console)
2. Select your app
3. **Store listing** → **Icon** → Upload `app_icons/`
4. **Store listing** → **Screenshots** → Upload validated screenshots
5. Save and publish

**Done! Your app is ready for submission.** 🚀

---

## 📁 Project Structure

```
google-play-console-tools/
├── README.md                           # This file
├── LICENSE                             # MIT License
├── requirements.txt                    # Dependencies
├── setup.py                            # Installation config
├── .gitignore                          # Git ignore rules
│
├── src/                                # Python source code
│   ├── icon_generator.py              # Generate icons (22 sizes)
│   ├── screenshot_validator.py        # Validate screenshots
│   ├── screenshot_converter.py        # Convert/resize screenshots
│   └── cli.py                         # Command-line interface
│
├── docs/                               # Documentation
│   ├── START_HERE.md                  # Quick start guide
│   ├── QUICK_REFERENCE.md             # Command cheat sheet
│   ├── GOOGLE_PLAY_CONSOLE_TOOLS.md   # Complete overview
│   ├── ICON_GENERATOR_README.md       # Icon generator guide
│   ├── SCREENSHOT_VALIDATOR_README.md # Validator guide
│   ├── SCREENSHOT_CONVERTER_README.md # Converter guide
│   └── TOOLS_SUMMARY.md               # Full reference
│
└── examples/                           # Example files
    └── [sample screenshots]
```

---

## 💡 Tips & Best Practices

### Icons
✅ Use at least 512×512 source image  
✅ PNG with transparent background  
✅ Simple and recognizable at small sizes  
✅ Test on different device types  

### Screenshots
✅ Show real features, not generic text  
✅ First screenshot is featured — choose wisely!  
✅ Use 2–5 best screenshots (quality > quantity)  
✅ Consistent design language  
✅ Add text callouts to highlight features  
✅ Portrait (9:16) for mobile apps  
✅ Landscape (16:9) for tablets/games  

---

## 🐛 Troubleshooting

### "Python not found"
```bash
# Use python3
python3 src/icon_generator.py app-icon.png
```

### "Format error"
```bash
# Convert image to PNG first
# Then run the tools
```

### "Aspect ratio not 16:9"
```bash
# Use the converter
python src/screenshot_converter.py screenshot.png convert-16:9
```

### "Google Cloud Storage error"
```bash
# Authenticate first
gcloud auth application-default login
```

See [QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) for more troubleshooting.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📊 Project Stats

- ✅ **3 Tools** — Icon generator, validator, converter
- ✅ **7 Guides** — Comprehensive documentation
- ✅ **22 Icon Sizes** — All Google Play sizes
- ✅ **Production Ready** — Tested and verified
- ✅ **Open Source** — MIT License

---

## 🔗 Useful Links

- [Google Play Console](https://play.google.com/console) — Submit your app
- [Icon Requirements](https://support.google.com/googleplay/android-developer/answer/1078870) — Official specs
- [Screenshot Guidelines](https://support.google.com/googleplay/android-developer/answer/1233393) — Official guide
- [Pillow Docs](https://pillow.readthedocs.io/) — Image processing library
- [Listed on FMHY](https://github.com/fmhy/FMHY/issues/103) — Free Media HyperYeah community
- [FMHY Submission Details](FMHY_SUBMISSION.md) — Community listing documentation

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Free to use, modify, and distribute for any purpose.

---

## 👨‍💻 About

Created by **Balaji - Full Stack Developer**

- Portfolio: [https://tech.balajitechlab.com/](https://tech.balajitechlab.com/)
- GitHub: [@Balajitechlabs](https://github.com/Balajitechlabs)

---

## ⭐ Show Your Support

If this tool helped you, please:
- ⭐ Star this repository
- 📢 Share with other developers
- 🐛 Report bugs or suggest features
- 🤝 Contribute improvements

---

## 🎓 Getting Help

1. **Start here**: Read [docs/START_HERE.md](docs/START_HERE.md)
2. **Quick help**: Check [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)
3. **Detailed guide**: See tool-specific docs in [docs/](docs/)
4. **Issues**: Open an issue if you need help

---

**Ready to submit your app?** Start with [docs/START_HERE.md](docs/START_HERE.md) 🚀
