# Automated System Reliability Audit (Python)

## Project Overview
This tool automates the auditing of transit schedule reliability. It was designed to ingest GTFS (General Transit Feed Specification) data, simulate real-time sensor inputs, and flag operational anomalies based on specific control thresholds.

**Tools Used:** Python, Pandas, NumPy, ETL Data Processing.

## Key Features
* **Automated Data Ingestion:** Parses complex GTFS text files (`stop_times.txt`) to establish a control baseline.
* **Threshold Monitoring:** Automatically flags any trip delayed by >10 minutes (configurable threshold).
* **Failure Reporting:** Generates a CSV audit trail (`centro_audit_report.csv`) for operations management.

## How to Run
1.  Clone the repository.
2.  Run the data generator (if raw data is missing):
    ```bash
    python create_data.py
    ```
3.  Execute the audit script:
    ```bash
    python audit_centro_gtfs.py
    ```

## Sample Output
> "Audited Trip Count: 200"
> "Failures Detected: 22"
