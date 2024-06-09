import pyautogui

# Capture the screenshot of the specified region
# im = pyautogui.screenshot("screen.png" , region=(0,0,300,300))

try:
    # Try to find the center coordinates of the image on the screen
    x, y = pyautogui.locateCenterOnScreen("eight.png" , confidence=0.7)
    print("Image found. Coordinates:", x, y)
    
    # Move the mouse cursor to the found coordinates
    pyautogui.moveTo(x , y)
    
    # Perform a left click at the found coordinates
    pyautogui.leftClick()
    
except pyautogui.ImageNotFoundException:
    # If the image is not found, handle the exception
    print("Image not found.")
except Exception as e:
    # Handle any other exceptions that might occur
    print("Error:", e)