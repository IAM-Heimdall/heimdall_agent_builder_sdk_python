# setup.py
from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="heimdall-agent-builder-sdk",
    version="0.2.0",
    author="IAM Heimdall Team",
    author_email="team@iamheimdall.com",
    description="Python SDK for Agent Builders to interact with Heimdall AIF Core Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IAM-Heimdall/heimdall-agent-builder-sdk-python",
    packages=find_packages(exclude=["tests", "examples", "docs"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ]
    },
    keywords="aif agent identity token jwt authentication",
    project_urls={
        "Bug Reports": "https://github.com/IAM-Heimdall/heimdall-agent-builder-sdk-python/issues",
        "Source": "https://github.com/IAM-Heimdall/heimdall-agent-builder-sdk-python",
    },
)