from PIL import Image
import os
import sys
from pathlib import Path

# Google Play Console screenshot requirements
REQUIREMENTS = {
    "formats": ["png", "jpg", "jpeg"],
    "max_file_size_mb": 8,
    "max_file_size_bytes": 8 * 1024 * 1024,
    "min_dimension": 320,
    "max_dimension": 3840,
    "aspect_ratios": {
        "16:9": (16, 9),
        "9:16": (9, 16),
    }
}

def get_file_size_mb(file_path):
    """Get file size in MB"""
    return os.path.getsize(file_path) / (1024 * 1024)

def get_image_dimensions(file_path):
    """Get image width and height"""
    try:
        img = Image.open(file_path)
        return img.width, img.height
    except Exception as e:
        return None, f"Error reading image: {e}"

def get_aspect_ratio(width, height):
    """Calculate aspect ratio and return as string"""
    if width is None or height is None:
        return None
    
    # Find GCD to simplify ratio
    from math import gcd
    g = gcd(width, height)
    w_ratio = width // g
    h_ratio = height // g
    return f"{w_ratio}:{h_ratio}", (width / height)

def check_format(file_path):
    """Check if file format is PNG or JPEG"""
    ext = Path(file_path).suffix.lower().lstrip('.')
    return ext in REQUIREMENTS["formats"], ext

def check_file_size(file_path):
    """Check if file size is within limit"""
    size_mb = get_file_size_mb(file_path)
    is_valid = size_mb <= REQUIREMENTS["max_file_size_mb"]
    return is_valid, size_mb

def check_dimensions(width, height):
    """Check if dimensions are within valid range"""
    if width is None or height is None:
        return False, "Cannot determine dimensions"
    
    issues = []
    if width < REQUIREMENTS["min_dimension"]:
        issues.append(f"Width {width}px is below minimum {REQUIREMENTS['min_dimension']}px")
    if height < REQUIREMENTS["min_dimension"]:
        issues.append(f"Height {height}px is below minimum {REQUIREMENTS['min_dimension']}px")
    if width > REQUIREMENTS["max_dimension"]:
        issues.append(f"Width {width}px exceeds maximum {REQUIREMENTS['max_dimension']}px")
    if height > REQUIREMENTS["max_dimension"]:
        issues.append(f"Height {height}px exceeds maximum {REQUIREMENTS['max_dimension']}px")
    
    return len(issues) == 0, issues if issues else f"{width}x{height}px ✓"

def check_aspect_ratio(width, height, target_ratios=None):
    """Check if aspect ratio matches 16:9 or 9:16"""
    if width is None or height is None:
        return False, "Cannot determine dimensions"
    
    if target_ratios is None:
        target_ratios = list(REQUIREMENTS["aspect_ratios"].keys())
    
    aspect_ratio, decimal_ratio = get_aspect_ratio(width, height)
    
    # Check against target ratios with some tolerance (1% for rounding)
    tolerance = 0.01
    valid_ratios = []
    
    for ratio_str in target_ratios:
        w, h = REQUIREMENTS["aspect_ratios"][ratio_str]
        target_decimal = w / h
        if abs(decimal_ratio - target_decimal) <= tolerance:
            valid_ratios.append(ratio_str)
    
    if valid_ratios:
        return True, f"{aspect_ratio} {valid_ratios}"
    else:
        return False, f"{aspect_ratio} (not 16:9 or 9:16)"

