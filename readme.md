# SchemaPing
## Simple Interplatform Push Notifier
## Dependencies: None! (Tkinter though.)

SchemaPing is a very small, tkinter-based notification creator.
Nothing fancy right now. No images, no custom time, but it's very useful for some cases where you don't want to work with plyer / wintoasts, etc.

For the most part-ish, SchemaPing is compatible with all OSes and all screen sizes.

(Both claims untested. In theory should be true.)


There are currently 2 methods of utilising SchemaPing.

## P.S Ignore the font in these images. Imagine it's Segoe UI.
# 1: Py Imports
![image](https://github.com/user-attachments/assets/d4ff12ad-ff37-496b-9ba3-a4cdfb394ac2)
To use:
- Download schemaping.py from the root of this repository.
- Place wherever your script is.
- See below. Or above.
```python
import schemaping
schemaping.create_notif("Hello World!","We are connected!!!")
```
Very simple. 
# 2: CMD Args.
![image](https://github.com/user-attachments/assets/cab69632-6807-4df5-a91a-2f9b0b423a3f)

```
path/to/your/schemaping -t Hello_World! -c We_are_connected!!!
```
Since you can't use spaces in cmd args, SchemaPing resolves this by substituting spaces for underscores!
e.g, "Testing_123." in the example will come out as "Testing 123."

# "What does build.py do?"
build.py generates an .exe of schemaping.py using pyinstaller, which is assumed to be in the same dir.
Use if you intend to utilize schemaping on something that doesn't have python.
And remember..


![6a0120a85dcdae970b0128776ff992970c-pi](https://github.com/user-attachments/assets/d8ff21a2-6686-4b00-8061-392039381810)
