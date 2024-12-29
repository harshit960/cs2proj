from flask import Flask, request, jsonify
import subprocess
import time
import pyautogui
import pygetwindow as gw
import os
import pygetwindow as gw
import win32gui
import win32con
app = Flask(__name__)

# Helper function to focus on a specific window by title
# def focus_window(title):
#     try:
#         print("Finding window: " + title)
#         window = gw.getWindowsWithTitle(title)[0]  # Get the window with the specified title
#         window.activate()  # Focus the window
#         window.restore()   # Restore it if minimized
#         return True
#     except IndexError:
#         return False  # If no window is found with that title
def focus_window(title_part):
    try:
        # Get all window titles
        windows = gw.getAllTitles()
        matching_windows = [w for w in windows if title_part.lower() in w.lower()]
        
        if not matching_windows:
            print(f"No window found matching: {title_part}")
            raise Exception(f"No window found matching: {title_part}")
        
        # Focus and bring the window to the front using win32gui
        hwnd = gw.getWindowsWithTitle(matching_windows[0])[0]._hWnd  # Get window handle
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore the window if minimized
        win32gui.SetForegroundWindow(hwnd)  # Bring the window to the front

        return True
    except Exception as e:
        return False, str(e)  #
    


# Helper function to take a screenshot for a given link
def take_screenshot(link, window_title="Counter-Strike 2"):
    focus_window(window_title)
    if not focus_window(window_title):
        print("Window not found: " + window_title)
        return False, "Window not found: " + window_title

    try:
        # Open the link in the associated application
        subprocess.run(['explorer', link], shell=True)
        time.sleep(1)  # Wait for the application to load the link
        
        # Perform actions and take screenshots
        pyautogui.moveTo(1080, 300)
        pyautogui.mouseDown(button="left")
        time.sleep(5)
        screenshot_name = str(time.time()) + ".png"
        pyautogui.screenshot(screenshot_name)
        for i in range(20):
            pyautogui.moveRel(-50,0)
            time.sleep(0.05)
        time.sleep(1)
        pyautogui.mouseUp(button="left")
        screenshot_name = str(time.time()) + ".png"
        pyautogui.screenshot(screenshot_name)
        return True, screenshot_name
    except Exception as e:
        return False, str(e)

# Flask endpoint to handle screenshot requests
@app.route('/take_screenshot', methods=['POST'])
def take_screenshot_endpoint():
    data = request.get_json()
    if not data or 'link' not in data:
        return jsonify({"error": "Invalid request, 'link' is required"}), 400
    
    link = data['link']
    success, message = take_screenshot(link)
    if success:
        return jsonify({"message": "Screenshot saved successfully", "image_name": message}), 200
    else:
        return jsonify({"error": message}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
