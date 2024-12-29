import subprocess
import time
import pyautogui
import pygetwindow as gw

link = ["steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4800345177931084064A36001674929D14883377421505215594","steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4800345177931084064A36001674929D14883377421505215594","steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561199146708568A35320368260D11848656866460789963"]
def focus_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]  # Get the window with the specified title
        window.activate()  # Focus the window
        window.restore()   # Restore it if minimized
        return True
    except IndexError:
        return False  # If no window is found with that title

focus_window("Counter-Strike 2")
for i in link:
  subprocess.run(['explorer', i], shell=True)
  pyautogui.moveTo(1080, 300)
  time.sleep(1)
  pyautogui.mouseDown(button="left")

  time.sleep(5)
  pyautogui.screenshot(str(time.time())+".png")
  for i in range(20):
    pyautogui.moveRel(-50,0)
    time.sleep(0.05)

  time.sleep(1)
  pyautogui.mouseUp(button="left")
  pyautogui.screenshot(str(time.time())+"2.png")

left = 0
right = 1280
top = 100
bottom = 700

# image = Image.open("screenshot1.png")
# crop_image = image.crop((left, top, right, bottom))
# crop_image.save("crop_screenshot1.png")

# image = Image.open("screenshot2.png")
# crop_image = image.crop((left, top, right, bottom))
# crop_image.save("crop_screenshot2.png")