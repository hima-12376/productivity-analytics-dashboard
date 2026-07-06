from database.repository import ActivityRepository

repo = ActivityRepository()

df = repo.get_all_sessions()

print(df)