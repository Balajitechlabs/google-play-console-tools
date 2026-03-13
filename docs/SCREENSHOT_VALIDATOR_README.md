# Google Play Console Screenshot Validator

Validate your app screenshots to ensure they meet Google Play Console requirements before uploading.

## Features

✓ Validates format (PNG or JPEG)  
✓ Checks file size (max 8 MB)  
✓ Verifies aspect ratio (16:9 or 9:16)  
✓ Confirms dimensions (320–3,840 px per side)  
✓ Batch validate entire directories  
✓ Detailed report for each screenshot  

## Google Play Console Requirements

| Requirement | Details |
|---|---|
| **Format** | PNG or JPEG |
| **File Size** | Maximum 8 MB each |
| **Aspect Ratio** | 16:9 (landscape) or 9:16 (portrait) |
| **Dimensions** | Each side: 320–3,840 pixels |
| **Quantity** | 2–8 screenshots per language |

### Recommended Resolutions

- **Landscape (16:9)**: 1024×576, 1280×720, 1920×1080, 2560×1440
- **Portrait (9:16)**: 1080×1920, 1440×2560

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Validate Single Screenshot

```bash
python screenshot_validator.py /path/to/screenshot.png
```

### Validate Directory (Multiple Screenshots)

```bash
python screenshot_validator.py ./screenshots/
```

The validator will check all PNG and JPEG files in the directory and provide a summary report.

## Example Output

```
✓ PASS - screenshot_1920x1080.png
────────────────────────────────────────────────────────────
  ✓ Format: PNG
  ✓ File Size: 0.01 MB
  ✓ Dimensions: 1920x1080px ✓
  ✓ Aspect Ratio: 16:9 ['16:9']

✓ This screenshot is ready for Google Play Console!
```

## Batch Validation Example

```bash
mkdir -p my_screenshots
# Add your PNG/JPEG screenshots to my_screenshots/
python screenshot_validator.py my_screenshots/
```

```
SUMMARY
============================================================
Total screenshots: 8
✓ Passed: 8
✗ Failed: 0

✓ All screenshots are ready for Google Play Console!
```

## Common Issues & Fixes

### ✗ Aspect Ratio Not 16:9 or 9:16

If your screenshot is wrong aspect ratio, you need to crop or resize it.

**Quick fix**: Add black bars or crop to correct ratio.

Example with Python:

```python
from PIL import Image

img = Image.open('screenshot.png')
width, height = img.size

# Force to 16:9
target_height = int(width * 9 / 16)
# Crop from center
top = (height - target_height) // 2
img = img.crop((0, top, width, top + target_height))
img.save('screenshot_16-9.png')
```

### ✗ File Size Exceeds 8 MB

Compress using a tool or Python:

```python
from PIL import Image

img = Image.open('screenshot.png')
img.save('screenshot_compressed.png', quality=85, optimize=True)
```

### ✗ Dimensions Out of Range

- **Too small**: Must be at least 320×180 (16:9) or 180×320 (9:16)
- **Too large**: Cannot exceed 3840 pixels on any side

Resize using:

```bash
python -c "
from PIL import Image
img = Image.open('screenshot.png')
img.thumbnail((3840, 3840), Image.Resampling.LANCZOS)
img.save('screenshot_resized.png')
"
```

## Uploading to Google Play Console

After validation passes:

1. Go to [Google Play Console](https://play.google.com/console)
2. Select your app
3. Go to **Store listing** → **Screenshots**
4. Upload 2–8 screenshots
5. Reorder by dragging (first screenshot is featured)
6. Add optional short descriptions
7. Save

## Tips

- Use clear, representative screenshots showing key app features
- First screenshot is shown as a preview — make it count!
- Use consistent design language across all screenshots
- Add text callouts to highlight features
- Test on different screen sizes
- Portrait (9:16) is recommended for mobile apps
- Landscape (16:9) good for tablets or games

## Environment Variables

```bash
export SCREENSHOTS_DIR="./my_screenshots"
python screenshot_validator.py $SCREENSHOTS_DIR
```

## Related Tools

- **Icon Generator**: `python hy.py` — Generate all Google Play Console icon sizes
- **Screenshot Validator**: `python screenshot_validator.py` — Validate screenshots (this tool)
