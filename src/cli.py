#!/usr/bin/env python3
"""
Google Play Console Tools Suite
Complete toolkit for Android app submission to Google Play Store

Quick Start:
    python hy.py                              # Generate icons
    python screenshot_validator.py ./ss/      # Validate screenshots
    python screenshot_converter.py file convert-16:9  # Fix aspect ratio
"""

import os
import sys

TOOLS = {
    "1": {
        "name": "Icon Generator",
        "file": "hy.py",
        "description": "Generate all Google Play Console icon sizes",
        "usage": "python hy.py [image] [output_folder]",
        "example": "python hy.py app-icon.png app_icons",
    },
    "2": {
        "name": "Screenshot Validator",
        "file": "screenshot_validator.py",
        "description": "Validate screenshots meet Google Play requirements",
        "usage": "python screenshot_validator.py <file_or_directory>",
        "example": "python screenshot_validator.py screenshots/",
    },
    "3": {
        "name": "Screenshot Converter",
        "file": "screenshot_converter.py",
        "description": "Fix aspect ratio and resize screenshots",
        "usage": "python screenshot_converter.py <file> <action>",
        "example": "python screenshot_converter.py screenshot.png convert-16:9",
    },
}

DOCS = {
    "Overview": "GOOGLE_PLAY_CONSOLE_TOOLS.md",
    "Icon Generator": "ICON_GENERATOR_README.md",
    "Screenshot Validator": "SCREENSHOT_VALIDATOR_README.md",
    "Screenshot Converter": "SCREENSHOT_CONVERTER_README.md",
    "Tools Summary": "TOOLS_SUMMARY.md",
    "Quick Reference": "QUICK_REFERENCE.md",
}


def print_header():
    """Print header"""
    print("\n" + "=" * 70)
    print("  GOOGLE PLAY CONSOLE TOOLS SUITE")
    print("  Android App Submission Toolkit")
    print("=" * 70 + "\n")


def print_menu():
    """Print main menu"""
    print("SELECT A TOOL:")
    print()
    for key, tool in TOOLS.items():
        print(f"  {key}. {tool['name']}")
        print(f"     {tool['description']}")
        print()


def print_docs_menu():
    """Print documentation menu"""
    print("DOCUMENTATION:")
    print()
    for i, (name, filename) in enumerate(DOCS.items(), 1):
        exists = "✓" if os.path.exists(filename) else "✗"
        print(f"  {i}. {exists} {name}")
        print(f"     → {filename}")
    print()


def print_quick_start():
    """Print quick start guide"""
    print("QUICK START (3 steps):")
    print()
    print("  Step 1: Generate icons")
    print("  $ python hy.py app-icon.png")
    print("  ↓")
    print("  Step 2: Prepare screenshots")
    print("  $ python screenshot_validator.py screenshots/")
    print("  ↓")
    print("  Step 3: Fix any issues")
    print("  $ python screenshot_converter.py bad.png convert-16:9")
    print()
    print("  Then upload to Google Play Console:")
    print("  ➜ https://play.google.com/console")
    print()


def print_requirements():
    """Print Google Play Console requirements"""
    print("REQUIREMENTS:")
    print()
    print("  Icons:")
    print("    • 512×512 minimum (PNG with transparency)")
    print("    • Generates 22 sizes automatically")
    print()
    print("  Screenshots:")
    print("    • 2–8 screenshots required")
    print("    • PNG or JPEG format")
    print("    • 16:9 or 9:16 aspect ratio")
    print("    • Max 8 MB each")
    print("    • 320–3,840 px per side")
    print()


def show_tool_help(tool_key):
    """Show help for specific tool"""
    if tool_key in TOOLS:
        tool = TOOLS[tool_key]
        print()
        print(f"TOOL: {tool['name']}")
        print("─" * 70)
        print(f"Description: {tool['description']}")
        print(f"File: {tool['file']}")
        print(f"Usage: {tool['usage']}")
        print(f"Example: {tool['example']}")
        print()
        print("For more info, see:")
        if tool['name'] == 'Icon Generator':
            print(f"  → ICON_GENERATOR_README.md")
        elif tool['name'] == 'Screenshot Validator':
            print(f"  → SCREENSHOT_VALIDATOR_README.md")
        elif tool['name'] == 'Screenshot Converter':
            print(f"  → SCREENSHOT_CONVERTER_README.md")
        print()


def main():
    """Main menu"""
    print_header()
    
    if len(sys.argv) > 1:
        # Command line argument
        arg = sys.argv[1].lower()
        
        if arg in ['--help', '-h', 'help']:
            print_menu()
            print_docs_menu()
            print_quick_start()
            print_requirements()
            return
        
        elif arg in TOOLS:
            show_tool_help(arg)
            return
        
        elif arg == 'info':
            print_quick_start()
            print_requirements()
            return
    
    # Interactive menu
    print_menu()
    print_docs_menu()
    
    print("\nOPTIONS:")
    print("  A. Quick Start Guide")
    print("  B. Requirements")
    print("  C. Exit")
    print()
    
    choice = input("Enter your choice (1-3, A-C): ").strip().upper()
    
    if choice in TOOLS:
        show_tool_help(choice)
    elif choice == 'A':
        print_quick_start()
    elif choice == 'B':
        print_requirements()
    elif choice == 'C':
        print("Goodbye!")
        return
    else:
        print("\n✗ Invalid choice")
        return
    
    print("\nTo run a tool directly:")
    for key, tool in TOOLS.items():
        print(f"  {tool['usage']}")


if __name__ == "__main__":
    main()
