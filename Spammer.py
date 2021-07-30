import pyautogui, time
time.sleep(5)
f = open("destroyer", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.2)
