from setuptools import find_packages, setup

# read the contents of README.md file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='laceworksdk',
    packages=find_packages(include=["laceworksdk", "laceworksdk.*"]),
    version='0.9.3',
    license='MIT',
    description='Community-developed Python SDK for the Lacework APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alan Nix',
    author_email='alan.nix@lacework.net',
    url='https://github.com/alannix-lw/lacework-python-sdk',
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
    ],
)
