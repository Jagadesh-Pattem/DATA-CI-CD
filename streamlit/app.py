import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Hello!! Welcome to this enhanced Streamlit App")

user_name = st.text_input("Enter your name:", 'Jaga')

number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)

color = st.selectbox('Choose a color:', ['Red', 'Green', 'Blue'])

slider_value = st.slider('Select a value:', min_value=0, max_value=100, value=25)

if st.button('Submit'):
    st.write(f"Hello {user_name}! You entered the number {number}, selected the color {color}, and chose the value {slider_value}.")

data_length = 20

chart_data = {
    'a': [i for i in range(data_length)],
    'b': [i**2 for i in range(data_length)],
    'c': [i**0.5 for i in range(data_length)]
}

st.line_chart(chart_data)

st.bar_chart(chart_data)