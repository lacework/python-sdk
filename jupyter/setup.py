import os

from setuptools import find_packages, setup

from laceworkjupyter import version


PACKAGE_NAME = "laceworkjupyter"

project_root = os.path.abspath(os.path.dirname(__file__))

# Read the contents of README.md file
with open(os.path.join(project_root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="laceworkjupyter",
    packages=find_packages(include=["laceworkjupyter", "laceworkjupyter.*"]),
    license="MIT",
    description=(
        "Community-developed Jupyter helper for the Lacework Python SDK"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kristinn Gudjonsson",
    author_email="kristinn.gudjonsson@lacework.net",
    version=version.get_version(),
    url="https://github.com/lacework/python-sdk",
    download_url="https://pypi.python.org/pypi/laceworkjupyter",
    keywords=[
        "lacework", "api", "sdk", "python", "api", "jupyter", "notebook"],
    include_package_data=True,
    install_requires=[
        "python-dotenv",
        "requests",
        "pyyaml",
        "laceworksdk",
        "ipywidgets",
        "mitreattack-python",
        "pandas"
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
