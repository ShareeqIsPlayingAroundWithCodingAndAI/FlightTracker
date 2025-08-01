import pandas as pd
from tabulate import tabulate
from utils.helpers import format_departure_times, calculate_countdowns

# Load flight data
df = pd.read_csv('Flights.csv')

# Format datetime
df = format_departure_times(df)

# Add countdowns
df = calculate_countdowns(df)

# Sort by departure time
df = df.sort_values(by='departure_time')

# Display flight data
print(tabulate(df, headers='keys', tablefmt='grid'))
