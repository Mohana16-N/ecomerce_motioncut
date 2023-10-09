import pyautogui as p
import time

# Wait for WhatsApp Web to load (you might need to adjust the sleep time)
time.sleep(10)

# Loop to send the message multiple times
for i in range(100):
    # Type the message
    p.write("Reply me call me\n")
    p.write("its not me program")
    # Press the "Enter" key to send the message
    p.press("enter")

    # Add a delay to simulate a human typing speed (optional)
    # time.sleep(1)
