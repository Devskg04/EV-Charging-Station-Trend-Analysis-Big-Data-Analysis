# Experiment 2: Project Proposal & Architecture Definition

## 1. Project Title & Problem Domain
**Project Title:** Smart City Green Energy Infrastructure: Big Data Analysis of EV Charging Networks  
**Domain Focus:** Green Energy & Smart City Infrastructure (EV Charging)

**Context & Background:**
As the global transition to electric vehicles (EVs) accelerates, smart cities must develop robust charging infrastructures. However, the adoption rate frequently outpaces grid capacity, leading to unbalanced station utilization, long driver wait times, and grid instability. Managing thousands of distributed EV chargers generates massive streams of telemetry data (utilization rates, power output, session durations) that cannot be analyzed effectively in real-time using traditional relational databases.

**Problem Statement:**
Inefficient distribution of EV charging demand causes localized grid congestion and degrades the user experience. By analyzing historical charging session metrics, pricing types, weather conditions, and traffic congestion, this project aims to predict station utilization and wait times. 

**Project Objectives:**
This project aims to design and implement a scalable, distributed Big Data architecture using Apache Hadoop and Apache Spark to:
1. **Ingest and Store:** Reliably store massive volumes of raw EV telemetry data across a distributed file system (HDFS).
2. **Process at Scale:** Utilize PySpark's distributed in-memory computing to clean and transform over 1.3 million session logs efficiently.
3. **Predictive Modeling:** Leverage Spark MLlib to forecast station utilization rates and optimize dynamic pricing models based on traffic and weather conditions.
4. **Actionable Intelligence:** Provide grid operators and city planners with interactive dashboards to route drivers to under-utilized stations and plan future infrastructure investments.

---

## 2. Dataset Allocation
**Dataset Origin:** Smart City EV Charging Network Logs  
**Data Architecture:** High-frequency spatio-temporal logs tracking charging session telemetry, grid power output, and external environmental factors.  

**Volume & Scale Justification:**
The selected dataset comprises an extensive **~339 MB** of raw CSV data on disk. During iterative Machine Learning and complex time-window aggregations across thousands of station IDs, this expands significantly in-memory. It provides a robust volume to demonstrate the necessity and power of Spark's distributed DataFrame API.

**Spatio-Temporal Scope:**
- **Time Horizon:** Comprehensive tracking across multiple seasons and times of day, capturing peak commuting hours, weekend anomalies, and seasonal weather impacts (extreme heat vs. precipitation).
- **Geographic Spread:** Covers major smart cities (e.g., Los Angeles) with varying traffic congestion indexes and local events.

**Feature Engineering & Target Variables:**
- **Station Telemetry:** power_output_kw, ports_available, ports_occupied, vg_session_duration_mins.
- **External Factors:** 	emperature_f, precipitation_mm, 	raffic_congestion_index, is_weekend, is_peak_hour.
- **Target Variables:** 
  - utilization_rate (Continuous numeric variable for Regression tasks).
  - estimated_wait_time_mins (Regression and Time-Series forecasting).

---

## 3. Team Roles & Responsibilities
To efficiently build this end-to-end Big Data system, our team is structured around the following specialized roles:

1. **Dhruv Jain — Data Engineer**
   - *Responsibilities:* Design and maintain the distributed infrastructure (Docker, Hadoop cluster). Manage data ingestion pipelines (Shell scripting into HDFS) and ensure data availability and fault tolerance.

2. **Aryan Rajendra Dalvi — Data Scientist**
   - *Responsibilities:* Lead the Machine Learning layer. Utilize Apache Spark MLlib to build predictive models for EV station utilization, perform hyperparameter tuning, and evaluate model accuracy.

3. **Vivaan Balchandani — Data Analyst**
   - *Responsibilities:* Lead Exploratory Data Analysis (EDA) using PySpark. Identify statistical trends, handle missing values, analyze weather/traffic correlations, and uncover actionable insights from the raw data.

4. **Vansh Chawla — BI & Visualization Engineer**
   - *Responsibilities:* Design the presentation layer. Connect aggregated outputs from the Spark cluster to visualization tools (Tableau, PowerBI, or Streamlit) to build interactive dashboards for grid operators.

---

## 4. End-to-End System Architecture

Below is the high-level architecture diagram detailing the five core layers of our Big Data system: Ingestion, Storage, Processing, Machine Learning, and Dashboarding.

`mermaid
graph TD
    %% Define Styles
    classDef source fill:#f9d0c4,stroke:#333,stroke-width:2px,color:#000;
    classDef ingest fill:#f9f0c4,stroke:#333,stroke-width:2px,color:#000;
    classDef storage fill:#c4e0f9,stroke:#333,stroke-width:2px,color:#000;
    classDef process fill:#d0f9c4,stroke:#333,stroke-width:2px,color:#000;
    classDef ml fill:#e0c4f9,stroke:#333,stroke-width:2px,color:#000;
    classDef dash fill:#f9c4e0,stroke:#333,stroke-width:2px,color:#000;

    %% Nodes
    subgraph Data Sources
        A1[EV Station Telemetry Logs]:::source
        A2[Weather & Traffic Data]:::source
    end

    subgraph 1. Ingestion Layer
        B[Shell Scripting / Batch Ingestion]:::ingest
    end

    subgraph 2. Distributed Storage Layer
        C[(Hadoop HDFS - Raw Zone)]:::storage
    end

    subgraph 3. Processing Layer
        D1[PySpark Data Cleaning]:::process
        D2[Missing Value Imputation]:::process
        D3[Feature Engineering]:::process
    end

    subgraph 4. Machine Learning Layer
        E1[Spark MLlib]:::ml
        E2[Utilization Predictive Modeling]:::ml
    end

    subgraph 5. Presentation / Dashboard Layer
        F1[Aggregated Data Storage]:::storage
        F2[Tableau / PowerBI / Streamlit Dashboard]:::dash
    end

    %% Flow
    A1 --> B
    A2 --> B
    B -->|Put to distributed storage| C
    C -->|Read by Spark| D1
    D1 --> D2
    D2 --> D3
    D3 --> E1
    E1 --> E2
    E2 --> F1
    D3 --> F1
    F1 --> F2
`

### Architecture Breakdown:
1. **Ingestion Layer:** Raw EV charging CSV logs are batch-loaded into the cluster using Hadoop filesystem commands.
2. **Storage Layer:** Hadoop HDFS provides scalable, fault-tolerant distributed storage across multiple DataNodes.
3. **Processing Layer:** Apache Spark distributes the computation in-memory across worker nodes. PySpark is used to clean the data, handle nulls, and extract features.
4. **Machine Learning Layer:** Spark MLlib trains distributed regression models to predict future utilization rates and wait times based on historical telemetry.
5. **Dashboard Layer:** Aggregated, clean datasets and model predictions are exported and visualized using industry-standard BI tools (e.g., Tableau or PowerBI) to create actionable Smart Grid dashboards.

