import keyboard
import time

keyboard.wait('k')
keyboard.press_and_release('win+r')
time.sleep(0.5)
keyboard.write('cmd')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.write('netsh wlan show profile name="[YOUR WIFI NETWORK]" key=clear')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('ctrl+shift+a')
time.sleep(0.5)
keyboard.press_and_release('ctrl+c')
time.sleep(0.5)