def validate_screenshot(file_path):
    """Validate a single screenshot against all requirements"""
    results = {
        "file": os.path.basename(file_path),
        "path": file_path,
        "valid": True,
        "checks": {}
    }
    
    # Check 1: File format
    format_valid, format_ext = check_format(file_path)
    results["checks"]["format"] = {
        "valid": format_valid,
        "message": f"{format_ext.upper()}" if format_valid else f"{format_ext.upper()} (must be PNG or JPEG)"
    }
    if not format_valid:
        results["valid"] = False
    
    # Check 2: File size
    try:
        size_valid, size_mb = check_file_size(file_path)
        results["checks"]["file_size"] = {
            "valid": size_valid,
            "message": f"{size_mb:.2f} MB" if size_valid else f"{size_mb:.2f} MB (max 8 MB)"
        }
        if not size_valid:
            results["valid"] = False
    except Exception as e:
        results["checks"]["file_size"] = {"valid": False, "message": f"Error: {e}"}
        results["valid"] = False
    
    # Check 3: Dimensions and aspect ratio
    width, height = get_image_dimensions(file_path)
    
    if isinstance(height, str):  # error message
        results["checks"]["dimensions"] = {"valid": False, "message": height}
        results["checks"]["aspect_ratio"] = {"valid": False, "message": "Cannot determine"}
        results["valid"] = False
    else:
        dim_valid, dim_msg = check_dimensions(width, height)
        results["checks"]["dimensions"] = {
            "valid": dim_valid,
            "message": dim_msg if isinstance(dim_msg, str) else " | ".join(dim_msg)
        }
        if not dim_valid:
            results["valid"] = False
        
        # Check 4: Aspect ratio
        ratio_valid, ratio_msg = check_aspect_ratio(width, height)
        results["checks"]["aspect_ratio"] = {
            "valid": ratio_valid,
            "message": ratio_msg
        }
        if not ratio_valid:
            results["valid"] = False
    
    return results

def print_results(results):
    """Pretty print validation results"""
    status = "✓ PASS" if results["valid"] else "✗ FAIL"
    print(f"\n{status} - {results['file']}")
    print("─" * 60)
    
    checks = results["checks"]
    for check_name, check_result in checks.items():
        icon = "✓" if check_result["valid"] else "✗"
        print(f"  {icon} {check_name.replace('_', ' ').title()}: {check_result['message']}")

def validate_directory(directory_path):
    """Validate all screenshots in a directory"""
    if not os.path.isdir(directory_path):
        print(f"✗ Directory not found: {directory_path}")
        return []
    
    valid_files = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            valid_files.append(os.path.join(directory_path, filename))
    
    if not valid_files:
        print(f"✗ No PNG or JPEG files found in {directory_path}")
        return []
    
    return sorted(valid_files)

def main():
    """Main function"""
    print("=" * 60)
    print("Google Play Console Screenshot Validator")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python screenshot_validator.py <file_or_directory>")
        print("\nExamples:")
        print("  python screenshot_validator.py ./screenshots/")
        print("  python screenshot_validator.py screenshot.png")
        return
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        # Validate single file
        results = validate_screenshot(target)
        print_results(results)
        
        if not results["valid"]:
            print("\n⚠ This screenshot does NOT meet Google Play Console requirements.")
            print("   See issues above.")
            sys.exit(1)
        else:
            print("\n✓ This screenshot is ready for Google Play Console!")
    
    elif os.path.isdir(target):
        # Validate directory
        files = validate_directory(target)
        
        if not files:
            print(f"\n✗ No valid image files found in {target}")
            sys.exit(1)
        
        print(f"\nFound {len(files)} screenshot(s) to validate...\n")
        
        all_results = []
        passed = 0
        failed = 0
        
        for file_path in files:
            results = validate_screenshot(file_path)
            all_results.append(results)
            print_results(results)
            
            if results["valid"]:
                passed += 1
            else:
                failed += 1
        
        # Summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Total screenshots: {len(files)}")
        print(f"✓ Passed: {passed}")
        print(f"✗ Failed: {failed}")
        
        if failed == 0:
            print("\n✓ All screenshots are ready for Google Play Console!")
        else:
            print(f"\n⚠ {failed} screenshot(s) need to be fixed before uploading.")
        
        # Show detailed requirements
        print("\n" + "=" * 60)
        print("GOOGLE PLAY CONSOLE REQUIREMENTS")
        print("=" * 60)
        print(f"Format: PNG or JPEG")
        print(f"Max File Size: {REQUIREMENTS['max_file_size_mb']} MB")
        print(f"Aspect Ratio: 16:9 or 9:16")
        print(f"Dimensions: Each side between {REQUIREMENTS['min_dimension']}—{REQUIREMENTS['max_dimension']} pixels")
        print(f"  - 16:9 typical: 1024×576, 1280×720, 1920×1080, 2560×1440")
        print(f"  - 9:16 typical: 1080×1920, 1440×2560")
        
        if failed > 0:
            sys.exit(1)
    
    else:
        print(f"✗ File or directory not found: {target}")
        sys.exit(1)

if __name__ == "__main__":
    main()
