import pandas as pd
from datetime import datetime

def format_departure_times(df):
    df['departure_time'] = pd.to_datetime(df['departure_time'], format='%d/%m/%Y %H:%M')
    return df

def calculate_countdowns(df):
    now = datetime.now()
    df['time_to_departure'] = df['departure_time'] - now
    df['status'] = df['time_to_departure'].apply(lambda td: get_status(td))
    return df

def get_status(td):
    if td.total_seconds() < 0:
        return "Departed"
    elif td.total_seconds() < 3600:
        return "Departing Soon"
    else:
        return "Scheduled"
