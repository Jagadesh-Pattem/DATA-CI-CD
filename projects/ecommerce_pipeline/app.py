import streamlit as st
import pandas as pd
import requests
import random

def fetch_products():
    response = requests.get('https://fakestoreapi.com/products')
    return response.json()

def fetch_users():
    response = requests.get('https://randomuser.me/api?results=20')
    return response.json()['results']

def transform_products(products):
    df = pd.DataFrame(products)
    df = df[['id', 'title', 'price', 'category', 'description', 'image']]
    return df

def transform_users(users):
    user_data = []
    for user in users:
        user_data.append({
            'user_id': user['login']['uuid'],
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'city': user['location']['city'],
            'country': user['location']['country'],
            'picture': user['picture']['medium']
        })
    return pd.DataFrame(user_data)

def assign_sellers(products, users_data):
    user_ids = users_data['user_id'].tolist()
    products['seller_id'] = [random.choice(user_ids) for _ in range(len(user_ids))]
    return products.merge(users_data, left_on='seller_id', right_on='user_id')

def main():
    st.title("E-commerce data pipeline")
    st.write("This app visualizes e-commerce data fetched from Fake Store API and assigns random sellers")

    products_data = fetch_products()
    users_data = fetch_users()

    products_df = transform_products(products_data)
    users_df = transform_users(users_data)

    merged_df = assign_sellers(products_df, users_df)

    st.write("## Data")
    st.write(merged_df)

    st.write("## Data Summary")
    st.write(merged_df.describe())

    st.write("## Products Prices")
    st.bar_chart(merged_df['price'])

    if st.checkbox("Show product images"):
        st.write(" ## Product Images")
        for index, row in merged_df.iterrows():
            st.image(row['image'], caption=row['title'], width=100, use_column_width=False)
    
    if st.checkbox("Show seller images"):
        st.write(" ## Seller Images")
        for index, row in merged_df.iterrows():
            st.image(row['picture'], caption=row['name'], width=100, use_column_width=False)
            st.write(f"Name: {row['name']}")
            st.write(f"Email: {row['email']}")
            st.write(f"Location: {row['city']}, {row['country']}")
            st.write("------------------------------------")

if __name__ == "__main__":
    main()