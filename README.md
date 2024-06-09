# Screen Capture and Clicking with PyAutoGUI

This Python script contains a simple example code for searching for an image on the screen and clicking it using the PyAutoGUI library.

## Installation

To install the PyAutoGUI library, use the following command in your project folder:

```
pip install pyautogui
```

## Usage

1. The `pyautogui.locateCenterOnScreen()` function finds the position of the image on the screen.
2. If the image is found, the mouse is moved to that position using the `pyautogui.moveTo()` function.
3. A left click is performed at the found coordinates using the `pyautogui.leftClick()` function.

## Example Usage

```python
import pyautogui

try:
    x, y = pyautogui.locateCenterOnScreen("eight.png" , confidence=0.7)
    print("Image found. Coordinates:", x, y)
    pyautogui.moveTo(x , y)
    pyautogui.leftClick()
    
except pyautogui.ImageNotFoundException:
    print("Image not found.")
except Exception as e:
    print("Error:", e)
```

## Notes

- The `confidence` parameter of the `pyautogui.locateCenterOnScreen()` function determines how certain the image match should be. The default value is 0.9.
- Before running the code, make sure you specify the correct name and path of the image you want to use.
