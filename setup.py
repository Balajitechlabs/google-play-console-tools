#!/usr/bin/env python
"""
Setup configuration for Google Play Console Tools
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="google-play-console-tools",
    version="1.0.0",
    author="Balaji - Full Stack Developer",
    author_email=\"admin@tech.balajitechlab.com\",
    description="Complete toolkit for preparing Android apps for Google Play Console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Balajitechlabs/google-play-console-tools",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["icon_generator", "screenshot_validator", "screenshot_converter", "cli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gpc-tools=cli:main",
            "gpc-icons=icon_generator:main",
            "gpc-validate=screenshot_validator:main",
            "gpc-convert=screenshot_converter:main",
        ],
    },
    include_package_data=True,
)
