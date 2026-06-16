import pandas as pd
import requests
import datetime

log_file = "etl_logs.log"

def log_message(msg):
    with open(log_file, "a") as f:
        f.write(f'{datetime.datetime.now()}-{msg}\n')

try:
    # Extract
    api_response = requests.get('https://jsonplaceholder.typicode.com/posts');
    data = api_response.json()
    df = pd.DataFrame(data)
    # Transform
    df['title_length'] = df['title'].apply(len)
    df['body_length'] = df['body'].apply(len)
    etl_timestamp = datetime.datetime.now()
    df['etl_timestamp'] = etl_timestamp
    # Load
    df.to_csv('etl_target.csv', index=False)
    print(f"ETL process completed at {etl_timestamp}")
    log_message(f"ETL process completed at {etl_timestamp}")
except Exception as e:
    log_message(f"Error occurred: {str(e)}")
