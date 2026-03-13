# Contributing to Google Play Console Tools

Thank you for your interest in contributing! This document provides guidelines and instructions.

## Code of Conduct

- Be respectful and inclusive
- Support other community members
- Focus on constructive feedback
- Respect diverse perspectives

## How to Contribute

### Reporting Bugs

**Before submitting a bug report:**
- Check existing issues
- Test with the latest version
- Collect as much information as possible

**Include in bug report:**
- Python version (`python --version`)
- Operating system
- Exact error message
- Steps to reproduce
- Expected vs actual behavior

**Example:**
```
Title: Icon generator crashes with large JPEG files

Description:
When processing a 5MB JPEG image, the tool crashes with:
  MemoryError: Unable to allocate 2.5 GiB for array

Steps to reproduce:
1. python src/icon_generator.py large-image.jpg
2. Error occurs immediately

Environment:
- Python 3.9.7
- macOS 12.3
- Pillow 9.0.1
```

### Suggesting Enhancements

**Before suggesting:**
- Check if already suggested
- Explain the use case
- Provide examples if possible

**Include in suggestion:**
- Clear description of feature
- Why this would be useful
- Potential implementation approach

### Submitting Changes

#### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/Balajitechlabs/google-play-console-tools.git
cd google-play-console-tools

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt
```

#### Make Your Changes

```bash
# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes
# Test extensively
git add .
git commit -m "Add your descriptive commit message"
```

#### Commit Message Guidelines

- Use clear, descriptive messages
- Start with a verb (Add, Fix, Improve, etc.)
- Keep first line under 50 characters
- Reference issues with #123

**Examples:**
```
Add screenshot batch processing feature
Fix aspect ratio calculation for 21:9 aspect ratios
Improve error handling in icon generator
```

#### Testing

Before submitting:

```bash
# Test icon generator
python src/icon_generator.py test-icon.png

# Test validator
python src/screenshot_validator.py screenshots/

# Test converter
python src/screenshot_converter.py screenshot.png convert-16:9
```

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Update README.md** if functionality changes
4. **Follow code style** (PEP 8)
5. **Provide clear description** of changes
6. **Link related issues** with `Fixes #123`

**PR Template:**
```markdown
## Description
Brief description of changes

## Related Issue
Fixes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How did you test this?

## Screenshots (if applicable)
Any relevant screenshots
```

## Development Guidelines

### Code Style

Follow PEP 8:
```python
# Good
def generate_icons(source_path, output_folder="app_icons"):
    """Generate all icon sizes from source image."""
    os.makedirs(output_folder, exist_ok=True)
    # ... code

# Bad
def generate_icons(source_path,output_folder="app_icons"):
    #generate icons
    os.makedirs(output_folder,exist_ok=True)
```

### Documentation

- Add docstrings to functions
- Comment complex logic
- Keep README.md updated
- Document CLI arguments

```python
def validate_screenshot(file_path):
    """
    Validate a single screenshot against Google Play requirements.
    
    Args:
        file_path: Path to the screenshot file
        
    Returns:
        dict: Validation results with 'valid', 'checks', and details
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a valid image
    """
    # Implementation
```

### Testing

While automated tests aren't required yet, test:
- Common use cases
- Edge cases
- Different file types
- Error conditions

## Project Structure

```
src/
├── icon_generator.py       # Icon generation logic
├── screenshot_validator.py # Validation logic
├── screenshot_converter.py # Conversion/resize logic
└── cli.py                  # Command-line interface

docs/
├── START_HERE.md          # Getting started
├── QUICK_REFERENCE.md     # Quick help
└── [tool guides]          # Detailed documentation
```

## Areas for Contribution

### High Priority
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Performance optimizations
- [ ] Windows batch file scripts
- [ ] Docker support

### Medium Priority
- [ ] Additional image formats (WebP, AVIF)
- [ ] Batch watermarking for screenshots
- [ ] Screenshot annotation tools
- [ ] Cloud storage integrations

### Low Priority
- [ ] GUI version
- [ ] Web interface
- [ ] Mobile app

## Questions?

- Check [docs/START_HERE.md](docs/START_HERE.md)
- Read existing issues and discussions
- Open a new issue to ask questions

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- GitHub contributor list

Thank you for contributing! 🎉
