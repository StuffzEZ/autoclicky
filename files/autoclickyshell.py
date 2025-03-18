import pyautogui
import time

# Main function
def main():
    print("AutoClicky Shell")
    print("-------------------")
    print("If You Would Like To Enter The Settings Menu, Type SETTINGS Or Press Enter To Just Continue")
    option = input("Option? SETTINGS/Enter (Continue): ")
    if option == "SETTINGS":
        debugmodein = input("Enable Debug Mode (Show Clicks?) Y/n")
        if debugmodein == "Y":
            debug = 1
#    print("Please Enter The Keyboard Keys You Want To Press Or Click Escape When It Starts Recording (esc)")
#    print("Recording Keys In 10 Seconds...")
#    time.sleep(5)
#    print("Recording Keys In 5 Seconds...")
#    time.sleep(5)
#    print("Recording Keys... Press Escape (esc) When Done")
#    recorded = keyboard.record(until='esc')
#    time.sleep(1)
#    print("Recorded Keys!")
    print("-------------------")
    num_clicks = int(input("Enter the number of clicks: "))
    click_delay = float(input("Enter the click delay (in seconds): "))

    auto_clicker(num_clicks, click_delay, debug)

# Function to perform auto clicks
def auto_clicker(num_clicks, click_delay, debug):
    try:
        print("Auto Clicker will start in 3 seconds. Move your mouse to the desired click location.")
        time.sleep(3)

        for _ in range(num_clicks):
            x, y = pyautogui.position()  # Get current mouse position
            pyautogui.click(x, y)       # Perform a mouse click
            if debug == 1:
                print(f"Click at ({x}, {y})")
#            keyboard.play(recorded, speed_factor=500)
            time.sleep(click_delay)  # Add some randomness to the delay

        print("Auto Clicker has finished.")
    except KeyboardInterrupt:
        print("Auto Clicker stopped.")

if __name__ == "__main__":
    main()