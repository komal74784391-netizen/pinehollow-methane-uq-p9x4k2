import pandas as pd

REQUIRED = ['flight_id', 'timestamp', 'ch4_ppb', 'wind_speed_ms', 'altitude_m']

def load_flight(path):
    frame = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in frame.columns]
    if missing:
        raise ValueError(f'missing columns: {missing}')
    frame['timestamp'] = pd.to_datetime(frame['timestamp'], utc=True)
    return frame.sort_values('timestamp')
