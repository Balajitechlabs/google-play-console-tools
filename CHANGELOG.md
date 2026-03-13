# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-13

### Added
- **Icon Generator** - Generate all 22 Google Play Console icon sizes from a single source image
  - Support for PNG, JPEG, and other common formats
  - Google Cloud Storage integration for downloading icons
  - Supports transparent backgrounds
  - Generates adaptive icons for Android 8.0+
  - Creates notification icons for all DPI ranges

- **Screenshot Validator** - Validate screenshots meet all Google Play requirements
  - Check format (PNG or JPEG)
  - Verify file size (max 8 MB)
  - Confirm aspect ratio (16:9 or 9:16)
  - Validate dimensions (320–3,840 px per side)
  - Batch validate entire directories
  - Detailed pass/fail reports with specific issues

- **Screenshot Converter** - Fix aspect ratios and resize screenshots
  - Convert to 16:9 (landscape) aspect ratio
  - Convert to 9:16 (portrait) aspect ratio
  - Resize to exact dimensions
  - Add black bars (letterboxing) intelligently
  - Crop to maintain quality
  - Batch process entire directories
  - Support for PNG and JPEG

- **Complete Documentation**
  - Getting Started guide (START_HERE.md)
  - Quick Reference cheat sheet
  - Detailed tool-specific guides
  - Complete overview and workflow guide
  - Troubleshooting and FAQ

- **CLI Tools**
  - Command-line interface for all tools
  - Interactive menu system
  - Batch processing capabilities
  - Comprehensive help messages

### Features
- Python 3.7+ support
- Cross-platform (Windows, macOS, Linux)
- No GUI required - terminal-based for automation
- Minimal dependencies (Pillow + optional google-cloud-storage)
- MIT License - completely free and open source
- Production-ready and tested
- Detailed error messages with solutions

### Documentation
- README.md - Main project documentation
- START_HERE.md - Quick start guide
- QUICK_REFERENCE.md - Command cheat sheet
- Tool-specific guides in docs/
- Complete workflow examples
- Troubleshooting guides

### Installation
- pip installable from source
- Virtual environment support
- Optional Google Cloud Storage support
- Cross-platform executable scripts

## Planned Features

### Version 1.1.0 (Planned)
- [ ] Unit tests with pytest
- [ ] Integration tests
- [ ] Performance optimizations for large batch processing
- [ ] Additional output format support (WebP)
- [ ] Screenshot annotation tools
- [ ] Watermarking support

### Version 1.2.0 (Planned)
- [ ] GUI version (PyQt/Tkinter)
- [ ] Web interface
- [ ] Docker containerization
- [ ] Windows batch scripts (.bat)
- [ ] Shell scripts for Linux/macOS
- [ ] More cloud storage integrations (AWS S3, Azure)

### Version 2.0.0 (Planned)
- [ ] Mobile app companion
- [ ] Real-time monitoring
- [ ] Advanced screenshot editing
- [ ] AI-powered screenshot analysis
- [ ] Automated screenshot capture from app

## Known Issues

- None at release

## Support

For issues, feature requests, or questions:
1. Check [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)
2. Read tool-specific documentation in [docs/](docs/)
3. Open an issue on GitHub

## Contributors

- Balaji - Full Stack Developer (Initial release)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for full list.

---

## Version History

- **1.0.0** (2026-03-13) - Initial public release
  - All core features implemented
  - Complete documentation
  - Production-ready

---

[Unreleased]: https://github.com/Balajitechlabs/google-play-console-tools/compare/v1.0.0...develop
[1.0.0]: https://github.com/Balajitechlabs/google-play-console-tools/releases/tag/v1.0.0
