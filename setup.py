import os

from setuptools import find_packages, setup


PACKAGE_NAME = "laceworksdk"

project_root = os.path.abspath(os.path.dirname(__file__))

# Read the contents of README.md file
with open(os.path.join(project_root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read the version from version.py file
version = {}
with open(os.path.join(project_root, PACKAGE_NAME, 'version.py'), encoding='utf-8') as f:
    exec(f.read(), version)

setup(
    name='laceworksdk',
    packages=find_packages(include=["laceworksdk", "laceworksdk.*"]),
    version=version['__version__'],
    license='MIT',
    description='Community-developed Python SDK for the Lacework APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alan Nix',
    author_email='alan.nix@lacework.net',
    url='https://github.com/alannix-lw/python-sdk',
    download_url='https://pypi.python.org/pypi/laceworksdk',
    keywords=['lacework', 'api', 'sdk', 'python', 'api'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
