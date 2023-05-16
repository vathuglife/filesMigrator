# Welcome to Files Migrator!

## Introduction
This is a desktop application that can gather all files from different destinations, as well as organize them into specific folders for easier access. The project also 
allows me to understand how a GUI app works on the Desktop environment, getting used to the Python syntax, as well as some Object-Oriented Concepts. 

Since this is one of my very first projects, the files organization is so horrendous that it could easily disturb viewers. So...take care! (heheh...)

## Technologies used
Just Kivy (a Python framework).

## Motivation
The idea of this application stemmed from the hassle of searching for a specific file with a specific format (e.g. abc.zip) in a folder containing different formats (e.g. .zip, .img, .exe...). We can eliminate this problem by building an application that filters out files by their format, then organize them into respective folders (e.g. .zip files into Zip folder...)

## Project/Build Status
1.4 (Deprecated)

## Code Style
Single-file (not recommended)

## Use examples
### Main Menu
Where all options of the app is displayed.
![image](https://github.com/vathuglife/filesMigrator/assets/99245931/ed5f3af1-1f51-4437-89e4-7823796ba14e)
### Customize Directories
To add more source directories, simply click on the Plus sign, then choose an appropriate source.
![image](https://github.com/vathuglife/filesMigrator/assets/99245931/98c7ee95-63f5-42bd-9d9e-52bddd66cbb4)
### Change Destination
![image](https://github.com/vathuglife/filesMigrator/assets/99245931/31213ccf-21f5-47d0-929d-baf27f286334)
### Customizing extensions
Adds more extension to each file category 
![image](https://github.com/vathuglife/filesMigrator/assets/99245931/aeea0e39-0071-4ef7-93f6-b7fc1e5f4cea)
### Reorganize files
For example, you have a file called **A.EXE** lying inside the **Audio** folder. This is incorrect since **A is an Executable file, NOT an Audio file**,
so what this feature does is to move incorrectly placed files to their appropriate folders.

## Features
- Add different folders to gather files from
- Customize extensions for each category (e.g. Images category might contain .png, .img,...)
- Choose the destination to migrate the files to
- Migrate the files (of course)

## How to use
Before doing anything, here are a couple of dependencies that need to be installed:
- Python (version 3.9.1)
- Kivy (version 2.1, can be installed via CMD using the command: `python -m pip install "kivy[base,media]" kivy_examples`)
- KivyMD (version 0.104.2, can be installed via CMD using the command: `python -m pip install kivymd==0.104.2`)
- Auto Py to Exe (Windows CMD command: `python -m pip install auto-py-to-exe`)

+ Step 1: After pulling the source code from GitHub, open up the terminal and type: `auto-py-to-exe`.
+ Step 2: In the Script Location section, browse to the folder containing the **migratorGUI.py** file.
+ Step 3: In the Onefile section, choose **One File** option.
+ Step 4: In the Console Window section, Choose the **Window Based** option.
+ Step 5: In the Additional Files section, choose the **Add Folder** option, then select the **folder containing the migratorGUI.py** file (It should be the ver1.4 folder).
+ Step 6: In the Advanced Options, choose the **hidden-imports** section, then click the plus button once more to show a total of 2 entries. Then for each entry, type in: `plyer.platforms.win.notification`, `plyer.platforms.win.filechooser`
+ Step 7: In the Settings section, **Output Directory** option, browse to the folder where you want the final EXE file to be created.
+ Step 8: Click **Convert PY to EXE** and you are done!
