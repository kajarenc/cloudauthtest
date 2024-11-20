import streamlit as st


google_login = st.button("Login with Google")

if google_login:
    st.experimental_user.login("google")

st.write(st.experimental_user)


logout_button = st.button("Logout")

if logout_button:
    st.experimental_user.logout()

x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)
