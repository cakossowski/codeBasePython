# What is this?

Not a dream of a teenage girl, but some sort of log, where I write down my "achievements" of the day and certain 
notes for the project. I keep forgetting most ideas I had for this project and sometimes get lost in details.
So this is just a measurement to keep myself in line.

## 18th Aug 23:
- Added README.md / Diary.md
- changed overall comments / "commentstyle" and language in main.py
- fixed relativ path in linux environment
- Testing in windows still due, in case current solution not fitting I should create a function, that
sets the path in relation to the used user OS
- created that function, will test that soon
- externalized current_plan, help function into own module
- updated git

Ideas of this day:
- follow advice and maybe pack "window management" in own module oder pre-create certain sets?

## 21st Aug 23:
- experimenting with PyInstaller
- seems like not all packages are packed by PyInstaller
- fixed issue where logo.png couldn't be opened

## 22nd Aug 23:
- running into issue with opening PDF File on Linux after making it an exe
- found possible workaround, but unfortunately doesn't work for me at all
- all modules are externalized in different .py files
- also changed "new_window" method name to corresponding method name in file
- cleaned up a few typos

## 23rd Aug 23:
- started working on interfaces corresponding to each function
- interface for generate_plan is finished / proper graphics for buttons missing
- added first clickable checkboxes as filter, that already set a true/false for each filter
- tried to fix the issue of opening the pdf from the exe directly, 
  only was possible after I added the file to PyInstaller directly and after copying it manually to the directory
- the issue of opening any files with created .exe files with PyInstaller is that it tries to open something from the tmp
  files of your computer, which makes relative pathing useless
- need to look for other tool, workaround or in dire need for completely different solution
- added button images to git, implementation for interface will probably follow tomorrow
- couldn't wait until tomorrow, had to add the images as the buttons, although implementation isn't perfect at the moment

## 24th Aug 23:
- started to look into classes with CTk
- also tried to implement in tests
- started with pass generator app with a gui

## 25th Aug 23:
- proceeding to work on SHIELD

## 28th Aug 23:
- somehow worked out classes in Ctk, but code looks messier then without

## 29th Aug 23:
- started with SQLite in Python

## 30th Aug 23:
- Journey with SQL goes on, I am testing a little "trash code" to get going with it

