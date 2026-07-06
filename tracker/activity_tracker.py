import time
import win32gui
import win32process
import psutil


def get_active_window_info():
    """
    Returns:
        Window title
        Process name
    """

    hwnd = win32gui.GetForegroundWindow()

    window_title = win32gui.GetWindowText(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    process = psutil.Process(pid)

    process_name = process.name()

    return window_title, process_name


previous_window = ""

print("Activity Tracker Started...")
print("Press Ctrl + C to stop.\n")

while True:

    window_title, process_name = get_active_window_info()

    if window_title != previous_window:

        print(f"Application : {process_name}")
        print(f"Window Title: {window_title}")
        print("-" * 50)

        previous_window = window_title

    time.sleep(1)