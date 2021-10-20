import os

from setuptools import find_packages, setup


PACKAGE_NAME = "laceworksdk"

project_root = os.path.abspath(os.path.dirname(__file__))

# Read the contents of README.md file
with open(os.path.join(project_root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="laceworksdk",
    packages=find_packages(include=["laceworksdk", "laceworksdk.*"]),
    license="MIT",
    description="Community-developed Python SDK for the Lacework APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alan Nix",
    author_email="alan.nix@lacework.net",
    use_scm_version={"write_to": "laceworksdk/version.py"},
    setup_requires=["setuptools_scm"],
    url="https://github.com/lacework/python-sdk",
    download_url="https://pypi.python.org/pypi/laceworksdk",
    keywords=["lacework", "api", "sdk", "python", "api"],
    install_requires=[
        "python-dotenv",
        "bleach",
        "requests",
        "configparser",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
