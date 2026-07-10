import streamlit as st
import pandas as pd
import requests
import random
from datetime import datetime, timedelta

def fetch_patients():
    response = requests.get("https://randomuser.me/api?results=50")
    return response.json()['results']

def generate_healthcare_data(record_count):
    services = ['General Checkup', 'Blood Test', 'X-Ray', 'MRI', 'Surgery']
    data = []
    for _ in range(record_count):
        data.append({
            'service_id': random.randint(1000, 9999),
            'service_name': random.choice(services),
            'service_cost': round(random.uniform(50, 500), 2),
            'service_date': (datetime.now()-timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        })
    return pd.DataFrame(data)

def generate_medication_data(record_count):
    medications = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Amoxicillin', 'Metformin']
    data = []
    for _ in range(record_count):
        data.append({
            'medication_id': random.randint(1000, 9999),
            'medication_name': random.choice(medications),
            'dosage': f"{random.randint(1, 500)} mg",
            'medication_cost': round(random.uniform(5, 100), 2),
            'prescription_date': (datetime.now()-timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        })
    return pd.DataFrame(data)

def fetch_facilities():
    response = requests.get("https://health.data.ny.gov/resource/xdss-u53e.json")
    return pd.DataFrame(response.json())

def transform_patients(data):
    patients = []
    for patient in data:
        patients.append({
            'patient_id': patient['login']['uuid'],
            'name': f"{patient['name']['first']} {patient['name']['last']}",
            'email': patient['email'],
            'age': patient['dob']['age'],
            'gender': patient['gender'],
            'phone': patient['phone'],
            'city': patient['location']['city'],
            'country': patient['location']['country']
        })
    return pd.DataFrame(patients)

def assign_services_to_patients(patients, services):
    service_ids = services['service_id'].tolist()
    patients['service_id'] = [random.choice(service_ids) for _ in range(len(patients))]
    return patients

def assign_medications_to_patients(patients, medications):
    medication_ids = medications['medication_id'].tolist()
    patients['medication_id'] = [random.choice(medication_ids) for _ in range(len(patients))]
    return patients

def main():
    st.title("Realtime Healthcare Data Pipeline")
    st.write("THis dashboard simulates a real-time CI/CD data pipeline for healthcare organizations.")
    st.write("## Real-time data refresh")
    if st.button("Refresh Data"):
        st.experimental_rerun()

    patients_data = fetch_patients()
    healthcare_data = generate_healthcare_data(100)
    medication_data = generate_medication_data(100)
    facilities_data = fetch_facilities()

    patients_df = transform_patients(patients_data)

    patients_services_df = assign_services_to_patients(patients_df, healthcare_data)
    patients_services_df = patients_services_df.merge(healthcare_data, on='service_id', how='left')

    patients_med_df = assign_medications_to_patients(patients_services_df, medication_data)
    merged_df = patients_med_df.merge(medication_data, on='medication_id', how='left')

    st.write('### Patients Data')
    st.write(patients_df)

    st.write('### Healthcare Data')
    st.write(healthcare_data)

    st.write('### Medication Data')
    st.write(medication_data)

    st.write('### Healthcare Facilities Data')
    st.write(facilities_data.head(20))

    st.write('## Service cost distribution')
    st.bar_chart(merged_df['service_cost'])

    st.write('## Medication cost distribution')
    st.bar_chart(merged_df['medication_cost'])

    st.write('## Service count by type')
    service_count = merged_df['service_name'].value_counts()
    st.bar_chart(service_count)

    st.write('## Medication cost overtime')
    medication_cost_over_time = merged_df.groupby('prescription_date')['medication_cost'].sum().reset_index()
    st.line_chart(medication_cost_over_time.set_index('prescription_date'))

if __name__ == "__main__":
    main()

