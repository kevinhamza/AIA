import pyautogui
import os
import subprocess
import time
from win32api import GetSystemMetrics
import psutil

class DeviceControl:
    def __init__(self):
        pass

    def move_mouse(self, x, y):
        """Move the mouse to a specific position"""
        pyautogui.moveTo(x, y)

    def click(self, x, y):
        """Simulate a mouse click at the specified coordinates"""
        pyautogui.click(x, y)

    def scroll(self, direction, amount=10):
        """Scroll the mouse in the specified direction"""
        pyautogui.scroll(amount) if direction == "up" else pyautogui.scroll(-amount)

    def screenshot(self, save_path="screenshot.png"):
        """Capture a screenshot of the current screen"""
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)

    def open_application(self, app_name):
        """Open an application by name (Windows-specific)"""
        try:
            subprocess.run([app_name], check=True)
            print(f"{app_name} opened successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error opening {app_name}: {e}")

    def get_system_metrics(self):
        """Get screen width and height"""
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        return screen_width, screen_height

    def close_application(self, app_name):
        """Close an application by its name"""
        for process in psutil.process_iter():
            try:
                if app_name.lower() in process.name().lower():
                    process.terminate()
                    print(f"{app_name} closed successfully.")
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    def shutdown_system(self):
        """Shut down the computer"""
        os.system("shutdown /s /t 1")

    def restart_system(self):
        """Restart the computer"""
        os.system("shutdown /r /t 1")

    def lock_system(self):
        """Lock the computer"""
        os.system("rundll32.exe user32.dll,LockWorkStation")

if __name__ == "__main__":
    device_control = DeviceControl()
    device_control.move_mouse(100, 100)
    device_control.click(100, 100)
    device_control.scroll("up", 5)
    device_control.screenshot("screenshot_test.png")
    device_control.open_application("notepad")
    time.sleep(2)
    device_control.close_application("notepad")
    device_control.shutdown_system()
