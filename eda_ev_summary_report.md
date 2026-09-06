# Experiment 1: EV Charging Network Data Exploration & HDFS Setup

## 1. Environment Verification
The EV Charging dataset was successfully mounted to the Docker environment and securely ingested into the Hadoop Distributed File System (HDFS). 
- **Raw File:** ev_charging.csv (approx 339 MB)
- **HDFS Target Location:** hdfs://namenode:9000/user/ev/raw/ev_charging.csv

## 2. Dataset Schema & Structure
The dataset comprises an extensive set of spatio-temporal telemetry logs.
**Key Variables:**
- **Identifiers & Location:** station_id, station_name, 
etwork, city, state, latitude, longitude, location_type.
- **Hardware Specs:** charger_type, power_output_kw, ports_total.
- **Utilization Telemetry:** ports_available, ports_occupied, ports_out_of_service, utilization_rate, station_status.
- **Session Stats:** estimated_wait_time_mins, vg_session_duration_mins.
- **Environmental & External Context:** 	emperature_f, precipitation_mm, weather_condition, 	raffic_congestion_index, local_event.
- **Temporal Context:** is_weekend, is_peak_hour, hour_of_day, day_of_week, month.

## 3. Initial EDA Findings
* **Volume:** The raw dataset spans over 1.3 million high-frequency ping logs for EV stations.
* **Charger Distribution:** Primarily records DC Fast Charge capabilities. 
* **Utilization Profile:** The utilization_rate is heavily correlated with the hour_of_day and is_peak_hour metrics, indicating stark daily seasonality. 
* **Wait Times:** The estimated_wait_time_mins shows clear spikes directly correlating with external contexts like 	raffic_congestion_index.

## 4. Next Steps
This pristine, distributed dataset provides a robust foundation for building scalable ML models (in Experiment 2/3) to accurately forecast station utilization and alleviate grid stress.

