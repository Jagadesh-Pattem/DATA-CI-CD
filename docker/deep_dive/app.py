import pandas as pd
import os

def main():
    env = os.getenv("ENVIRONMENT")
    print(f"Environment: {env}\n")

    data = {
        "name": ['jaga', 'soumya', 'rajesh', 'ramya'],
        "age": [29, 26, 31, 27]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

if __name__ == "__main__":
    main()