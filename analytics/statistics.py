import pandas as pd
from datetime import datetime


class Statistics:

    def __init__(self, dataframe):
        self.df = dataframe

        self.df["start_time"] = pd.to_datetime(self.df["start_time"])
        self.df["end_time"] = pd.to_datetime(self.df["end_time"])

    # ---------------------------------------
    # Overall Statistics
    # ---------------------------------------

    def total_screen_time(self):
        """Returns total screen time (all data)."""
        return self.df["duration"].sum()

    def most_used_applications(self):
        """Returns applications sorted by total usage time."""

        return (
            self.df
            .groupby("application")["duration"]
            .sum()
            .sort_values(ascending=False)
        )

    def top_n_applications(self, n):
        """Returns the top N most used applications."""
        return self.most_used_applications()[:n]

    # ---------------------------------------
    # Session Filters
    # ---------------------------------------

    def get_sessions(self, period):

        if period == "today":

            return self.df[
                self.df["start_time"].dt.date == datetime.now().date()
            ]

        elif period == "week":

            current_week = datetime.now().isocalendar().week
            current_year = datetime.now().year

            return self.df[
                (self.df["start_time"].dt.isocalendar().week == current_week)
                &
                (self.df["start_time"].dt.year == current_year)
            ]

        elif period == "month":

            current_month = datetime.now().month
            current_year = datetime.now().year

            return self.df[
                (self.df["start_time"].dt.month == current_month)
                &
                (self.df["start_time"].dt.year == current_year)
            ]

        else:
            raise ValueError("Invalid period")

    # ---------------------------------------
    # Period Statistics
    # ---------------------------------------

    def screen_time(self, period):
        """Returns screen time for today/week/month."""

        sessions = self.get_sessions(period)

        return sessions["duration"].sum()

    def top_applications(self, period):
        """Returns applications ranked by usage for the given period."""

        sessions = self.get_sessions(period)

        return (
            sessions
            .groupby("application")["duration"]
            .sum()
            .sort_values(ascending=False)
        )

    def top_n_applications_period(self, period, n):
        """Returns top N applications for the given period."""

        return self.top_applications(period)[:n]
    
    def daily_screen_time(self):

        result = (
            self.df
            .groupby(self.df["start_time"].dt.date)["duration"]
            .sum()
            .sort_index()
        )

        return result
    def hourly_screen_time(self):

        result = (
            self.df
            .groupby(self.df["start_time"].dt.hour)["duration"]
            .sum()
            .sort_index()
        )

        return result
    
    def weekday_screen_time(self):

            result = (
                self.df
                .groupby(self.df["start_time"].dt.day_name())["duration"]
                .sum()
            )

            order = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ]

            result = result.reindex(order, fill_value=0)

            return result

    def longest_session(self):
        """
        Returns the session with the maximum duration.
        """

        index = self.df["duration"].idxmax()

        return self.df.loc[index]
    
    def average_session_time(self):
        """
        Returns the average duration of a session in seconds.
        """

        return round(self.df["duration"].mean(), 2)

    def application_switches(self):
        """
        Returns the number of application switches.
        """

        if len(self.df) <= 1:
            return 0

        return len(self.df) - 1
    
    def application_summary(self, app_name):
        """
        Returns summary statistics for a single application.
        """

        app_df = self.df[
            self.df["application"] == app_name
        ]

        if app_df.empty:
            return None

        return {
            "application": app_name,
            "total_time": app_df["duration"].sum(),
            "sessions": len(app_df),
            "average_session": round(app_df["duration"].mean(), 2),
            "longest_session": app_df["duration"].max()
        }
    
    def category_screen_time(self):
        """
        Returns the total screen time for each category.
        """

        result = (
            self.df
            .groupby("category")["duration"]
            .sum()
            .sort_values(ascending=False)
        )

        return result
    
    def top_categories(self, n=5):

        result = self.category_screen_time()

        return result.head(n)
    
    def category_percentage(self):
        """
        Returns the percentage of total screen time
        spent in each category.
        """

        result = self.category_screen_time()

        total = result.sum()

        percentage = (
            result / total * 100
        ).round(2)

        return percentage