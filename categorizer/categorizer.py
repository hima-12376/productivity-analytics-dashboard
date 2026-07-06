class ApplicationCategorizer:
    """
    Categorizes applications based on the executable name
    and (optionally) the window title.
    """

    APPLICATION_MAP = {

        # Development
        "Code.exe": "Work",
        "pycharm64.exe": "Work",
        "devenv.exe": "Work",
        "idea64.exe": "Work",
        "eclipse.exe": "Work",
        "notepad++.exe": "Work",

        # Browsers
        "chrome.exe": "Browser",
        "msedge.exe": "Browser",
        "firefox.exe": "Browser",

        # Communication
        "Teams.exe": "Communication",
        "Slack.exe": "Communication",
        "Discord.exe": "Communication",
        "Telegram.exe": "Communication",

        # Entertainment
        "Spotify.exe": "Entertainment",
        "vlc.exe": "Entertainment",

        # System
        "explorer.exe": "System",
        "cmd.exe": "System",
        "powershell.exe": "System",
        "Taskmgr.exe": "System",
    }

    TITLE_RULES = {

        # Learning
        "coursera": "Learning",
        "udemy": "Learning",
        "geeksforgeeks": "Learning",
        "w3schools": "Learning",
        "stackoverflow": "Learning",
        "chatgpt": "Learning",
        "kaggle": "Learning",

        # Work
        "github": "Work",
        "gitlab": "Work",
        "jira": "Work",
        "notion": "Work",

        # Entertainment
        "youtube": "Entertainment",
        "netflix": "Entertainment",
        "spotify": "Entertainment",
        "prime video": "Entertainment",

        # Social
        "facebook": "Social",
        "instagram": "Social",
        "twitter": "Social",
        "x.com": "Social",
        "linkedin": "Social",

        # Shopping
        "amazon": "Shopping",
        "flipkart": "Shopping",

        # Communication
        "gmail": "Communication",
        "outlook": "Communication"
    }

    @classmethod
    def get_category(cls, application, window_title=""):
        """
        Returns the category for an application.

        Window title rules take priority over
        executable name.
        """

        title = window_title.lower()

        # First inspect window title
        for keyword, category in cls.TITLE_RULES.items():

            if keyword in title:
                return category

        # Otherwise inspect application name
        return cls.APPLICATION_MAP.get(
            application,
            "Other"
        )
