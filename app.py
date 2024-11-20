import streamlit as st


google_login = st.button("Login with Google")

if google_login:
    st.experimental_user.login("google")


okta_login = st.button("Login with Okta")
if okta_login:
    st.experimental_user.login("okta")

st.write(st.experimental_user)


logout_button = st.button("Logout")

if logout_button:
    st.experimental_user.logout()

x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)


st.write("TEST FOR FILE UPLOADER")
x = st.file_uploader("Upload a photo")

if x is not None:
    st.image(x)
    st.write(x.name)
    st.write(x.type)
    st.write(x.size)
