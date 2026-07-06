from categorizer.categorizer import ApplicationCategorizer


tests = [

    ("Code.exe", "Visual Studio Code"),

    ("msedge.exe", "GitHub - Activity Tracker"),

    ("msedge.exe", "ChatGPT"),

    ("msedge.exe", "YouTube"),

    ("msedge.exe", "Coursera"),

    ("Spotify.exe", "Spotify Premium"),

    ("explorer.exe", "Documents"),

    ("unknown.exe", "Random App")
]


for application, title in tests:

    category = ApplicationCategorizer.get_category(
        application,
        title
    )

    print(
        f"{application:15} | "
        f"{title:30} | "
        f"{category}"
    )