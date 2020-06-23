from setuptools import find_packages, setup

setup(
    name='laceworksdk',
    packages=find_packages(include=["laceworksdk", "laceworksdk.*"]),
    version='0.1.1',
    license='MIT',
    description='Community-developed Python SDK for the Lacework APIs',
    author='Alan Nix',
    author_email='alan.nix@lacework.net',
    url='https://github.com/alannix-lw/lacework-python-sdk',
    download_url='https://pypi.python.org/pypi/laceworksdk',
    keywords=['lacework', 'api', 'sdk', 'python', 'api'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
