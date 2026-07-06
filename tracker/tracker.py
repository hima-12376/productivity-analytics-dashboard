import time
from datetime import datetime

from tracker.window_detector import WindowDetector
from database.database import insert_activity
from categorizer.categorizer import ApplicationCategorizer


class Tracker:

    def __init__(self):

        self.detector = WindowDetector()

        self.current_app = None
        self.current_window = None
        self.session_start = None

    def initialize(self):

        self.current_app, self.current_window = (
            self.detector.get_active_window()
        )

        self.session_start = datetime.now()

        print("Tracking Started")
        print(self.current_app)

    def save_current_session(self):

        end_time = datetime.now()

        duration = int(
            (end_time - self.session_start).total_seconds()
        )

        category = ApplicationCategorizer.get_category(
            self.current_app,
            self.current_window
        )

        print("\nSaving session...")

        print(f"Application : {self.current_app}")
        print(f"Category    : {category}")
        print(f"Duration    : {duration} seconds")

        insert_activity(
            application=self.current_app,
            category=category,
            window_title=self.current_window,
            start_time=self.session_start,
            end_time=end_time,
            duration=duration
        )

        return end_time

    def start_tracking(self):

        print("\nMonitoring application changes...\n")

        try:

            while True:

                app, window = self.detector.get_active_window()

                if app != self.current_app:

                    end_time = self.save_current_session()

                    self.current_app = app
                    self.current_window = window
                    self.session_start = end_time

                    print(f"\nNow tracking: {self.current_app}")
                    print("-" * 50)

                time.sleep(1)

        except KeyboardInterrupt:

            print("\nStopping tracker...")

            self.save_current_session()

            print("Goodbye!")