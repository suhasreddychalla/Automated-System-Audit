import pandas as pd
import numpy as np

# --- CONFIGURATION ---
THRESHOLD_MINUTES = 10
DATA_FILE = 'stop_times.txt' 

def run_audit_check():
    print("--- STARTING CENTRO SYSTEM AUDIT (GTFS DATA) ---")
    
    # 1. LOAD THE DATA
    try:
        df = pd.read_csv(DATA_FILE, usecols=['trip_id', 'stop_id', 'arrival_time'])
        df = df.head(1000) 
        print(f"Official GTFS Data Loaded: {len(df)} scheduled stops found.")
    except FileNotFoundError:
        print(f"ERROR: '{DATA_FILE}' not found.")
        return

    # 2. SIMULATE REAL-TIME LOGS
    print("Simulating real-time sensor inputs...")
    random_delays = np.random.choice(
        [0, 2, 5, 8, 12, 15, 25], 
        size=len(df),
        p=[0.4, 0.3, 0.1, 0.1, 0.05, 0.03, 0.02]
    )
    df['Simulated_Delay_Min'] = random_delays
    
    # 3. THE AUDIT LOGIC
    df['Audit_Flag'] = df['Simulated_Delay_Min'] > THRESHOLD_MINUTES

    # 4. GENERATE REPORT
    anomalies = df[df['Audit_Flag'] == True]

    print(f"\n--- AUDIT RESULTS ---")
    print(f"Audited Trip Count: {len(df)}")
    print(f"Threshold Violation: > {THRESHOLD_MINUTES} mins")
    print(f"Failures Detected: {len(anomalies)}")
    
    if len(anomalies) > 0:
        print("\nSAMPLE OF FLAGGED EVENTS:")
        print(anomalies[['trip_id', 'arrival_time', 'Simulated_Delay_Min']].head(5))
        anomalies.to_csv('centro_audit_report.csv', index=False)
        print("\nFull report saved to 'centro_audit_report.csv'")

if __name__ == "__main__":
    run_audit_check()