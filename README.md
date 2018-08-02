# auto-click
Automate a mouse click on the screen that looks like the template image.

## Install and Run
git clone this repo then:
```
pip install -r requirements.txt
python main.py
```

## Motivation
I miss the league of legends timer to click the "accept!" button too many time. This script fixes it!

## How it works
The script will take a screenshot every 2 seconds until a part of the screen looks close enough to the template image.
Then make a mouse click on the position where the template was detected.
