from database.repository import ActivityRepository
from analytics.statistics import Statistics

repo = ActivityRepository()

df = repo.get_all_sessions()

stats = Statistics(df)

print(stats.category_percentage())