import os 
import boto3 
import pandas as pd
import pyarrow as pa 
import pyarrow.parquet as pq 

def process_csv(csv_file: str, 
                output_dir:str, 
                bucket_name: str, 
                s3_key: str
                ) -> None:
    os.makedirs(output_dir, exist_ok=True)

    s3 = boto3.client('s3')

    df = pd.read_csv(csv_file)
    
    # Create a Json file only to compare file sizes
    json_file = os.path.join(output_dir, 'moviesAndTv.json')
    df.to_json(json_file, orient="records", lines=False)

    parquet_file = os.path.join(output_dir, "moviesAndTv.parquet")

    table = pa.Table.from_pandas(df)

    pq.write_table(table, parquet_file)

    s3.upload_file(parquet_file, bucket_name, s3_key)