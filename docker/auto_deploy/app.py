import pandas as pd
import numpy as np

customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'customer_name': ['Jaga', 'Soumya', 'Rajesh', 'Ramya', 'Alice'],
    'country': ['USA', 'India', 'UK', 'Canada', 'Australia']
});

print(customers)