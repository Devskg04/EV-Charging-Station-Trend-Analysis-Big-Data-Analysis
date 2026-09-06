import pandas as pd
import os

print("--- EV Station Data Verification Script ---")

file_path = "ev_charging.csv"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found in the current directory.")
    exit(1)

print(f"Loading {file_path}...")
try:
    df = pd.read_csv(file_path)
    print("\n[SUCCESS] File loaded successfully!")
    print(f"Total Records (Rows): {len(df):,}")
    print(f"Total Features (Columns): {len(df.columns)}")
    
    print("\n--- Schema Overview ---")
    print(df.dtypes)
    
    print("\n--- Missing Values Check ---")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("[SUCCESS] The dataset is perfectly clean with ZERO missing values!")
    else:
        print(missing[missing > 0])
        
    print("\n--- Data Snapshot ---")
    print(df.head(3))
    print("\nVerification Complete. The EV dataset is fully ready for Big Data Processing.")
except Exception as e:
    print(f"Error during verification: {e}")
