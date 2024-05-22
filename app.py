import streamlit as st


direct_login = st.button("Login with direct redirect")

if direct_login:
    st.experimental_user.login()

send_to_host_login = st.button("Login with send to host")

if send_to_host_login:
    st.experimental_user.login(send_redirect_to_host=True)

st.write(st.experimental_user)


logout_button = st.button("Logout")

if logout_button:
    st.experimental_user.logout()

x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)
