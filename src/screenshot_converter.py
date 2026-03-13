from PIL import Image
import os
import sys
from pathlib import Path

# Google Play Console screenshot requirements
TARGET_RESOLUTIONS = {
    "16:9": [
        (1024, 576),
        (1280, 720),
        (1920, 1080),
        (2560, 1440),
    ],
    "9:16": [
        (1080, 1920),
        (1440, 2560),
    ]
}

def get_aspect_ratio(width, height):
    """Calculate aspect ratio and return as string"""
    from math import gcd
    g = gcd(width, height)
    w_ratio = width // g
    h_ratio = height // g
    return f"{w_ratio}:{h_ratio}", (width / height)

def convert_to_aspect_ratio(source_path, target_aspect, output_path=None, quality=95):
    """Convert screenshot to target aspect ratio by adding black bars or cropping"""
    
    try:
        img = Image.open(source_path)
        width, height = img.size
        current_ratio, current_decimal = get_aspect_ratio(width, height)
        
        print(f"Source: {width}×{height} ({current_ratio})")
        
        # Determine target dimensions
        if target_aspect == "16:9":
            target_w_h = 16 / 9
        elif target_aspect == "9:16":
            target_w_h = 9 / 16
        else:
            raise ValueError(f"Invalid aspect ratio: {target_aspect}")
        
        # Calculate if we need to crop or add bars
        if current_decimal > target_w_h:
            # Too wide, crop width or add height
            new_height = int(width / (16/9 if target_aspect == "16:9" else 9/16))
            if new_height > height:
                # Add black bars vertically
                new_img = Image.new('RGB', (width, new_height), (0, 0, 0))
                offset = (new_height - height) // 2
                new_img.paste(img, (0, offset))
                target_size = (width, new_height)
                print(f"Added black bars: {width}×{new_height} (16:9)")
            else:
                # Crop height
                offset = (height - new_height) // 2
                new_img = img.crop((0, offset, width, offset + new_height))
                target_size = (width, new_height)
                print(f"Cropped height: {width}×{new_height} (16:9)")
        else:
            # Too tall, add black bars horizontally or crop width
            new_width = int(height * (16/9 if target_aspect == "16:9" else 9/16))
            if new_width > width:
                # Add black bars horizontally
                new_img = Image.new('RGB', (new_width, height), (0, 0, 0))
                offset = (new_width - width) // 2
                new_img.paste(img, (offset, 0))
                target_size = (new_width, height)
                print(f"Added black bars: {new_width}×{height} (9:16)")
            else:
                # Crop width
                offset = (width - new_width) // 2
                new_img = img.crop((offset, 0, offset + new_width, height))
                target_size = (new_width, height)
                print(f"Cropped width: {new_width}×{height} (9:16)")
        
        # Save
        if output_path is None:
            stem = Path(source_path).stem
            ext = Path(source_path).suffix
            output_path = f"{stem}_converted{ext}"
        
        # Use appropriate save parameters
        if output_path.lower().endswith('.png'):
            new_img.save(output_path, 'PNG', optimize=True)
        else:
            new_img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        print(f"✓ Saved: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error: {e}")
        raise

def resize_to_target(source_path, target_dimension, output_path=None, quality=95):
    """Resize screenshot to target dimension"""
    
    try:
        img = Image.open(source_path)
        width, height = img.size
        
        print(f"Source: {width}×{height}")
        print(f"Target: {target_dimension[0]}×{target_dimension[1]}")
        
        # Resize
        resized = img.resize(target_dimension, Image.Resampling.LANCZOS)
        
        # Save
        if output_path is None:
            stem = Path(source_path).stem
            ext = Path(source_path).suffix
            output_path = f"{stem}_resized{ext}"
        
        if output_path.lower().endswith('.png'):
            resized.save(output_path, 'PNG', optimize=True)
        else:
            resized.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        print(f"✓ Saved: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error: {e}")
        raise

def batch_convert_directory(directory, target_aspect, quality=95):
    """Convert all screenshots in a directory"""
    
    if not os.path.isdir(directory):
        print(f"✗ Directory not found: {directory}")
        return
    
    files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            files.append(os.path.join(directory, filename))
    
    if not files:
        print(f"✗ No PNG or JPEG files found in {directory}")
        return
    
    print(f"Found {len(files)} screenshot(s) to convert...\n")
    
    for file_path in sorted(files):
        print(f"Processing: {os.path.basename(file_path)}")
        convert_to_aspect_ratio(file_path, target_aspect)
        print()

def main():
    """Main function"""
    print("=" * 60)
    print("Google Play Console Screenshot Converter")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python screenshot_converter.py <screenshot> <action>")
        print("\nActions:")
        print("  convert-16:9 <file>     Convert to 16:9 aspect ratio")
        print("  convert-9:16 <file>     Convert to 9:16 aspect ratio")
        print("  resize <file> WIDTHxHEIGHT  Resize to exact dimensions")
        print("\nExamples:")
        print("  python screenshot_converter.py screenshot.png convert-16:9")
        print("  python screenshot_converter.py screenshot.png resize 1920x1080")
        print("  python screenshot_converter.py ./screenshots convert-9:16")
        return
    
    target = sys.argv[1]
    
    if len(sys.argv) < 3:
        print("✗ Missing action. Use: convert-16:9, convert-9:16, or resize WIDTHxHEIGHT")
        return
    
    action = sys.argv[2]
    
    if os.path.isdir(target):
        # Directory mode
        if action.startswith("convert-"):
            aspect = action.split("-")[1]
            print(f"\nConverting all screenshots to {aspect}...\n")
            batch_convert_directory(target, aspect)
        else:
            print("✗ Resize action requires a specific file, not directory")
    
    elif os.path.isfile(target):
        # File mode
        print()
        
        if action.startswith("convert-"):
            aspect = action.split("-")[1]
            if aspect not in ["16:9", "9:16"]:
                print(f"✗ Invalid aspect ratio: {aspect}")
                return
            convert_to_aspect_ratio(target, aspect)
        
        elif action == "resize":
            if len(sys.argv) < 4:
                print("✗ Missing dimensions. Usage: resize WIDTHxHEIGHT")
                print("  Example: resize 1920x1080")
                return
            
            try:
                dim = sys.argv[3].split("x")
                if len(dim) != 2:
                    raise ValueError("Use WIDTHxHEIGHT format")
                target_dim = (int(dim[0]), int(dim[1]))
                resize_to_target(target, target_dim)
            except Exception as e:
                print(f"✗ Invalid dimensions: {e}")
                return
        
        else:
            print(f"✗ Unknown action: {action}")
            print("   Use: convert-16:9, convert-9:16, or resize WIDTHxHEIGHT")
    
    else:
        print(f"✗ File or directory not found: {target}")

if __name__ == "__main__":
    main()
