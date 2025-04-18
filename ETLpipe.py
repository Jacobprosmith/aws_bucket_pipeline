import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import boto3

# Load the raw CSV
df = pd.read_csv("fake_stock_data.csv", index_col="Date", parse_dates=True)
df.dropna(inplace=True)

# Normalize price features
scaler = MinMaxScaler()
df[['Open', 'High', 'Low', 'Close']] = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close']])

# Log-transform Volume
df['Volume'] = np.log1p(df['Volume'])

# Save the processed version
df.to_csv("processed_stock_data.csv")

processed_file_name = 'processed_stock_data.csv'
df.to_csv(processed_file_name)

# === S3 LOAD STEP ===

# Set up S3 variables
bucket_name = 'bucketpreparation'
s3_key = f'csv_cleaned_data/{processed_file_name}'

# Initialize boto3 S3 client
s3 = boto3.client('s3')

# Upload to S3
try:
    s3.upload_file(processed_file_name, bucket_name, s3_key)
    print(f"Successfully uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"Upload failed: {e}")