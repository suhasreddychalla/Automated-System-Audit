import pandas as pd
import random

def create_realistic_gtfs_data():
    print("Generating 'Official' CENTRO Data File...")

    # 1. SETUP REAL SYRACUSE STOPS
    stops = [
        (101, "Syracuse Transit Hub"),
        (205, "College Place (Syracuse Univ)"),
        (308, "Destiny USA Mall"),
        (410, "Drumlins Country Club"),
        (550, "South Campus - Slocum Heights")
    ]

    # 2. CREATE SCHEDULED TRIPS
    data_rows = []
    trip_id_counter = 1000
    
    for hour in range(8, 18): # 8 AM to 6 PM
        for minute in [0, 15, 30, 45]:
            trip_id_counter += 1
            current_minute = minute
            current_hour = hour
            
            for stop_seq, (stop_id, stop_name) in enumerate(stops):
                time_str = f"{current_hour:02d}:{current_minute:02d}:00"
                data_rows.append({
                    'trip_id': trip_id_counter,
                    'arrival_time': time_str,
                    'departure_time': time_str,
                    'stop_id': stop_id,
                    'stop_sequence': stop_seq + 1
                })
                current_minute += 12
                if current_minute >= 60:
                    current_minute -= 60
                    current_hour += 1

    # 3. SAVE AS TEXT FILE
    df = pd.DataFrame(data_rows)
    df.to_csv('stop_times.txt', index=False)
    print("SUCCESS: 'stop_times.txt' has been created in your folder.")

if __name__ == "__main__":
    create_realistic_gtfs_data()