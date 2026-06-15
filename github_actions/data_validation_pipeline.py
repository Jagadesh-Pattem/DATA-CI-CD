import pandas as pd
import datetime

log_file = 'data_validation_log.txt'

def log_message(message):
    with open(log_file, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def validate_data(file_path):
    try:
        df = pd.read_csv(file_path)
        log_message("Data Loaded Successfully")
        errors = []
        #Check for null values
        if df.isnull().values.any():
            missing_data = df[df.isnull().any(axis=1)]
            errors.append(f'Missing data found:\n{missing_data}')
        #Check for invalid ages
        if not df['age'].apply(lambda x: str(x).isdigit()).all():
            invalid_age_data = df[~df['age'].apply(lambda x: str(x).isdigit())]
            errors.append(f'Invalid age found:\n{invalid_age_data}')
        
        if errors:
            for err in errors:
                log_message(err)
            log_message("Data validation failed with errors.")
        else:
            log_message("Data validation passed with no errors.")
        
    except Exception as e:
        log_message(f"Error validating data: {e}")
        return False
    
if __name__ == "__main__":
    file_path = 'github_actions/data.csv'
    validate_data(file_path)
