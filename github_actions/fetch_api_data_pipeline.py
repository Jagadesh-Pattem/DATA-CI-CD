import requests
import pandas as pd
import os

API_URL = 'https://jsonplaceholder.typicode.com/posts';

DATA_FOLDER = 'data';
os.makedirs(DATA_FOLDER, exist_ok=True);

response = requests.get(API_URL);

if response.status_code == 200:
    data = response.json();
    df = pd.DataFrame(data);
    csv_file_path = os.path.join(DATA_FOLDER, 'api_data.csv');
    df.to_csv(csv_file_path, index=False);
    print(f"Data successfully fetched and saved to {csv_file_path}");
else:
    print(f"Failed to fetch data from API. Status Code: {response.status_code}");