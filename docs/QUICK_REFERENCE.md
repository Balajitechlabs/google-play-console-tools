# Google Play Console Tools - Quick Reference Card

## 🚀 Quick Commands

### Generate Icons
```bash
python hy.py app-icon.png
```
**Result**: 22 icon files in `app_icons/` folder

### Validate Screenshots
```bash
python screenshot_validator.py ./screenshots/
```
**Result**: Pass/Fail report for each screenshot

### Fix Screenshot Aspect Ratio
```bash
python screenshot_converter.py screenshot.png convert-16:9
```
**Result**: `screenshot_converted.png` (fixed aspect ratio)

### Resize Screenshot to Exact Size
```bash
python screenshot_converter.py screenshot.png resize 1920x1080
```
**Result**: `screenshot_resized.png` (exact dimensions)

---

## 📋 Requirements Checklist

### Before Upload

- [ ] Icon: Generated from `hy.py` (all 22 sizes)
- [ ] Screenshots: 2–8 total
- [ ] Screenshots: PNG or JPEG format
- [ ] Screenshots: 16:9 or 9:16 aspect ratio
- [ ] Screenshots: 320–3,840 px per side
- [ ] Screenshots: Max 8 MB each
- [ ] Screenshots: Validated with `screenshot_validator.py`

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Wrong aspect ratio | `python screenshot_converter.py file.png convert-16:9` |
| File too large | Reduce quality or use PNG compression |
| Dimensions wrong | `python screenshot_converter.py file.png resize 1920x1080` |
| Multiple files | `python screenshot_validator.py directory/` |
| GCS error | `gcloud auth application-default login` |

---

## 📐 Common Dimensions

### Landscape (16:9)
- 1024×576 (minimum recommended)
- **1280×720** (720p - popular)
- **1920×1080** (Full HD - recommended)
- 2560×1440 (2K)
- 3840×2160 (4K - maximum)

### Portrait (9:16)
- 576×1024 (minimum recommended)
- **1080×1920** (Full HD - recommended)
- 1440×2560 (2K)
- 2160×3840 (4K - maximum)

---

## 🎨 Icon Sizes Generated

| Icon Type | Sizes |
|-----------|-------|
| Play Store | 512×512, 1024×500 |
| App Icons | 36×36 to 192×192 (6 sizes) |
| Adaptive Icons | 108×108, 162×162, 216×216 |
| Notifications | 20×20 to 96×96 (11 sizes) |
| **Total** | **22 files** |

---

## 📁 File Organization

```
my_app_project/
├── app-icon.png              ← Your source icon
├── hy.py                     ← Icon generator
├── screenshot_validator.py   ← Validator
├── screenshot_converter.py   ← Converter
│
├── app_icons/                ← Generated icons
│   └── playstore_icon_512.png
│
└── screenshots/              ← Your screenshots
    ├── home_screen.png
    ├── features.png
    └── details.png
```

---

## 🔄 Complete Workflow

```
1. Generate Icons
   └─> python hy.py icon.png
       └─> app_icons/ folder created

2. Prepare Screenshots
   ├─> python screenshot_converter.py bad.png convert-16:9
   └─> python screenshot_validator.py screenshots/
       └─> All validated ✓

3. Upload to Google Play Console
   ├─> Add icons from app_icons/
   ├─> Add screenshots
   └─> Publish!
```

---

## ⚠️ Common Mistakes

❌ Screenshot is 4:3 aspect ratio  
→ `python screenshot_converter.py file.png convert-16:9`

❌ File size 15 MB  
→ Compress image (reduce quality)

❌ Dimensions 2048×1536 (not in specs)  
→ `python screenshot_converter.py file.png resize 1920x1080`

❌ Wrong format (BMP, TIFF, etc.)  
→ Convert to PNG or JPEG first

❌ Different dimensions for each screenshot  
→ Use `resize` to make them consistent

---

## 💡 Pro Tips

✓ Use **1920×1080** for all 16:9 screenshots  
✓ Use **1080×1920** for all 9:16 screenshots  
✓ First screenshot is featured → choose wisely  
✓ Use only 2–5 screenshots (quality > quantity)  
✓ Add text callouts to highlight features  
✓ Keep background consistent  
✓ Test icons on multiple device sizes  
✓ Portrait (9:16) for mobile apps  
✓ Landscape (16:9) for tablets/games  

---

## 🆘 Help Commands

```bash
python hy.py
# Shows usage and options

python screenshot_validator.py
# Shows usage and requirements

python screenshot_converter.py
# Shows conversion options and examples
```

---

## 🌐 Useful Links

- Google Play Console: https://play.google.com/console
- Icon Guidelines: https://support.google.com/googleplay/android-developer/answer/1078870
- Screenshot Guidelines: https://support.google.com/googleplay/android-developer/answer/1233393

---

## ✅ Pre-Launch Checklist

Before submitting to Google Play Console:

- [ ] All 22 icons generated and quality-checked
- [ ] 2–8 screenshots selected
- [ ] All screenshots 16:9 or 9:16 aspect ratio
- [ ] All screenshots validated (all ✓ marks)
- [ ] App title, description, and keywords complete
- [ ] Privacy policy URL set
- [ ] Contact email provided
- [ ] Screenshots ordered (best first)
- [ ] No personal information in screenshots
- [ ] Icons visible on different backgrounds
- [ ] Ready to publish!

---

**Version**: March 2026  
**Status**: Ready for Production  
**Tools**: 3 (Icon Generator, Validator, Converter)
