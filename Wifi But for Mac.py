import keyboard
import time

keyboard.wait('k')
keyboard.press_and_release('win+space')
time.sleep(0.5)
keyboard.write('Terminal')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.write('security find-generic-password -wa IMSA_wifi')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('win+a')
time.sleep(0.5)
keyboard.press_and_release('win+c')
time.sleep(0.5)