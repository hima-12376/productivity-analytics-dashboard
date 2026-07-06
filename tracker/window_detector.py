import win32gui
import win32process
import psutil


class WindowDetector:
    """
    Responsible only for communicating with Windows
    and returning information about the active window.
    """

    def get_active_window(self):
        hwnd = win32gui.GetForegroundWindow()

        window_title = win32gui.GetWindowText(hwnd)

        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)

        process_name = process.name()

        return process_name, window_title