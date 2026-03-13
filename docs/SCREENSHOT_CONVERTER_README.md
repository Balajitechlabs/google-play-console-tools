# Google Play Console Screenshot Converter

Convert and resize app screenshots to meet Google Play Console requirements. Fix aspect ratio issues by adding black bars or resizing.

## Features

✓ Convert to 16:9 aspect ratio (landscape)  
✓ Convert to 9:16 aspect ratio (portrait)  
✓ Resize to exact dimensions  
✓ Add black bars (letterboxing) when needed  
✓ Crop intelligently to maintain quality  
✓ Batch convert entire directories  
✓ Preserve quality (PNG and JPEG support)  

## When to Use

- Screenshots have wrong aspect ratio (4:3, 21:9, etc.)
- Need to resize to match Google Play Console specs
- Want to add black borders to incorrect dimensions
- Converting entire batch of screenshots

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Convert Single Screenshot to 16:9

```bash
python screenshot_converter.py screenshot.png convert-16:9
```

Output: `screenshot_converted.png` (added/cropped to 16:9 ratio)

### Convert Single Screenshot to 9:16

```bash
python screenshot_converter.py screenshot.png convert-9:16
```

Output: `screenshot_converted.png` (added/cropped to 9:16 ratio)

### Resize to Exact Dimensions

```bash
python screenshot_converter.py screenshot.png resize 1920x1080
```

Output: `screenshot_resized.png` (resized to exactly 1920×1080)

### Batch Convert Directory to 16:9

```bash
python screenshot_converter.py ./screenshots convert-16:9
```

Converts all PNG/JPEG files in the directory to 16:9, saves as `filename_converted.png`

### Batch Convert Directory to 9:16

```bash
python screenshot_converter.py ./screenshots convert-9:16
```

Converts all files in directory to 9:16 aspect ratio.

## Recommended Dimensions

### Landscape (16:9)
- **Minimum**: 1024×576
- **Recommended**: 1920×1080 or 2560×1440
- **Maximum**: 3840×2160

### Portrait (9:16)
- **Minimum**: 576×1024
- **Recommended**: 1080×1920 or 1440×2560
- **Maximum**: 2160×3840

## How It Works

### Mode: Add Black Bars (Letterboxing)

If your screenshot is too wide or too tall, the converter adds black bars:

```
Before (4:3):        After (16:9):
┌──────────────┐    ┌─────────────────────┐
│              │    │█████████████████████│
│  Screenshot  │ → │    Screenshot       │
│              │    │█████████████████████│
└──────────────┘    └─────────────────────┘
```

### Mode: Crop

If adding bars would make the image too large, intelligent cropping is used:

```
Before (21:9):       After (16:9):
┌──────────────────────────────┐    ┌──────────────────┐
│  Screenshot Area    Content  │ → │  Screenshot Area │
└──────────────────────────────┘    └──────────────────┘
    (cropped from center)
```

## Examples

### Fix a 4:3 Screenshot

```bash
# Original: 1024×768 (4:3)
python screenshot_converter.py old_screenshot.png convert-16:9
# Result: 1365×768 (16:9) with black bars on sides
```

### Convert to Standard HD

```bash
# Resize to 1920×1080 (Full HD)
python screenshot_converter.py screenshot.png resize 1920x1080
# Result: 1920×1080 (perfect for Play Store)
```

### Batch Process Multiple Screenshots

```bash
mkdir -p my_screenshots
# Add all your screenshots to my_screenshots/

# Convert all to portrait (9:16)
python screenshot_converter.py my_screenshots convert-9:16

# Result: my_screenshots contain original + converted versions
```

### Workflow: Convert → Validate

```bash
# 1. Convert your screenshots
python screenshot_converter.py bad_screenshot.png convert-16:9

# 2. Validate the result
python screenshot_validator.py screenshot_converted.png

# 3. If valid, upload to Google Play Console!
```

## Quality Settings

The converter uses high quality settings by default:

- **PNG**: Optimized (~95% quality)
- **JPEG**: 95% quality factor

To adjust (advanced):
Edit the script and change the `quality` parameter in function calls from `95` to your desired value (0-100).

## Troubleshooting

### Result is wrong aspect ratio

The converter uses intelligent detection. If results are unexpected:
1. Check source image is valid
2. Try explicit resize instead: `resize 1920x1080`

### Output image is blurry

- Adjust source image resolution before converting
- Use `resize` mode instead if known target dimensions

### File size too large

- Converter is lossy for JPEG, lossless for PNG
- For JPEG: `quality` parameter in code
- For PNG: Use external compression tools

### Black bars look wrong

- This is expected! They're added to maintain aspect ratio
- Alternative: crop to exact dimensions with `resize`

## Comparison: Convert vs Resize

| Action | Use When | Result |
|--------|----------|--------|
| `convert-16:9` | Need 16:9 ratio, any size | Adds/crops to 16:9, preserves original size where possible |
| `convert-9:16` | Need 9:16 ratio, any size | Adds/crops to 9:16, preserves original size where possible |
| `resize 1920x1080` | Need exact dimensions | Stretches/squeezes to exactly 1920×1080 |

## Batch Processing Script

For processing many screenshots at once:

```bash
#!/bin/bash
# convert_all.sh

for file in screenshots/*.png screenshots/*.jpg; do
    echo "Converting: $file"
    python screenshot_converter.py "$file" convert-16:9
done

echo "All converted! Validating..."
python screenshot_validator.py screenshots/
```

## Tips

✓ Always validate after conversion: `python screenshot_validator.py`  
✓ Keep original files as backup before converting  
✓ Use consistent dimensions across all screenshots (e.g., all 1920×1080)  
✓ Portrait (9:16) recommended for mobile apps  
✓ Landscape (16:9) good for tablets and games  
✓ Test converted screenshots on multiple devices  

## Integration with Other Tools

This tool works with:
- **Icon Generator**: `python hy.py` — Generate app icons
- **Screenshot Validator**: `python screenshot_validator.py` — Validate screenshots

Complete workflow:
```bash
# 1. Generate icons
python hy.py app-icon.png

# 2. Convert screenshots
python screenshot_converter.py bad_screenshot.png convert-16:9

# 3. Validate screenshots
python screenshot_validator.py screenshot_converted.png

# 4. Upload to Google Play Console
# Open: https://play.google.com/console
```

## Related Links

- [Google Play Console Screenshots Guide](https://support.google.com/googleplay/android-developer/answer/1233393)
- [Screenshot Best Practices](https://support.google.com/googleplay/android-developer/answer/9844778)
