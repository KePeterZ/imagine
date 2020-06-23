# Installing imagine.py

## Downloading from GitHub

First, install ev3dev on an SD card, as [shown here.](https://www.ev3dev.org/docs/getting-started/)
Then do any first-time setup you with to do.  
In my opinion, it's good practice to do a ```sudo apt update``` on the first boot, but you are free to leave that out.  

Next, run these 2 commands (assuming you're using the stock ev3dev OS):
```bash
git clone https://github.com/KePeterZ/imagine ~/
cd imagine
```
And you're good to go! Howewer, you'll probably want to write your code in a different directory, rather than in ```~/imagine```, so you'll have to copy ```imagine.py``` file into whichever folder you want to use it in. 

## Alternate solution: put imagine in ```PATH```

If you want to use imagine in any folder on the filesystem, you'll probably want to put it in your path, but keep in mind, that this will make it more difficult for you to edit it. 

If you want to put the lib (in it's current state) into PATH, you'll have to run this command: 
```bash
sudo cp ./imagine.py /usr/lib/micropython/imagine.py
```
Howewer, if you modify the main robotClass, you'll need to re-run the above command, to refresh the file in PATH.

# KePeterZ, 2020