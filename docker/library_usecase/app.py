import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    environment = os.getenv('ENVIRONMENT', 'dev')
    debug_mode = os.getenv('DEBUG_MODE', 'false')
    print(f"ENVIRONMENT: {environment}")
    print(f"DEBUG_MODE: {debug_mode}")
    data = {
        'name': ['Jaga', 'Soumya', 'Rajesh', 'Ramya'],
        'age': [29, 26, 31, 27],
        'salary': [20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

    avg_salary = np.mean(df['salary'])
    print(f"Avg Salary: {avg_salary}")

    plt.bar(df['name'], df['age'])
    plt.xlabel('Name')
    plt.ylabel('Age')
    plt.title('name vs Age')
    plt.show()


if __name__ == '__main__':
    main()