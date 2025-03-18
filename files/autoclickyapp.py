import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading
import keyboard

def update_status(message):
    status_label.config(text=message)

def start_autoclicker():
    try:
        num_clicks = int(num_clicks_entry.get())
        click_delay = float(click_delay_entry.get())
        debug = debug_var.get()
        
        update_status("Auto Clicker will start in 3 seconds. Move your mouse.")
        time.sleep(3)
        
        for _ in range(num_clicks):
            if keyboard.is_pressed("ctrl+c"):
                update_status("Auto Clicker interrupted.")
                return
            
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            if debug:
                debug_text.insert(tk.END, f"Click at ({x}, {y})\n")
                debug_text.see(tk.END)
            time.sleep(click_delay)
        
        update_status("Auto Clicker has finished.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_clicking_thread():
    threading.Thread(target=start_autoclicker, daemon=True).start()

def toggle_debug():
    if debug_var.get():
        debug_text.pack()
    else:
        debug_text.pack_forget()

# Create GUI window
root = tk.Tk()
root.title("AutoClicky GUI")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

# Labels and input fields
tk.Label(root, text="Number of Clicks:", bg="#f0f0f0").pack(pady=2)
num_clicks_entry = tk.Entry(root, relief="solid", borderwidth=2)
num_clicks_entry.pack(pady=2)

tk.Label(root, text="Click Delay (seconds):", bg="#f0f0f0").pack(pady=2)
click_delay_entry = tk.Entry(root, relief="solid", borderwidth=2)
click_delay_entry.pack(pady=2)

debug_var = tk.BooleanVar()
debug_check = tk.Checkbutton(root, text="Enable Debug Mode", variable=debug_var, command=toggle_debug, bg="#f0f0f0")
debug_check.pack(pady=5)

# Debug output text box
debug_text = tk.Text(root, height=5, state=tk.NORMAL, relief="solid", borderwidth=2)

tk.Label(root, text="", bg="#f0f0f0").pack()  # Spacer

# Start button
start_button = tk.Button(root, text="Start AutoClicker", command=start_clicking_thread, relief="solid", borderwidth=2, bg="#4CAF50", fg="white")
start_button.pack(pady=5)

# Status label
status_label = tk.Label(root, text="", bg="#f0f0f0", fg="blue")
status_label.pack(pady=5)

# Run the application
root.mainloop()
