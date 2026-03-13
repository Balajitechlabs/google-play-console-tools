# Examples

This folder contains example files and sample output from the Google Play Console Tools.

## What's Here

### Screenshots

Sample screenshots showing before and after using the tools:

- `original/` - Original screenshots with issues
- `converted/` - Converted screenshots ready for Google Play

### Icons

Sample icon generation output:
- `icons/` - Complete set of 22 generated icons

## Using These Examples

### 1. Validate Screenshots

```bash
python src/screenshot_validator.py examples/original/
```

See which screenshots pass and which fail validation.

### 2. Fix Issues

```bash
python src/screenshot_converter.py examples/original/screenshot.png convert-16:9
```

Convert screenshots to correct aspect ratio.

### 3. Re-validate

```bash
python src/screenshot_validator.py examples/converted/
```

Verify converted screenshots are ready for Google Play.

## Quick Test

To quickly test the tools:

```bash
# 1. Generate icons from example image
python src/icon_generator.py examples/sample-icon.png examples/sample-output-icons

# 2. Validate sample screenshots
python src/screenshot_validator.py examples/original/

# 3. Fix any issues
python src/screenshot_converter.py examples/original/sample.png convert-16:9

# 4. Verify result
python src/screenshot_validator.py examples/converted/
```

## Create Your Own Examples

To contribute example files:

1. Create a folder with your examples
2. Test the tools against your examples
3. Document what you're testing
4. Submit a PR with your examples

## File Structure

```
examples/
├── README.md                    # This file
├── original/
│   ├── screenshot-1.jpeg       # Original screenshots (may have issues)
│   └── screenshot-2.jpeg
├── converted/
│   ├── screenshot-1_converted.jpeg    # Fixed screenshots
│   └── screenshot-2_converted.jpeg
└── icons/
    ├── app-icon-512.png        # Example generated icons
    └── ... (22 files total)
```

## Tips for Testing

- **Test different aspect ratios** (16:9, 9:16, 4:3, 21:9, etc.)
- **Test different file sizes** (small and large files)
- **Test different formats** (PNG, JPEG)
- **Test batch processing** (multiple files at once)
- **Test edge cases** (minimum sizes, maximum sizes)

## Contributing Examples

Found a case the tools don't handle well? 

1. Document the issue
2. Include example files
3. Submit via GitHub issue or PR

This helps improve the tools for everyone!

---

**Ready to test?** Start with the Quick Test section above!

For detailed usage, see the main [README.md](../README.md) or documentation in [docs/](../docs/).
