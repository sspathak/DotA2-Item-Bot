# DotA2-Item-Bot
Got too many active items? Use the item bot to automatically activate certain items (like satanic) when your health is low!

## Requirements
* Python 3
* Screen recording permission

## Dependencies
* [NumPy](https://pypi.org/project/numpy/)
* [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/)


## Instructions
 Coming soon!

## How does it work?
#### 1. The item bot constantly searches for an item at a given slot
* Takes a screenshot few times every second using PyAutoGUI.
* Reads the pixel values that corresponding to the location of the item slot in the screenshot
#### 2. If the item is present, it checks if the health is low
* Compares the pixel values in the screenshot to that of the item by taking the arithmetic sum of the pixel values
* Estimates HP in a similar way by comparing the value at a pixel corresponding to the health bar. If the health is low, the pixel value will be lower.

#### 3. If the health is low, the bot activates the item
* Simulates pressing of a key (defined in the code) using PyAutoGUI


*NOTE: If the item is on cooldown, the pixel values will not match and the bot will act as if the item is not present*
