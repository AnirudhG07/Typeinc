import os
from setuptools import setup, find_packages
import shutil, gzip
import platform 

def install_man_page():
    source_path = os.path.join("docs", "man", "typeinc.1")
    dest_path = os.path.join("/usr/local/", "share", "man", "man1", "typeinc.1.gz")

    # Compress the man page
    with open(source_path, 'rb') as src, gzip.open(dest_path, 'wb') as dst:
        shutil.copyfileobj(src, dst)

description="""
# Typeinc

Tyepinc, an ncurses based tool, is your goto terminal tool to play around with your typing speed with various difficulty levels.
You get an amazing UI for typing keyboard giving you a feel of both typewriters and keyboards.
Get your Tyepinc score and boast to your pals of your speed. Dream to achieve a Granddtypaa!

# Features

- Typing Speed Test where you can test your typing speed.
- Set your own difficulty level and test the abilities of your typing skills.
- Get your grade and Tyepinc score and boast to your pals of your speed.
- A cool UI of keyboard typing to give you a feel of both typewriters and keyboards.
- A user-friendly interface to make your typing experience more fun and interactive.
- View top 10 highscores(local) for each difficulty level.

# Installation
To install Typeinc, please fulfill the dependicies and run the following command:
```bash
pip install typeinc
```
To run the command, run the following command:
```bash
typeinc
```
And you are good to go!

## Dependencies
- Python 3.9 or higher
- ncurses library
- Other python libraries which will be installed automatically

Visit the Github Repository for more details: https://github.com/AnirudhG07/Typeinc

# Version
1.0.0

# Note:
1) The tool is developed using Python and ncurses library.
2) This tools is crossplatform for MacOS, Linux, Windows, etc.

"""

install_requires=[]

if platform.system() == 'Windows':
    install_requires.append('windows-curses')

setup(
    name='typeinc',
    version='1.0.0',
    description='Typeinc, an ncurses based tool, is your goto terminal tool to play around with your typing speed with various difficulty levels.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnirudhG07/Typeinc',
    author='Anirudh Gupta',
    packages=find_packages(),
    install_requires=install_requires,
    keywords=['terminal', 'typing speed test', 'typing', 'CLI'],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'typeinc=typeinc.main:main',
        ],
    },
    package_data={
        'typeinc': ['configurations/*', 'scores/*', 'wordlist.txt'],
    },
    include_package_data=True,
    classifiers=[   
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Everyone",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Typing Speed Test",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Windows",
    ],
)