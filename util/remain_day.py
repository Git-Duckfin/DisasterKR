from datetime import datetime, timedelta

# Start and end dates
start_date = datetime.strptime("2022-05-20", "%Y-%m-%d")
end_date = datetime.strptime("2024-04-07", "%Y-%m-%d")

# Calculate the number of days
total_days = (end_date - start_date).days

# Calculate the number of weeks and remaining days
weeks, remaining_days = divmod(total_days, 7)
remaining_days

