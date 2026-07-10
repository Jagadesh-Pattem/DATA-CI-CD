import streamlit as st
import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)
    return df

def transform_dataframe(df):
    df['Age_group'] = pd.cut(df['Age'], bins=[0, 30, 40, 50], labels=['Young', 'Middle-aged', 'Older'])
    return df

st.title("DataFrame Transformation App")

st.write("## Original DataFrame")
df = create_dataframe()
st.write(df)

st.write("## Transformed DataFrame")
transformed_df = transform_dataframe(df)
st.write(transformed_df)