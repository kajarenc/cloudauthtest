import streamlit as st


direct_login = st.button("Login with direct redirect")

if direct_login:
    st.experimental_user.login()

send_to_host_login = st.button("Login with send to host")

if send_to_host_login:
    st.experimental_user.login(send_to_host=True)

st.write(st.experimental_user)
