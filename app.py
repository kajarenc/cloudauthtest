import streamlit as st


login_button = st.button("Login")

if login_button:
    st.experimental_user.login()

st.write(st.experimental_user)
