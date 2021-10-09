# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)
dt2 = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt2.replace(year=1917).isoformat()

# Print the results in ISO 8601 format
print(dt.isoformat())
print(dt2.isoformat())
print(dt_old)