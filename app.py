from flask import Flask, render_template, jsonify

from database.repository import ActivityRepository
from analytics.statistics import Statistics

app = Flask(__name__)


def get_statistics():
    """
    Loads activity data and returns the Statistics object
    along with the DataFrame.
    """

    repo = ActivityRepository()

    df = repo.get_all_sessions()

    stats = Statistics(df)

    return stats, df


def series_to_json(series, key_name, value_name):
    """
    Converts a pandas Series into a JSON-serializable list.
    """

    data = []

    for key, value in series.items():

        if hasattr(value, "item"):
            value = value.item()

        data.append({

            key_name: str(key),

            value_name: value

        })

    return data


@app.route("/")
def dashboard():

    stats, df = get_statistics()

    data = {

        "today_screen_time": stats.screen_time("today"),

        "total_screen_time": stats.total_screen_time(),

        "total_sessions": len(df),

        "application_switches": stats.application_switches(),

        "longest_session": stats.longest_session(),

        "top_applications": stats.top_applications("today")

    }

    return render_template(
        "index.html",
        data=data
    )


@app.route("/api/dashboard")
def dashboard_api():

    stats, df = get_statistics()

    longest = stats.longest_session()

    return jsonify({

        "today_screen_time": int(
            stats.screen_time("today")
        ),

        "total_screen_time": int(
            stats.total_screen_time()
        ),

        "total_sessions": int(
            len(df)
        ),

        "application_switches": int(
            stats.application_switches()
        ),

        "longest_session": {

            "application": longest["application"],

            "duration": int(
                longest["duration"]
            )

        }

    })


@app.route("/api/top-applications")
def top_applications_api():

    stats, df = get_statistics()

    result = stats.top_applications("today")

    return jsonify(
        series_to_json(
            result,
            "application",
            "duration"
        )
    )


@app.route("/api/daily")
def daily_api():

    stats, df = get_statistics()

    result = stats.daily_screen_time()

    return jsonify(
        series_to_json(
            result,
            "date",
            "duration"
        )
    )


@app.route("/api/hourly")
def hourly_api():

    stats, df = get_statistics()

    result = stats.hourly_screen_time()

    return jsonify(
        series_to_json(
            result,
            "hour",
            "duration"
        )
    )


@app.route("/api/weekday")
def weekday_api():

    stats, df = get_statistics()

    result = stats.weekday_screen_time()

    return jsonify(
        series_to_json(
            result,
            "day",
            "duration"
        )
    )


@app.route("/api/categories")
def category_api():

    stats, df = get_statistics()

    result = stats.category_screen_time()

    return jsonify(
        series_to_json(
            result,
            "category",
            "duration"
        )
    )


@app.route("/api/category-percentage")
def category_percentage_api():

    stats, df = get_statistics()

    result = stats.category_percentage()

    return jsonify(
        series_to_json(
            result,
            "category",
            "percentage"
        )
    )


if __name__ == "__main__":
    app.run(debug=True)