from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [req.strip() for req in f.readlines()]

with open("test_requirements.txt", "r", encoding="utf-8") as f:
    test_requirements = [req.strip() for req in f.readlines()]


setup(
    name="headtailx",
    version="0.0.1",
    author="Mitchell P. Krawiec-Thayer",
    author_email="headtailx@mitchellpkt.com",
    description="Extends `head` and `tail` commands to support previewing binary data formats",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mitchellpkt/headtailx",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": test_requirements,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "headx=headtailx.headx:main",
            "tailx=headtailx.tailx:main",
        ],
    },
)
