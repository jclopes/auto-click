# auto-click
Automate a mouse click on any part of the screen by using an image of what you want to click.

## Motivation
I miss the league of legends timer to click the "accept!" button too many time. So I decided to automate the click of that accept button.

## Install and Run

First git clone this repo then install all dependencies:
```
pip install -r requirements.txt
```
Take a screenshot of the thing you want to click and save it to the same forder where you are running the script from with the name:
```
template.png
```
Finally run the script and see it in action with the command:
```
python main.py
```

## How it works
The script will take a screenshot every 2 seconds until a part of the screen looks close enough to the template image.
Then make a mouse click on the top left corner of the position where the template was detected.

To make the script work for your special case you need to replace the template image with a image that looks like what you want to be clicked. I took a screenshot of the "accept" screen button for LoL then croped and saved it as a template.
